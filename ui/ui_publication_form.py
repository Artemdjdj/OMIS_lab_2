# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'publication_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PublicationFormScreen(object):
    def setupUi(self, PublicationFormScreen):
        if not PublicationFormScreen.objectName():
            PublicationFormScreen.setObjectName(u"PublicationFormScreen")
        PublicationFormScreen.resize(620, 520)
        PublicationFormScreen.setMinimumSize(QSize(620, 520))
        self.mainLayout = QVBoxLayout(PublicationFormScreen)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 16, 20, 16)
        self.formLayout = QGridLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(12)
        self.titleLabel = QLabel(PublicationFormScreen)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.titleEdit = QLineEdit(PublicationFormScreen)
        self.titleEdit.setObjectName(u"titleEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)

        self.formLayout.addWidget(self.titleEdit, 0, 1, 1, 1)

        self.categoryLabel = QLabel(PublicationFormScreen)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.formLayout.addWidget(self.categoryLabel, 1, 0, 1, 1)

        self.categoryCombo = QComboBox(PublicationFormScreen)
        self.categoryCombo.setObjectName(u"categoryCombo")
        sizePolicy.setHeightForWidth(self.categoryCombo.sizePolicy().hasHeightForWidth())
        self.categoryCombo.setSizePolicy(sizePolicy)
        self.categoryCombo.setMinimumSize(QSize(180, 0))

        self.formLayout.addWidget(self.categoryCombo, 1, 1, 1, 1)

        self.textLabel = QLabel(PublicationFormScreen)
        self.textLabel.setObjectName(u"textLabel")

        self.formLayout.addWidget(self.textLabel, 2, 0, 1, 1, Qt.AlignTop)

        self.textEdit = QPlainTextEdit(PublicationFormScreen)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.formLayout.addWidget(self.textEdit, 2, 1, 1, 1)


        self.mainLayout.addLayout(self.formLayout)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(8)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonsSpacer)

        self.saveButton = QPushButton(PublicationFormScreen)
        self.saveButton.setObjectName(u"saveButton")

        self.buttonsLayout.addWidget(self.saveButton)

        self.cancelButton = QPushButton(PublicationFormScreen)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonsLayout.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(PublicationFormScreen)

        QMetaObject.connectSlotsByName(PublicationFormScreen)
    # setupUi

    def retranslateUi(self, PublicationFormScreen):
        PublicationFormScreen.setWindowTitle(QCoreApplication.translate("PublicationFormScreen", u"5. \u0424\u043e\u0440\u043c\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f/\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.titleLabel.setText(QCoreApplication.translate("PublicationFormScreen", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("PublicationFormScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 ]", None))
        self.categoryLabel.setText(QCoreApplication.translate("PublicationFormScreen", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.textLabel.setText(QCoreApplication.translate("PublicationFormScreen", u"\u0422\u0435\u043a\u0441\u0442:", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("PublicationFormScreen", u"[ \u043c\u043d\u043e\u0433\u043e\u0441\u0442\u0440\u043e\u0447\u043d\u043e\u0435 \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438 ]", None))
        self.saveButton.setText(QCoreApplication.translate("PublicationFormScreen", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("PublicationFormScreen", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

