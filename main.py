import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
)

from windows import (
    LoginWindow,
    RegisterWindow,
    MainScreenWindow,
    PublicationWindow,
    PublicationFormWindow,
    ProfileWindow,
    RecommendationsWindow,
    MentoringWindow,
    RatingWindow,
)

LOGIN = "login"
REGISTER = "register"
MAIN = "main"
PUBLICATION = "publication"
FORM = "form"
PROFILE = "profile"
RECOMMEND = "recommend"
MENTOR = "mentoring"
RATING = "rating"

PAGE_SIZE = 2

HINT_TEXT = (
    "В макетах нет кнопок перехода к перспективным экранам, поэтому они\n"
    "открываются с главной страницы клавишами:\n"
    "\n"
    "    F7 — экран рекомендаций\n"
    "    F8 — экран наставничества\n"
    "    F9 — экран рейтинга и достижений\n"
    "\n"
    "Вернуться на главную страницу с любого экрана:\n"
    "крестик окна или клавиша Esc."
)

CATEGORIES = ["Программирование", "Дизайн", "Маркетинг",
              "Управление проектами"]


DEMO_USER = {
    "name": "Иван Петров",
    "specialization": "Программирование",
    "experience": "Senior, 12 лет",
    "about": "Backend-разработчик. Делаюсь опытом по базам данных "
             "и оптимизации производительности.",
}

PUBLICATIONS = [
    {
        "id": 1,
        "title": "Оптимизация SQL-запросов на больших объёмах данных",
        "category": "Программирование",
        "author": "Иван Петров",
        "author_spec": "Программирование",
        "rating": 5,
        "comments": [
            {"author": "Мария Соколова",
             "text": "Спасибо, пункт про составные индексы очень помог!"},
            {"author": "Алексей Иванов",
             "text": "А что думаете о партиционировании больших таблиц?"},
        ],
        "text": (
            "Собрал приёмы, которые чаще всего дают наибольший прирост.\n\n"
            "1. Сначала смотрите план запроса (EXPLAIN), а не гадайте.\n"
            "2. Избегайте SELECT * - лишние столбцы мешают индексам.\n"
            "3. Составные индексы стройте по правилу «равенство -> диапазон».\n"
            "4. Разбивайте тяжёлые отчёты на батчи.\n\n"
            "Эти шаги снизили время отчёта с 40 секунд до 0.8 секунды."
        ),
    },
    {
        "id": 2,
        "title": "Дизайн-система с нуля: первые шаги команды",
        "category": "Дизайн",
        "author": "Мария Соколова",
        "author_spec": "Дизайн",
        "rating": 4,
        "comments": [
            {"author": "Елена Козлова", "text": "Отличный разбор, ждём продолжение!"},
        ],
        "text": (
            "Как мы за месяц собрали базовую дизайн-систему.\n\n"
            "1. Аудит экранов и повторяющихся элементов.\n"
            "2. Палитра, типографика и сетка.\n"
            "3. Библиотека компонентов с токенами.\n"
            "4. Синхронизация с разработчиками."
        ),
    },
    {
        "id": 3,
        "title": "Kanban или Scrum: как выбрать подход под команду",
        "category": "Управление проектами",
        "author": "Елена Козлова",
        "author_spec": "Управление проектами",
        "rating": 4,
        "comments": [],
        "text": (
            "Короткий чек-лист выбора:\n\n"
            "- Поток однотипных задач -> Kanban.\n"
            "- Сложный продукт с релизами -> Scrum.\n"
            "- Смешанный поток -> Scrumban с ограничением WIP."
        ),
    },
    {
        "id": 4,
        "title": "Как посчитать ROMI без боли: старт для малого бизнеса",
        "category": "Маркетинг",
        "author": "Алексей Иванов",
        "author_spec": "Маркетинг",
        "rating": 3,
        "comments": [],
        "text": (
            "Формула простая: (доход от канала - расходы) / расходы.\n"
            "Сложность в атрибуции. Для старта достаточно last-click "
            "и таблицы в 5 столбцов."
        ),
    },
    {
        "id": 5,
        "title": "Онбординг новых разработчиков: чек-лист первой недели",
        "category": "Программирование",
        "author": "Пётр Смирнов",
        "author_spec": "Программирование",
        "rating": 4,
        "comments": [
            {"author": "Иван Петров", "text": "Добавил бы в чек-лист доступ к логам."},
        ],
        "text": (
            "Что дать новичку в первый день: репозиторий, стенд, "
            "наставника и одну маленькую задачу в первый же день. "
            "Так человек быстро чувствует пользу и вливается в команду."
        ),
    },
]

MENTORS = [
    {"name": "Иван Петров", "theme": "Программирование",
     "experience": "12 лет"},
    {"name": "Мария Соколова", "theme": "Дизайн", "experience": "8 лет"},
    {"name": "Елена Козлова", "theme": "Управление проектами",
     "experience": "10 лет"},
]

ACHIEVEMENTS = [
    "Первая публикация - 10 баллов",
    "Активный комментатор - 25 баллов",
    "Публикация с оценкой 5 - 20 баллов",
]

TOP_SPECIALISTS = [
    "1. Иван Петров - 120 баллов",
    "2. Мария Соколова - 95 баллов",
    "3. Елена Козлова - 80 баллов",
]


class App:
    def __init__(self):
        self.user = None
        self.current_pub = None
        self.form_mode = "create"
        self.page = 1
        self.requests = []
        self._pub_origin = MAIN
        self._hint_shown = False

        self.windows = {
            LOGIN: LoginWindow(),
            REGISTER: RegisterWindow(),
            MAIN: MainScreenWindow(),
            PUBLICATION: PublicationWindow(),
            FORM: PublicationFormWindow(),
            PROFILE: ProfileWindow(),
            RECOMMEND: RecommendationsWindow(),
            MENTOR: MentoringWindow(),
            RATING: RatingWindow(),
        }
        self.current = None


        self.windows[MAIN].set_categories(["Все категории"] + CATEGORIES)
        self.windows[FORM].set_categories(CATEGORIES)
        self.windows[MENTOR].set_themes(["Все темы"] + CATEGORIES)

        self._wire()
        self._wire_closing()
        self._wire_shortcuts()
        self.go(LOGIN)


    def _wire(self):
        w = self.windows


        w[LOGIN].on("loginButton", "clicked", self.do_login)
        w[LOGIN].on("pushButton", "clicked",
                    lambda: self.go(REGISTER))

        w[REGISTER].on("registerButton", "clicked", self.do_register)
        w[REGISTER].on("pushButton", "clicked",
                       lambda: self.go(LOGIN))

        w[MAIN].on("createPublicationButton", "clicked", self.open_create_form)
        w[MAIN].on("profileButton", "clicked", lambda: self.go(PROFILE))
        w[MAIN].on("logoutButton", "clicked", self.do_logout)
        w[MAIN].on("searchEdit", "textChanged",
                   lambda _text: self.refresh_main())
        w[MAIN].on("categoryCombo", "currentIndexChanged",
                   lambda _index: self.refresh_main())
        w[MAIN].clicked.connect(
            lambda pub_id: self.open_publication(pub_id, MAIN))

        w[MAIN].open_recommendations.connect(lambda: self.go(RECOMMEND))
        w[MAIN].open_mentoring.connect(lambda: self.go(MENTOR))
        w[MAIN].open_ratings.connect(lambda: self.go(RATING))

        w[MAIN].on("prevPageButton", "clicked",
                   lambda: self.set_page(self.page - 1))
        w[MAIN].on("nextPageButton", "clicked",
                   lambda: self.set_page(self.page + 1))
        for number, button_name in enumerate(
                ("page1Button", "page2Button", "page3Button"), start=1):
            w[MAIN].on(button_name, "clicked",
                       lambda _checked=False, p=number: self.set_page(p))

        for number in range(1, 6):
            w[PUBLICATION].on(
                f"rating{number}Button", "clicked",
                lambda _checked=False, value=number: self.rate_current(value))
        w[PUBLICATION].on("sendButton", "clicked", self.add_comment)

        w[FORM].on("saveButton", "clicked", self.save_form)
        w[FORM].on("cancelButton", "clicked", self.cancel_form)


        w[PROFILE].on("editProfileButton", "clicked", self.edit_profile_dialog)
        w[PROFILE].clicked.connect(                             # клик по строке
            lambda pub_id: self.open_publication(pub_id, PROFILE))
        for row in (1, 2, 3):
            w[PROFILE].on(f"row{row}EditButton", "clicked",
                          lambda _c=False, r=row: self.edit_row_publication(r))
            w[PROFILE].on(f"row{row}DeleteButton", "clicked",
                          lambda _c=False, r=row: self.delete_row_publication(r))

        w[RECOMMEND].on("configureInterestsButton", "clicked",
                        self.interests_dialog)
        w[RECOMMEND].clicked.connect(
            lambda pub_id: self.open_publication(pub_id, RECOMMEND))

        w[MENTOR].on("searchButton", "clicked", self.refresh_mentoring)
        w[MENTOR].on("themeCombo", "currentIndexChanged",
                     lambda _index: self.refresh_mentoring())
        w[MENTOR].on("myRequestsButton", "clicked", self.show_requests)
        for row in (1, 2, 3):
            w[MENTOR].on(f"mentor{row}RequestButton", "clicked",
                         lambda _c=False, r=row: self.send_mentor_request(r))


    def _wire_closing(self):
        w = self.windows
        w[REGISTER].close_handler = lambda: self.go(LOGIN)
        w[PUBLICATION].close_handler = lambda: self.go(self._pub_origin)
        w[FORM].close_handler = self.cancel_form
        w[PROFILE].close_handler = lambda: self.go(MAIN)
        w[RECOMMEND].close_handler = lambda: self.go(MAIN)
        w[MENTOR].close_handler = lambda: self.go(MAIN)
        w[RATING].close_handler = lambda: self.go(MAIN)

    def _wire_shortcuts(self):
        w = self.windows
        self._shortcuts = []

        def add_shortcut(key, window, handler):
            shortcut = QShortcut(QKeySequence(key), window)
            shortcut.activated.connect(handler)
            self._shortcuts.append(shortcut)


        for name in (REGISTER, PUBLICATION, FORM, PROFILE,
                     RECOMMEND, MENTOR, RATING):
            add_shortcut(Qt.Key.Key_Escape, w[name], w[name].close)
        add_shortcut(Qt.Key.Key_F7, w[MAIN], lambda: self.go(RECOMMEND))
        add_shortcut(Qt.Key.Key_F8, w[MAIN], lambda: self.go(MENTOR))
        add_shortcut(Qt.Key.Key_F9, w[MAIN], lambda: self.go(RATING))

    def go(self, name, **data):
        target = self.windows[name]
        if self.current is not None and self.current is not target:
            target.move(self.current.pos())   # открыть на том же месте
            self.current.hide()
        self.current = target
        target.show()
        self._refresh(name, **data)

    def _refresh(self, name, **data):
        if name == MAIN:
            self.refresh_main()
        elif name == PUBLICATION:
            self.refresh_publication(data.get("pub_id"))
        elif name == FORM:
            self.refresh_form(data.get("pub_id"))
        elif name == PROFILE:
            self.refresh_profile()
        elif name == RECOMMEND:
            self.refresh_recommendations()
        elif name == MENTOR:
            self.refresh_mentoring()
        elif name == RATING:
            self.refresh_rating()

    def do_login(self):
        login, password = self.windows[LOGIN].credentials()
        if not login or not password:
            self.windows[LOGIN].show_error("Введите логин и пароль.")
            return

        self.user = dict(DEMO_USER)
        self.user["interests"] = [self.user["specialization"]]
        self.windows[LOGIN].show_error("")
        self.page = 1
        self.go(MAIN)
        self._show_first_hint()

    def do_register(self):
        form = self.windows[REGISTER].data()
        if not all(form.values()):
            QMessageBox.warning(
                self.windows[REGISTER], "Регистрация",
                "Заполните все поля формы.")
            return
        if form["password"] != form["password2"]:
            QMessageBox.warning(
                self.windows[REGISTER], "Регистрация",
                "Пароли не совпадают.")
            return
        if "@" not in form["email"] or "." not in form["email"]:
            QMessageBox.warning(
                self.windows[REGISTER], "Регистрация",
                "Некорректный e-mail.")
            return
        self.user = {
            "name": form["login"],
            "specialization": "Не указана",
            "experience": "Не указан",
            "about": "—",
            "interests": [],
        }
        self.requests = []
        self.page = 1
        self.go(MAIN)
        self._show_first_hint()

    def do_logout(self):
        self.user = None
        self.current_pub = None
        self.requests = []
        self.page = 1
        self.windows[LOGIN].reset()
        self.go(LOGIN)

    def _show_first_hint(self):
        if self._hint_shown:
            return
        self._hint_shown = True
        QMessageBox.information(
            self.windows[MAIN], "Навигация по платформе", HINT_TEXT)

    def refresh_main(self):
        keyword, category = self.windows[MAIN].filter_params()
        pubs = []
        for pub in PUBLICATIONS:
            if category != "Все категории" and pub["category"] != category:
                continue
            if keyword and keyword not in pub["title"].lower() \
                    and keyword not in pub["text"].lower():
                continue
            pubs.append(pub)
        total_pages = max(1, -(-len(pubs) // PAGE_SIZE))  # округление вверх
        self.page = min(max(self.page, 1), total_pages)
        start = (self.page - 1) * PAGE_SIZE
        self.windows[MAIN].fill_cards(
            pubs[start:start + PAGE_SIZE], self.page, total_pages)

    def set_page(self, page):
        self.page = page
        self.refresh_main()

    def open_publication(self, pub_id, origin=MAIN):
        self._pub_origin = origin
        self.go(PUBLICATION, pub_id=pub_id)

    def refresh_publication(self, pub_id):
        pub = next((p for p in PUBLICATIONS if p["id"] == pub_id), None)
        if pub is None:
            return
        self.current_pub = pub
        self.windows[PUBLICATION].show_publication(pub)

    def rate_current(self, value):
        if self.current_pub is None:
            return
        self.current_pub["rating"] = value
        QMessageBox.information(
            self.windows[PUBLICATION], "Оценка",
            f"Ваша оценка «{value}» сохранена.")

    def add_comment(self):
        window = self.windows[PUBLICATION]
        text = window.comment_text()
        if self.current_pub is None or self.user is None or not text:
            return
        self.current_pub["comments"].append(
            {"author": self.user["name"], "text": text})
        window.clear_comment_input()
        self.refresh_publication(self.current_pub["id"])

    def open_create_form(self):
        self.go(FORM)

    def refresh_form(self, pub_id):
        if pub_id is None:
            self.form_mode = "create"
            self.windows[FORM].mode_create()
        else:
            pub = next(p for p in PUBLICATIONS if p["id"] == pub_id)
            self.form_mode = "edit"
            self.current_pub = pub
            self.windows[FORM].mode_edit(pub)

    def save_form(self):
        title, category, text = self.windows[FORM].values()
        if not title or not text:
            QMessageBox.warning(
                self.windows[FORM], "Публикация",
                "Заполните название и текст публикации.")
            return
        if self.form_mode == "create":
            new_id = max((p["id"] for p in PUBLICATIONS), default=0) + 1
            PUBLICATIONS.append({
                "id": new_id,
                "title": title,
                "category": category,
                "author": self.user["name"],
                "author_spec": self.user.get("specialization", "—"),
                "rating": 0,
                "comments": [],
                "text": text,
            })
            self.page = -(-len(PUBLICATIONS) // PAGE_SIZE)
            self.go(MAIN)
        else:
            pub = self.current_pub
            pub["title"] = title
            pub["category"] = category
            pub["text"] = text
            self.go(PUBLICATION, pub_id=pub["id"])

    def cancel_form(self):
        if self.form_mode == "create":
            self.go(MAIN)
        else:
            self.go(PUBLICATION, pub_id=self.current_pub["id"])

    def refresh_profile(self):
        user = self.user or {}
        my_pubs = [
            p for p in PUBLICATIONS if p["author"] == user.get("name")
        ]
        self.windows[PROFILE].show_profile(user, my_pubs[:3])

    def edit_row_publication(self, row):
        pub_id = self.windows[PROFILE].row_pub_id(row)
        if pub_id:
            self._pub_origin = PROFILE
            self.go(FORM, pub_id=pub_id)

    def delete_row_publication(self, row):
        pub_id = self.windows[PROFILE].row_pub_id(row)
        if not pub_id:
            return
        pub = next((p for p in PUBLICATIONS if p["id"] == pub_id), None)
        if pub is None:
            return
        result = QMessageBox.question(
            self.windows[PROFILE], "Удаление публикации",
            f"Удалить публикацию «{pub['title']}»?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if result != QMessageBox.StandardButton.Yes:
            return
        PUBLICATIONS.remove(pub)
        if self.current_pub is pub:
            self.current_pub = None
        self.refresh_profile()

    def edit_profile_dialog(self):
        if self.user is None:
            return
        user = self.user
        dialog = QDialog(self.windows[PROFILE])
        dialog.setWindowTitle("Редактирование профиля")
        dialog.resize(360, 240)
        form = QFormLayout(dialog)
        name_edit = QLineEdit(user.get("name", ""))
        spec_edit = QLineEdit(user.get("specialization", ""))
        exp_edit = QLineEdit(user.get("experience", ""))
        about_edit = QPlainTextEdit(user.get("about", ""))
        form.addRow("Имя:", name_edit)
        form.addRow("Специализация:", spec_edit)
        form.addRow("Опыт:", exp_edit)
        form.addRow("О себе:", about_edit)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        form.addRow(buttons)
        if dialog.exec():
            user["name"] = name_edit.text().strip() or user["name"]
            user["specialization"] = spec_edit.text().strip()
            user["experience"] = exp_edit.text().strip()
            user["about"] = about_edit.toPlainText().strip()
            # здесь будет сохранение профиля в базе данных
            self.refresh_profile()


    def refresh_recommendations(self):
        interests = (self.user or {}).get("interests", [])
        scored = []
        for pub in PUBLICATIONS:
            if pub["category"] in interests:
                relevance = 95
            else:
                relevance = min(90, 60 + pub["rating"] * 6)
            scored.append((pub, relevance))
        scored.sort(key=lambda item: item[1], reverse=True)
        self.windows[RECOMMEND].fill(scored[:2])

    def interests_dialog(self):
        if self.user is None:
            return
        dialog = QDialog(self.windows[RECOMMEND])
        dialog.setWindowTitle("Мои интересы")
        dialog.resize(280, 180)
        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(dialog)
        boxes = []
        for category in CATEGORIES:
            box = QCheckBox(category)
            box.setChecked(category in self.user.get("interests", []))
            boxes.append(box)
            layout.addWidget(box)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        if dialog.exec():
            self.user["interests"] = [b.text() for b in boxes if b.isChecked()]
            self.refresh_recommendations()

    def refresh_mentoring(self):
        theme = self.windows[MENTOR].current_theme()
        if theme in ("Все темы", ""):
            mentors = list(MENTORS)
        else:
            mentors = [m for m in MENTORS if m["theme"] == theme]
        self.windows[MENTOR].fill(mentors)

    def send_mentor_request(self, row):
        mentor = self.windows[MENTOR].row_mentor(row)
        if mentor is None:
            return
        self.requests.append(mentor["name"])
        QMessageBox.information(
            self.windows[MENTOR], "Заявка на наставничество",
            f"Заявка наставнику {mentor['name']} отправлена.")

    def show_requests(self):
        if not self.requests:
            QMessageBox.information(
                self.windows[MENTOR], "Мои заявки",
                "У вас пока нет заявок.")
            return
        listing = "\n".join(f"• {name}" for name in self.requests)
        QMessageBox.information(
            self.windows[MENTOR], "Мои заявки", f"Ваши заявки:\n{listing}")

    def refresh_rating(self):
        self.windows[RATING].show_rating(
            points=120,
            level="Специалист",
            progress=45,
            achievements=ACHIEVEMENTS,
            specialists=TOP_SPECIALISTS,
        )


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    print("Подсказка: F7 — рекомендации, F8 — наставничество, F9 — рейтинг. "
          "Esc или крестик окна — вернуться на главную страницу.")
    controller = App()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
