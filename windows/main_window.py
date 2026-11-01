from PySide6.QtCore import Qt, Signal

from ui.ui_main_page import Ui_MainScreen
from windows.base import BaseWindow


class MainScreenWindow(BaseWindow):
    ui_class = Ui_MainScreen

    open_recommendations = Signal()
    open_mentoring = Signal()
    open_ratings = Signal()

    def __init__(self):
        super().__init__()
        self._cards = [self.ui.publicationCard1, self.ui.publicationCard2]
        for card in self._cards:
            self.make_clickable(card)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_F7:
            self.open_recommendations.emit()
            event.accept()
            return
        if key == Qt.Key.Key_F8:
            self.open_mentoring.emit()
            event.accept()
            return
        if key == Qt.Key.Key_F9:
            self.open_ratings.emit()
            event.accept()
            return
        super().keyPressEvent(event)

    def set_categories(self, categories):
        if self.ui.categoryCombo.count() == 0:
            self.ui.categoryCombo.addItems(categories)

    def filter_params(self):
        return (
            self.ui.searchEdit.text().strip().lower(),
            self.ui.categoryCombo.currentText(),
        )

    def fill_cards(self, pubs, page, total_pages):
        for index, card in enumerate(self._cards):
            pub = pubs[index] if index < len(pubs) else None
            card.setVisible(pub is not None)
            card.setProperty("clickId", pub["id"] if pub else 0)
            if pub is None:
                continue
            number = index + 1
            short_text = pub["text"][:120].replace("\n", " ")
            if len(pub["text"]) > 120:
                short_text += "…"
            getattr(self.ui, f"card{number}TitleLabel").setText(
                f"Название: {pub['title']}"
            )
            getattr(self.ui, f"card{number}MetaLabel").setText(
                f"Автор: {pub['author']} | Категория: {pub['category']}"
            )
            getattr(self.ui, f"card{number}TextLabel").setText(
                f"Краткий текст: {short_text}"
            )
            getattr(self.ui, f"card{number}StatsLabel").setText(
                f"★ Рейтинг: {pub['rating']} | "
                f"💬 Комментарии: {len(pub['comments'])}"
            )
        self.ui.prevPageButton.setEnabled(page > 1)
        self.ui.nextPageButton.setEnabled(page < total_pages)
        for number in (1, 2, 3):
            button = getattr(self.ui, f"page{number}Button")
            button.setEnabled(number <= total_pages and number != page)
