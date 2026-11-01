from ui.ui_profile import Ui_ProfileScreen
from windows.base import BaseWindow


class ProfileWindow(BaseWindow):
    ui_class = Ui_ProfileScreen
    ROWS = 3

    def __init__(self):
        super().__init__()
        self._rows = [
            getattr(self.ui, f"publicationRow{number}")
            for number in range(1, self.ROWS + 1)
        ]
        for row in self._rows:
            self.make_clickable(row)

    def show_profile(self, user, my_publications):
        self.ui.nameValueLabel.setText(user.get("name", "—"))
        self.ui.specializationValueLabel.setText(
            user.get("specialization", "—")
        )
        self.ui.experienceValueLabel.setText(user.get("experience", "—"))
        self.ui.aboutValueLabel.setText(user.get("about", "—"))
        for index, row in enumerate(self._rows):
            pub = (
                my_publications[index]
                if index < len(my_publications) else None
            )
            row.setVisible(pub is not None)
            row.setProperty("clickId", pub["id"] if pub else 0)
            if pub is None:
                continue
            number = index + 1
            getattr(self.ui, f"row{number}TitleLabel").setText(pub["title"])
            getattr(self.ui, f"row{number}CategoryLabel").setText(
                pub["category"]
            )
            getattr(self.ui, f"row{number}RatingLabel").setText(
                f"★ {pub['rating']}"
            )

    def row_pub_id(self, row_number):
        click_id = self._rows[row_number - 1].property("clickId")
        return click_id if click_id else None
