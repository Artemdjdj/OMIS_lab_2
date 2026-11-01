# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration_form.ui'
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

class Ui_RegisterScreen(object):
    def setupUi(self, RegisterScreen):
        if not RegisterScreen.objectName():
            RegisterScreen.setObjectName(u"RegisterScreen")
        RegisterScreen.resize(420, 460)
        RegisterScreen.setMinimumSize(QSize(420, 460))
        self.mainLayout = QVBoxLayout(RegisterScreen)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 20, 24, 20)
        self.headerFrame = QFrame(RegisterScreen)
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

        self.registerForm = QFormLayout()
        self.registerForm.setObjectName(u"registerForm")
        self.registerForm.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.registerForm.setHorizontalSpacing(8)
        self.registerForm.setVerticalSpacing(12)
        self.loginLabel = QLabel(RegisterScreen)
        self.loginLabel.setObjectName(u"loginLabel")

        self.registerForm.setWidget(0, QFormLayout.ItemRole.LabelRole, self.loginLabel)

        self.loginEdit = QLineEdit(RegisterScreen)
        self.loginEdit.setObjectName(u"loginEdit")

        self.registerForm.setWidget(0, QFormLayout.ItemRole.FieldRole, self.loginEdit)

        self.emailLabel = QLabel(RegisterScreen)
        self.emailLabel.setObjectName(u"emailLabel")

        self.registerForm.setWidget(1, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailEdit = QLineEdit(RegisterScreen)
        self.emailEdit.setObjectName(u"emailEdit")

        self.registerForm.setWidget(1, QFormLayout.ItemRole.FieldRole, self.emailEdit)

        self.passwordLabel = QLabel(RegisterScreen)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.registerForm.setWidget(2, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordEdit = QLineEdit(RegisterScreen)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.registerForm.setWidget(2, QFormLayout.ItemRole.FieldRole, self.passwordEdit)

        self.passwordRepeatLabel = QLabel(RegisterScreen)
        self.passwordRepeatLabel.setObjectName(u"passwordRepeatLabel")

        self.registerForm.setWidget(3, QFormLayout.ItemRole.LabelRole, self.passwordRepeatLabel)

        self.passwordRepeatEdit = QLineEdit(RegisterScreen)
        self.passwordRepeatEdit.setObjectName(u"passwordRepeatEdit")
        self.passwordRepeatEdit.setEchoMode(QLineEdit.Password)

        self.registerForm.setWidget(3, QFormLayout.ItemRole.FieldRole, self.passwordRepeatEdit)

        self.registerButton = QPushButton(RegisterScreen)
        self.registerButton.setObjectName(u"registerButton")

        self.registerForm.setWidget(4, QFormLayout.ItemRole.FieldRole, self.registerButton)


        self.mainLayout.addLayout(self.registerForm)

        self.pushButton = QPushButton(RegisterScreen)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background:None;\n"
"border:None;")

        self.mainLayout.addWidget(self.pushButton)

        self.bottomSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)


        self.retranslateUi(RegisterScreen)

        QMetaObject.connectSlotsByName(RegisterScreen)
    # setupUi

    def retranslateUi(self, RegisterScreen):
        RegisterScreen.setWindowTitle(QCoreApplication.translate("RegisterScreen", u"2. \u042d\u043a\u0440\u0430\u043d \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.headerLabel.setText(QCoreApplication.translate("RegisterScreen", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0430", None))
        self.loginLabel.setText(QCoreApplication.translate("RegisterScreen", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.loginEdit.setPlaceholderText(QCoreApplication.translate("RegisterScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 ]", None))
        self.emailLabel.setText(QCoreApplication.translate("RegisterScreen", u"E-mail:", None))
        self.emailEdit.setPlaceholderText(QCoreApplication.translate("RegisterScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 ]", None))
        self.passwordLabel.setText(QCoreApplication.translate("RegisterScreen", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("RegisterScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 ]", None))
        self.passwordRepeatLabel.setText(QCoreApplication.translate("RegisterScreen", u"\u041f\u043e\u0432\u0442\u043e\u0440:", None))
        self.passwordRepeatEdit.setPlaceholderText(QCoreApplication.translate("RegisterScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 ]", None))
        self.registerButton.setText(QCoreApplication.translate("RegisterScreen", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("RegisterScreen", u"\u0423\u0436\u0435 \u0435\u0441\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442? \u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

