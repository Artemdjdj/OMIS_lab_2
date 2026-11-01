# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(380, 470)
        LoginScreen.setMinimumSize(QSize(380, 470))
        self.mainLayout = QVBoxLayout(LoginScreen)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 20, 24, 20)
        self.headerFrame = QFrame(LoginScreen)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.Box)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.headerLayout = QVBoxLayout(self.headerFrame)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(8, 10, 8, 10)
        self.headerLabel = QLabel(self.headerFrame)
        self.headerLabel.setObjectName(u"headerLabel")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.headerLayout.addWidget(self.headerLabel)


        self.mainLayout.addWidget(self.headerFrame)

        self.headerSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.headerSpacer)

        self.loginForm = QFormLayout()
        self.loginForm.setObjectName(u"loginForm")
        self.loginForm.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.loginForm.setHorizontalSpacing(8)
        self.loginForm.setVerticalSpacing(12)
        self.loginLabel = QLabel(LoginScreen)
        self.loginLabel.setObjectName(u"loginLabel")

        self.loginForm.setWidget(0, QFormLayout.ItemRole.LabelRole, self.loginLabel)

        self.loginEdit = QLineEdit(LoginScreen)
        self.loginEdit.setObjectName(u"loginEdit")

        self.loginForm.setWidget(0, QFormLayout.ItemRole.FieldRole, self.loginEdit)

        self.passwordLabel = QLabel(LoginScreen)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.loginForm.setWidget(1, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordEdit = QLineEdit(LoginScreen)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.loginForm.setWidget(1, QFormLayout.ItemRole.FieldRole, self.passwordEdit)

        self.loginButton = QPushButton(LoginScreen)
        self.loginButton.setObjectName(u"loginButton")

        self.loginForm.setWidget(2, QFormLayout.ItemRole.FieldRole, self.loginButton)


        self.mainLayout.addLayout(self.loginForm)

        self.pushButton = QPushButton(LoginScreen)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background:None;\n"
"border:None;")

        self.mainLayout.addWidget(self.pushButton)

        self.errorLabel = QLabel(LoginScreen)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)
        self.errorLabel.setWordWrap(True)

        self.mainLayout.addWidget(self.errorLabel)

        self.bottomSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)


        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"1. \u042d\u043a\u0440\u0430\u043d \u0432\u0445\u043e\u0434\u0430", None))
        self.headerLabel.setText(QCoreApplication.translate("LoginScreen", u"\u041f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0430 \u043e\u0431\u043c\u0435\u043d\u0430 \u0437\u043d\u0430\u043d\u0438\u044f\u043c\u0438", None))
        self.loginLabel.setText(QCoreApplication.translate("LoginScreen", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.loginEdit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 ]", None))
        self.passwordLabel.setText(QCoreApplication.translate("LoginScreen", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 ]", None))
        self.loginButton.setText(QCoreApplication.translate("LoginScreen", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("LoginScreen", u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430? \u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.errorLabel.setText(QCoreApplication.translate("LoginScreen", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431 \u043e\u0448\u0438\u0431\u043a\u0435", None))
    # retranslateUi

