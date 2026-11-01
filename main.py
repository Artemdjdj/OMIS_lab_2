import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QMessageBox

from repository.publication_repository import PublicationRepository
from service.publication_service import PublicationService
from windows import (
    LoginWindow, RegisterWindow, MainScreenWindow, PublicationWindow,
    PublicationFormWindow, ProfileWindow, RecommendationsWindow,
    MentoringWindow, RatingWindow,
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


class App:
    def __init__(self):
        self.user = None
        self.current_pub = None
        self.form_mode = "create"
        self.page = 1
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

        self.publicationService = PublicationService(PublicationRepository())
        categories = self.publicationService.get_categories() or []
        self.windows[MAIN].set_categories(["Все категории"] + categories)
        self.windows[FORM].set_categories(categories)
        self.windows[MENTOR].set_themes(["Все темы"] + categories)

        self._wire()
        self._wire_closing()
        self._wire_shortcuts()
        self.go(LOGIN)

    def _safe_on(self, window, name, signal, handler):
        try:
            window.on(name, signal, handler)
        except AttributeError:
            pass

    def _wire(self):
        w = self.windows

        w[LOGIN].on("loginButton", "clicked", self.do_login)
        w[LOGIN].on("pushButton", "clicked", lambda: self.go(REGISTER))

        w[REGISTER].on("registerButton", "clicked", self.do_register)
        w[REGISTER].on("pushButton", "clicked", lambda: self.go(LOGIN))

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

        w[FORM].on("cancelButton", "clicked", self.cancel_form)
        for save_name in ("saveButton", "savePublicationButton",
                          "publishButton", "saveButton2"):
            self._safe_on(w[FORM], save_name, "clicked", self.save_form)

        for row in (1, 2, 3):
            w[PROFILE].on(f"row{row}EditButton", "clicked",
                          lambda _c=False, r=row: self.edit_row_publication(r))
            self._safe_on(w[PROFILE], f"row{row}DeleteButton", "clicked",
                          lambda _c=False, r=row: self.delete_row_publication(r))
        w[PROFILE].clicked.connect(
            lambda pub_id: self.open_publication(pub_id, PROFILE))

        for name in ("editProfileButton", "editButton"):
            self._safe_on(w[PROFILE], name, "clicked", self.edit_profile)
        for name in ("saveProfileButton", "saveButton", "saveChangesButton"):
            self._safe_on(w[PROFILE], name, "clicked", self.save_profile)
        for name in ("deleteProfileButton", "deleteAccountButton",
                     "deleteButton"):
            self._safe_on(w[PROFILE], name, "clicked", self.delete_profile)
        for name in ("backButton", "backToMainButton"):
            self._safe_on(w[PROFILE], name, "clicked",
                          lambda: self.go(MAIN))

        w[RECOMMEND].clicked.connect(
            lambda pub_id: self.open_publication(pub_id, RECOMMEND))

        w[PUBLICATION].on("sendButton", "clicked",
                   lambda: self.go(MAIN))

        for name in ("editButton", "editPublicationButton"):
            self._safe_on(w[PUBLICATION], name, "clicked",
                          self.edit_current_publication)
        for name in ("deleteButton", "deletePublicationButton"):
            self._safe_on(w[PUBLICATION], name, "clicked",
                          self.delete_current_publication)
        for name in ("backButton", "backButton2"):
            self._safe_on(w[PUBLICATION], name, "clicked",
                          lambda: self.go(self._pub_origin))

        w[MENTOR].on("searchButton", "clicked", self.refresh_mentoring)
        w[MENTOR].on("themeCombo", "currentIndexChanged",
                     lambda _index: self.refresh_mentoring())

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
            target.move(self.current.pos())
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
        user = self.publicationService.get_user("ivan")
        if not user:
            QMessageBox.warning(
                self.windows[LOGIN], "Ошибка",
                "Не удалось загрузить пользователя из БД.",
            )
            return
        self.user = user
        self.user["interests"] = [self.user.get("specialization") or ""]
        self.page = 1
        self.go(MAIN)
        self._show_first_hint()

    def do_register(self):
        if self.user is not None:
            self.user = None
        self.windows[LOGIN].reset()
        self.go(LOGIN)

    def do_logout(self):
        self.user = None
        self.current_pub = None
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
        for pub in (self.publicationService.get_publications() or []):
            if category != "Все категории" and pub["category"] != category:
                continue
            if keyword and keyword not in pub["title"].lower() \
                    and keyword not in pub["text"].lower():
                continue
            pubs.append(pub)
        total_pages = max(1, -(-len(pubs) // PAGE_SIZE))
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
        pub = next((p for p in (self.publicationService.get_publications() or [])
                    if p["id"] == pub_id), None)
        if pub is None:
            return
        self.current_pub = pub
        self.windows[PUBLICATION].show_publication(pub)

    def open_create_form(self):
        self.form_mode = "create"
        self.current_pub = None
        self.go(FORM)

    def refresh_form(self, pub_id):
        if pub_id is None:
            self.form_mode = "create"
            self.current_pub = None
            self.windows[FORM].mode_create()
            return
        pub = next((p for p in (self.publicationService.get_publications() or [])
                    if p["id"] == pub_id), None)
        if pub is None:
            self.go(MAIN)
            return
        self.form_mode = "edit"
        self.current_pub = pub
        self.windows[FORM].mode_edit(pub)

    def save_form(self):
        if self.form_mode == "edit" and self.current_pub is not None:
            self.go(PUBLICATION, pub_id=self.current_pub["id"])
        else:
            self.go(MAIN)

    def cancel_form(self):
        if self.form_mode == "edit" and self.current_pub is not None:
            self.go(PUBLICATION, pub_id=self.current_pub["id"])
        else:
            self.go(MAIN)

    def refresh_profile(self):
        user = self.user or {}
        my_pubs = [p for p in (self.publicationService.get_publications() or [])
                   if p["author"] == user.get("name")]
        self.windows[PROFILE].show_profile(user, my_pubs[:3])

    def edit_row_publication(self, row):
        pub_id = self.windows[PROFILE].row_pub_id(row)
        if pub_id:
            self._pub_origin = PROFILE
            self.go(FORM, pub_id=pub_id)

    def delete_row_publication(self, row):
        self.refresh_profile()

    def edit_profile(self):
        pass

    def save_profile(self):
        self.refresh_profile()

    def delete_profile(self):
        self.do_logout()

    def edit_current_publication(self):
        if self.current_pub is not None:
            self.go(FORM, pub_id=self.current_pub["id"])

    def delete_current_publication(self):
        self.go(self._pub_origin)

    def refresh_recommendations(self):
        interests = (self.user or {}).get("interests", [])
        scored = []
        for pub in (self.publicationService.get_publications() or []):
            if pub["category"] in interests:
                relevance = 95
            else:
                relevance = min(90, 60 + pub["rating"] * 6)
            scored.append((pub, relevance))
        scored.sort(key=lambda item: item[1], reverse=True)
        self.windows[RECOMMEND].fill(scored[:2])

    def refresh_mentoring(self):
        theme = self.windows[MENTOR].current_theme()
        mentors = self.publicationService.get_mentors(theme) or []
        self.windows[MENTOR].fill(mentors)

    def refresh_rating(self):
        user_id = (self.user or {}).get("id")
        if user_id is None:
            data = {
                "points": 0, "level": "Новичок", "progress": 0,
                "achievements": [], "specialists": [],
            }
        else:
            data = self.publicationService.get_rating_data(user_id)
        self.windows[RATING].show_rating(
            points=data["points"],
            level=data["level"],
            progress=data["progress"],
            achievements=data["achievements"],
            specialists=data["specialists"],
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