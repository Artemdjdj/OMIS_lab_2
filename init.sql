BEGIN;

CREATE TABLE specialists (
    id                SERIAL       PRIMARY KEY,
    login             VARCHAR(100) NOT NULL UNIQUE,
    password          VARCHAR(500) NOT NULL,
    email             VARCHAR(100) NOT NULL UNIQUE,
    registration_date TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id    SERIAL      PRIMARY KEY,
    title VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE profiles (
    id             SERIAL       PRIMARY KEY,
    name           VARCHAR(50)  NOT NULL,
    specialisation VARCHAR(40)  NOT NULL,
    experience     VARCHAR(100) NOT NULL,
    information    VARCHAR(500) NOT NULL,
    specialist_id  INTEGER      NOT NULL UNIQUE,
    CONSTRAINT fk_profiles_specialist
        FOREIGN KEY (specialist_id) REFERENCES specialists (id) ON DELETE CASCADE
);

CREATE TABLE publications (
    id            SERIAL       PRIMARY KEY,
    title         VARCHAR(100) NOT NULL,
    text          VARCHAR(500) NOT NULL,
    creation_date TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    specialist_id INTEGER      NOT NULL,
    category_id   INTEGER      NOT NULL,
    CONSTRAINT fk_publications_specialist
        FOREIGN KEY (specialist_id) REFERENCES specialists (id) ON DELETE CASCADE,
    CONSTRAINT fk_publications_category
        FOREIGN KEY (category_id)   REFERENCES categories (id)  ON DELETE CASCADE
);

CREATE TABLE comments (
    id             SERIAL       PRIMARY KEY,
    text           VARCHAR(500) NOT NULL,
    creation_date  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    specialist_id  INTEGER      NOT NULL,
    publication_id INTEGER      NOT NULL,
    CONSTRAINT fk_comments_specialist
        FOREIGN KEY (specialist_id)  REFERENCES specialists (id)  ON DELETE CASCADE,
    CONSTRAINT fk_comments_publication
        FOREIGN KEY (publication_id) REFERENCES publications (id) ON DELETE CASCADE
);

CREATE TABLE grades (
    id             SERIAL  PRIMARY KEY,
    value          INTEGER NOT NULL,
    specialist_id  INTEGER NOT NULL,
    publication_id INTEGER NOT NULL,
    CONSTRAINT chk_grades_value
        CHECK (value >= 0 AND value <= 10),
    CONSTRAINT uq_grades_once
        UNIQUE (specialist_id, publication_id),
    CONSTRAINT fk_grades_specialist
        FOREIGN KEY (specialist_id)  REFERENCES specialists (id)  ON DELETE CASCADE,
    CONSTRAINT fk_grades_publication
        FOREIGN KEY (publication_id) REFERENCES publications (id) ON DELETE CASCADE
);


INSERT INTO specialists (id, login, password, email, registration_date) VALUES
    (1, 'ivan',   '1234', 'ivan.petrov@example.com',    TIMESTAMP '2026-09-01 10:15:00'),
    (2, 'maria',  '1234', 'maria.sokolova@example.com', TIMESTAMP '2026-09-03 14:30:00'),
    (3, 'elena',  '1234', 'elena.kozlova@example.com',  TIMESTAMP '2026-09-05 09:45:00'),
    (4, 'alexey', '1234', 'alexey.ivanov@example.com',  TIMESTAMP '2026-09-07 18:20:00'),
    (5, 'petr',   '1234', 'petr.smirnov@example.com',   TIMESTAMP '2026-09-10 12:00:00');

INSERT INTO categories (id, title) VALUES
    (1, 'Программирование'),
    (2, 'Дизайн'),
    (3, 'Управление проектами'),
    (4, 'Маркетинг');

INSERT INTO profiles (id, name, specialisation, experience, information, specialist_id) VALUES
    (1, 'Иван Петров', 'Программирование', 'Senior, 12 лет',
     'Backend-разработчик. Делаюсь опытом по базам данных и оптимизации производительности.',
     1),
    (2, 'Мария Соколова', 'Дизайн', 'Middle, 8 лет',
     'Продуктовый дизайнер. Собираю дизайн-системы и делюсь практиками UI/UX.',
     2),
    (3, 'Елена Козлова', 'Управление проектами', 'Senior, 10 лет',
     'Руководитель проектов. Помогаю командам выстроить процесс без бюрократии.',
     3),
    (4, 'Алексей Иванов', 'Маркетинг', 'Middle, 6 лет',
     'Маркетолог. Настраиваю аналитику и считаю ROMI для малого бизнеса.',
     4),
    (5, 'Пётр Смирнов', 'Программирование', 'Middle, 7 лет',
     'Teamlead. Занимаюсь онбордингом разработчиков и внутренними инструментами.',
     5);

INSERT INTO publications (id, title, text, creation_date, specialist_id, category_id) VALUES
    (1, 'Оптимизация SQL-запросов на больших объёмах данных',
     E'Собрал приёмы, которые чаще всего дают наибольший прирост.\n\n1. Сначала смотрите план запроса (EXPLAIN), а не гадайте.\n2. Избегайте SELECT * - лишние столбцы мешают индексам.\n3. Составные индексы стройте по правилу «равенство -> диапазон».\n4. Разбивайте тяжёлые отчёты на батчи.\n\nЭти шаги снизили время отчёта с 40 секунд до 0.8 секунды.',
     TIMESTAMP '2026-10-05 11:00:00', 1, 1),
    (2, 'Дизайн-система с нуля: первые шаги команды',
     E'Как мы за месяц собрали базовую дизайн-систему.\n\n1. Аудит экранов и повторяющихся элементов.\n2. Палитра, типографика и сетка.\n3. Библиотека компонентов с токенами.\n4. Синхронизация с разработчиками.',
     TIMESTAMP '2026-10-12 10:30:00', 2, 2),
    (3, 'Kanban или Scrum: как выбрать подход под команду',
     E'Короткий чек-лист выбора:\n\n- Поток однотипных задач -> Kanban.\n- Сложный продукт с релизами -> Scrum.\n- Смешанный поток -> Scrumban с ограничением WIP.',
     TIMESTAMP '2026-10-15 16:20:00', 3, 3),
    (4, 'Как посчитать ROMI без боли: старт для малого бизнеса',
     E'Формула простая: (доход от канала - расходы) / расходы.\nСложность в атрибуции. Для старта достаточно last-click и таблицы в 5 столбцов.',
     TIMESTAMP '2026-10-20 09:10:00', 4, 4),
    (5, 'Онбординг новых разработчиков: чек-лист первой недели',
     E'Что дать новичку в первый день: репозиторий, стенд, наставника и одну маленькую задачу в первый же день. Так человек быстро чувствует пользу и вливается в команду.',
     TIMESTAMP '2026-10-25 14:40:00', 5, 1);

INSERT INTO comments (id, text, creation_date, specialist_id, publication_id) VALUES
    (1, 'Спасибо, пункт про составные индексы очень помог!',
     TIMESTAMP '2026-10-06 09:30:00', 2, 1),
    (2, 'А что думаете о партиционировании больших таблиц?',
     TIMESTAMP '2026-10-06 15:45:00', 4, 1),
    (3, 'Отличный разбор, ждём продолжение!',
     TIMESTAMP '2026-10-13 13:10:00', 3, 2),
    (4, 'Добавил бы в чек-лист доступ к логам.',
     TIMESTAMP '2026-10-26 10:05:00', 1, 5);

INSERT INTO grades (id, value, specialist_id, publication_id) VALUES
    (1,  5, 2, 1), (2,  5, 4, 1), (3,  4, 3, 1), (4,  6, 5, 1),
    (5,  4, 1, 2), (6,  3, 4, 2), (7,  5, 3, 2), (8,  4, 5, 2),
    (9,  5, 1, 3), (10, 3, 2, 3), (11, 4, 4, 3), (12, 4, 5, 3),
    (13, 3, 1, 4), (14, 3, 2, 4), (15, 2, 3, 4), (16, 4, 5, 4),
    (17, 4, 1, 5), (18, 5, 2, 5), (19, 3, 3, 5), (20, 4, 4, 5);
COMMIT;
