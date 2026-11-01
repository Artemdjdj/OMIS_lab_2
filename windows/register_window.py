from ui.ui_registration_form import Ui_RegisterScreen
from windows.base import BaseWindow


class RegisterWindow(BaseWindow):
    ui_class = Ui_RegisterScreen

    def data(self):
        return {
            "login": self.ui.loginEdit.text().strip(),
            "email": self.ui.emailEdit.text().strip(),
            "password": self.ui.passwordEdit.text(),
            "password2": self.ui.passwordRepeatEdit.text(),
        }

    def reset(self):
        self.ui.loginEdit.clear()
        self.ui.emailEdit.clear()
        self.ui.passwordEdit.clear()
        self.ui.passwordRepeatEdit.clear()

    def fill_demo(self):
        self.ui.loginEdit.setText("petr")
        self.ui.emailEdit.setText("petr@example.com")
        self.ui.passwordEdit.setText("123456")
        self.ui.passwordRepeatEdit.setText("123456")
