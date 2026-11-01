from ui.ui_publication_form import Ui_PublicationFormScreen
from windows.base import BaseWindow


class PublicationFormWindow(BaseWindow):
    ui_class = Ui_PublicationFormScreen

    def set_categories(self, categories):
        if self.ui.categoryCombo.count() == 0:
            self.ui.categoryCombo.addItems(categories)

    def mode_create(self):
        self.ui.titleEdit.clear()
        self.ui.textEdit.clear()
        if self.ui.categoryCombo.count() > 0:
            self.ui.categoryCombo.setCurrentIndex(0)

    def mode_edit(self, pub):
        self.ui.titleEdit.setText(pub["title"])
        self.ui.textEdit.setPlainText(pub["text"])
        index = self.ui.categoryCombo.findText(pub["category"])
        if index >= 0:
            self.ui.categoryCombo.setCurrentIndex(index)

    def values(self):
        return (
            self.ui.titleEdit.text().strip(),
            self.ui.categoryCombo.currentText(),
            self.ui.textEdit.toPlainText().strip(),
        )
