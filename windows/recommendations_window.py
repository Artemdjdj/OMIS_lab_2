from ui.ui_recommendation import Ui_RecommendationsScreen
from windows.base import BaseWindow


class RecommendationsWindow(BaseWindow):
    ui_class = Ui_RecommendationsScreen

    def __init__(self):
        super().__init__()
        self._cards = [
            self.ui.recommendationCard1,
            self.ui.recommendationCard2,
        ]
        for card in self._cards:
            self.make_clickable(card)

    def fill(self, recommendations):
        for index, card in enumerate(self._cards):
            item = (
                recommendations[index]
                if index < len(recommendations) else None
            )
            card.setVisible(item is not None)
            card.setProperty("clickId", item[0]["id"] if item else 0)
            if item is None:
                continue
            pub, relevance = item
            number = index + 1
            getattr(self.ui, f"card{number}TitleLabel").setText(
                f"Название: {pub['title']}"
            )
            getattr(self.ui, f"card{number}MetaLabel").setText(
                f"Автор: {pub['author']} | Категория: {pub['category']}"
            )
            getattr(self.ui, f"card{number}RelevanceLabel").setText(
                f"Релевантность: {relevance}%"
            )
