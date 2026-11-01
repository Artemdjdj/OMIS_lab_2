from ui.ui_publications import Ui_PublicationPageScreen
from windows.base import BaseWindow


class PublicationWindow(BaseWindow):
    ui_class = Ui_PublicationPageScreen

    def comment_text(self):
        return self.ui.commentEdit.text().strip()

    def clear_comment_input(self):
        self.ui.commentEdit.clear()

    def show_publication(self, pub):
        self.ui.titleLabel.setText(pub["title"])
        self.ui.metaLabel.setText(
            f"Автор: {pub['author']} | "
            f"Специализация: {pub.get('author_spec', '-')} | "
            f"Категория: {pub['category']}"
        )
        self.ui.publicationText.setPlainText(pub["text"])
        if pub["comments"]:
            self.ui.commentLabel.setText("\n".join(
                f"{comment['author']}: {comment['text']}"
                for comment in pub["comments"]
            ))
        else:
            self.ui.commentLabel.setText("Комментариев пока нет.")
        for number in range(1, 6):
            getattr(self.ui, f"rating{number}Button").setChecked(
                pub["rating"] == number
            )
