from ui.ui_login_form import Ui_LoginScreen
from windows.base import BaseWindow


class LoginWindow(BaseWindow):
    ui_class = Ui_LoginScreen

    def __init__(self):
        super().__init__()
        self.ui.errorLabel.setText("")

    def credentials(self):
        return (
            self.ui.loginEdit.text().strip(),
            self.ui.passwordEdit.text(),
        )

    def show_error(self, message):
        self.ui.errorLabel.setText(message)

    def reset(self):
        self.ui.loginEdit.clear()
        self.ui.passwordEdit.clear()
        self.ui.errorLabel.setText("")

    def fill_demo(self):
        self.ui.loginEdit.setText("ivan")
        self.ui.passwordEdit.setText("123456")
