from ui.ui_mentor import Ui_MentoringScreen
from windows.base import BaseWindow


class MentoringWindow(BaseWindow):
    ui_class = Ui_MentoringScreen
    ROWS = 3

    def __init__(self):
        super().__init__()
        self._mentors = []

    def set_themes(self, themes):
        if self.ui.themeCombo.count() == 0:
            self.ui.themeCombo.addItems(themes)

    def current_theme(self):
        return self.ui.themeCombo.currentText()

    def fill(self, mentors):
        self._mentors = mentors
        for index in range(self.ROWS):
            number = index + 1
            row = getattr(self.ui, f"mentorRow{number}")
            mentor = mentors[index] if index < len(mentors) else None
            row.setVisible(mentor is not None)
            if mentor is None:
                continue
            getattr(self.ui, f"mentor{number}NameLabel").setText(
                mentor["name"]
            )
            getattr(self.ui, f"mentor{number}ThemeLabel").setText(
                mentor["theme"]
            )
            getattr(self.ui, f"mentor{number}ExperienceLabel").setText(
                mentor["experience"]
            )

    def row_mentor(self, row_number):
        index = row_number - 1
        if 0 <= index < len(self._mentors):
            return self._mentors[index]
        return None
