from ui.ui_rating import Ui_RatingScreen
from windows.base import BaseWindow


class RatingWindow(BaseWindow):
    ui_class = Ui_RatingScreen

    def show_rating(self, points, level, progress, achievements, specialists):
        self.ui.pointsValueLabel.setText(str(points))
        self.ui.levelValueLabel.setText(level)
        self.ui.levelProgressBar.setValue(progress)
        for number in (1, 2, 3):
            label = getattr(self.ui, f"achievement{number}Label")
            if number <= len(achievements):
                label.setText(achievements[number - 1])
            specialist = getattr(self.ui, f"specialist{number}Label")
            if number <= len(specialists):
                specialist.setText(specialists[number - 1])
