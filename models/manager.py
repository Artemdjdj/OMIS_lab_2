import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DBManager:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName(os.getenv("DB_HOST", "localhost"))
        self.db.setPort(int(os.getenv("DB_PORT", 5434)))
        self.db.setDatabaseName(os.getenv("DB_NAME", "db"))
        self.db.setUserName(os.getenv("DB_USER", "user"))
        self.db.setPassword(os.getenv("DB_PASSWORD", "password"))
        if not self.db.open():
            raise RuntimeError(self.db.lastError().text())

    def get_categories(self):
        q = QSqlQuery()
        if not q.exec("SELECT title FROM categories ORDER BY title"):
            print("CATEGORIES ERROR:", q.lastError().text())
            return []
        result = []
        while q.next():
            result.append(q.value(0))
        return result

    def get_publications(self):
        q = QSqlQuery()
        sql = """
              SELECT p.id,
                     p.title,
                     p.text,
                     COALESCE(c.title, '')          AS category,
                     COALESCE(pr.name, s.login, '') AS author,
                     COALESCE(AVG(g.value), 0)      AS rating
              FROM publications p
                       LEFT JOIN categories c ON c.id = p.category_id
                       LEFT JOIN specialists s ON s.id = p.specialist_id
                       LEFT JOIN profiles pr ON pr.specialist_id = s.id
                       LEFT JOIN grades g ON g.publication_id = p.id
              GROUP BY p.id, p.title, p.text, c.title, pr.name, s.login
              ORDER BY p.id DESC \
              """
        if not q.exec(sql):
            print("PUBLICATIONS ERROR:", q.lastError().text())
            return []

        pubs = {}
        order = []
        while q.next():
            pid = q.value(0)
            pubs[pid] = {
                "id": pid,
                "title": q.value(1),
                "text": q.value(2),
                "category": q.value(3),
                "author": q.value(4),
                "rating": float(q.value(5) or 0),
                "comments": [],
            }
            order.append(pid)

        q2 = QSqlQuery()
        sql2 = """
               SELECT cm.publication_id,
                      cm.text,
                      COALESCE(pr.name, s.login, '') AS author
               FROM comments cm
                        LEFT JOIN specialists s ON s.id = cm.specialist_id
                        LEFT JOIN profiles pr ON pr.specialist_id = s.id
               ORDER BY cm.creation_date \
               """
        if not q2.exec(sql2):
            print("COMMENTS ERROR:", q2.lastError().text())
        else:
            while q2.next():
                pid = q2.value(0)
                if pid in pubs:
                    pubs[pid]["comments"].append({
                        "text": q2.value(1),
                        "author": q2.value(2),
                    })

        return [pubs[pid] for pid in order]

    def get_user(self, login="ivan"):
        q = QSqlQuery()
        q.prepare("""
                  SELECT s.id, s.login, pr.name, pr.specialisation, pr.experience, pr.information
                  FROM specialists s
                           LEFT JOIN profiles pr ON pr.specialist_id = s.id
                  WHERE s.login = :login
                  """)
        q.bindValue(":login", login)
        if not q.exec():
            print("USER ERROR:", q.lastError().text())
            return None
        if not q.next():
            return None
        return {
            "id": q.value(0),
            "login": q.value(1),
            "name": q.value(2) or q.value(1),
            "specialization": q.value(3) or "",
            "experience": q.value(4) or "",
            "about": q.value(5) or "",
        }

    def get_mentors(self, theme=None):
        q = QSqlQuery()
        if theme and theme not in ("Все темы", ""):
            q.prepare("""
                      SELECT pr.name, pr.specialisation, pr.experience
                      FROM profiles pr
                               JOIN specialists s ON s.id = pr.specialist_id
                      WHERE pr.specialisation = :theme
                      ORDER BY pr.name
                      """)
            q.bindValue(":theme", theme)
            ok = q.exec()
        else:
            ok = q.exec("""
                        SELECT pr.name, pr.specialisation, pr.experience
                        FROM profiles pr
                                 JOIN specialists s ON s.id = pr.specialist_id
                        ORDER BY pr.name
                        """)
        if not ok:
            print("MENTORS ERROR:", q.lastError().text())
            return []
        result = []
        while q.next():
            result.append({
                "name": q.value(0),
                "theme": q.value(1),
                "experience": q.value(2),
            })
        return result

    def get_user_stats(self, specialist_id):
        q = QSqlQuery()
        q.prepare("""
                  SELECT (SELECT COUNT(*) FROM publications WHERE specialist_id = :id),
                         (SELECT COUNT(*) FROM comments WHERE specialist_id = :id),
                         COALESCE((SELECT SUM(g.value)
                                   FROM grades g
                                            JOIN publications p ON p.id = g.publication_id
                                   WHERE p.specialist_id = :id), 0),
                         COALESCE((SELECT AVG(g.value)
                                   FROM grades g
                                            JOIN publications p ON p.id = g.publication_id
                                   WHERE p.specialist_id = :id), 0)
                  """)
        q.bindValue(":id", specialist_id)
        if not q.exec() or not q.next():
            print("STATS ERROR:", q.lastError().text())
            return {"points": 0, "pubs": 0, "comments": 0, "avg": 0.0}
        pubs = int(q.value(0) or 0)
        comments = int(q.value(1) or 0)
        grade_sum = int(q.value(2) or 0)
        grade_avg = float(q.value(3) or 0)
        points = 10 * pubs + 5 * comments + grade_sum
        return {"points": points, "pubs": pubs, "comments": comments, "avg": grade_avg}

    def get_achievements(self, specialist_id, stats=None):
        if stats is None:
            stats = self.get_user_stats(specialist_id)
        result = []
        if stats["pubs"] >= 1:
            result.append("Первая публикация - 10 баллов")
        if stats["comments"] >= 2:
            result.append("Активный комментатор - 25 баллов")
        if stats["avg"] >= 4.5:
            result.append("Публикация с высокой оценкой - 20 баллов")
        if not result:
            result.append("Достижений пока нет")
        return result

    def get_level_info(self, points):
        if points < 50:
            return "Новичок", int(points * 100 / 50)
        if points < 150:
            return "Специалист", int((points - 50) * 100 / 100)
        return "Эксперт", 100

    def get_top_specialists(self, limit=3):
        q = QSqlQuery()
        sql = f"""
            SELECT COALESCE(pr.name, s.login) AS name,
                   10 * (SELECT COUNT(*) FROM publications pu WHERE pu.specialist_id = s.id) +
                   5  * (SELECT COUNT(*) FROM comments cm WHERE cm.specialist_id = s.id) +
                   COALESCE((SELECT SUM(g.value) FROM grades g
                             JOIN publications pu2 ON pu2.id = g.publication_id
                             WHERE pu2.specialist_id = s.id), 0) AS points
            FROM specialists s
            LEFT JOIN profiles pr ON pr.specialist_id = s.id
            ORDER BY points DESC
            LIMIT {int(limit)}
        """
        if not q.exec(sql):
            print("TOP ERROR:", q.lastError().text())
            return []
        result = []
        idx = 0
        while q.next():
            idx += 1
            result.append(f"{idx}. {q.value(0) or ''} - {int(q.value(1) or 0)} баллов")
        return result

    def get_rating_data(self, specialist_id):
        stats = self.get_user_stats(specialist_id)
        level, progress = self.get_level_info(stats["points"])
        return {
            "points": stats["points"],
            "level": level,
            "progress": progress,
            "achievements": self.get_achievements(specialist_id, stats),
            "specialists": self.get_top_specialists(),
        }

    def save_categories(self, data, author):
        pass
