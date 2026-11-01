# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'publications.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_PublicationPageScreen(object):
    def setupUi(self, PublicationPageScreen):
        if not PublicationPageScreen.objectName():
            PublicationPageScreen.setObjectName(u"PublicationPageScreen")
        PublicationPageScreen.resize(820, 640)
        PublicationPageScreen.setMinimumSize(QSize(820, 640))
        self.mainLayout = QVBoxLayout(PublicationPageScreen)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 16, 20, 16)
        self.titleLabel = QLabel(PublicationPageScreen)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.mainLayout.addWidget(self.titleLabel)

        self.metaLabel = QLabel(PublicationPageScreen)
        self.metaLabel.setObjectName(u"metaLabel")

        self.mainLayout.addWidget(self.metaLabel)

        self.publicationText = QPlainTextEdit(PublicationPageScreen)
        self.publicationText.setObjectName(u"publicationText")
        self.publicationText.setReadOnly(True)

        self.mainLayout.addWidget(self.publicationText)

        self.ratingFrame = QFrame(PublicationPageScreen)
        self.ratingFrame.setObjectName(u"ratingFrame")
        self.ratingFrame.setFrameShape(QFrame.Box)
        self.ratingFrame.setFrameShadow(QFrame.Plain)
        self.ratingLayout = QHBoxLayout(self.ratingFrame)
        self.ratingLayout.setSpacing(12)
        self.ratingLayout.setObjectName(u"ratingLayout")
        self.ratingLayout.setContentsMargins(10, 6, 10, 6)
        self.ratingLabel = QLabel(self.ratingFrame)
        self.ratingLabel.setObjectName(u"ratingLabel")

        self.ratingLayout.addWidget(self.ratingLabel)

        self.rating1Button = QRadioButton(self.ratingFrame)
        self.ratingGroup = QButtonGroup(PublicationPageScreen)
        self.ratingGroup.setObjectName(u"ratingGroup")
        self.ratingGroup.addButton(self.rating1Button)
        self.rating1Button.setObjectName(u"rating1Button")

        self.ratingLayout.addWidget(self.rating1Button)

        self.rating2Button = QRadioButton(self.ratingFrame)
        self.ratingGroup.addButton(self.rating2Button)
        self.rating2Button.setObjectName(u"rating2Button")

        self.ratingLayout.addWidget(self.rating2Button)

        self.rating3Button = QRadioButton(self.ratingFrame)
        self.ratingGroup.addButton(self.rating3Button)
        self.rating3Button.setObjectName(u"rating3Button")

        self.ratingLayout.addWidget(self.rating3Button)

        self.rating4Button = QRadioButton(self.ratingFrame)
        self.ratingGroup.addButton(self.rating4Button)
        self.rating4Button.setObjectName(u"rating4Button")

        self.ratingLayout.addWidget(self.rating4Button)

        self.rating5Button = QRadioButton(self.ratingFrame)
        self.ratingGroup.addButton(self.rating5Button)
        self.rating5Button.setObjectName(u"rating5Button")

        self.ratingLayout.addWidget(self.rating5Button)

        self.ratingSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ratingLayout.addItem(self.ratingSpacer)


        self.mainLayout.addWidget(self.ratingFrame)

        self.commentsTitleLabel = QLabel(PublicationPageScreen)
        self.commentsTitleLabel.setObjectName(u"commentsTitleLabel")

        self.mainLayout.addWidget(self.commentsTitleLabel)

        self.commentLabel = QLabel(PublicationPageScreen)
        self.commentLabel.setObjectName(u"commentLabel")
        self.commentLabel.setWordWrap(True)

        self.mainLayout.addWidget(self.commentLabel)

        self.commentInputLayout = QHBoxLayout()
        self.commentInputLayout.setSpacing(8)
        self.commentInputLayout.setObjectName(u"commentInputLayout")
        self.commentEdit = QLineEdit(PublicationPageScreen)
        self.commentEdit.setObjectName(u"commentEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commentEdit.sizePolicy().hasHeightForWidth())
        self.commentEdit.setSizePolicy(sizePolicy)

        self.commentInputLayout.addWidget(self.commentEdit)

        self.sendButton = QPushButton(PublicationPageScreen)
        self.sendButton.setObjectName(u"sendButton")

        self.commentInputLayout.addWidget(self.sendButton)


        self.mainLayout.addLayout(self.commentInputLayout)


        self.retranslateUi(PublicationPageScreen)

        QMetaObject.connectSlotsByName(PublicationPageScreen)
    # setupUi

    def retranslateUi(self, PublicationPageScreen):
        PublicationPageScreen.setWindowTitle(QCoreApplication.translate("PublicationPageScreen", u"4. \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.titleLabel.setText(QCoreApplication.translate("PublicationPageScreen", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.metaLabel.setText(QCoreApplication.translate("PublicationPageScreen", u"\u0410\u0432\u0442\u043e\u0440: [ \u0418\u043c\u044f ] | \u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: [ ... ] | \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: [ ... ]", None))
        self.publicationText.setPlaceholderText(QCoreApplication.translate("PublicationPageScreen", u"[ \u0422\u0435\u043a\u0441\u0442 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438 ]", None))
        self.ratingLabel.setText(QCoreApplication.translate("PublicationPageScreen", u"\u041e\u0446\u0435\u043d\u043a\u0430 \u043f\u043e\u043b\u0435\u0437\u043d\u043e\u0441\u0442\u0438:", None))
        self.rating1Button.setText(QCoreApplication.translate("PublicationPageScreen", u"\u2605 1", None))
        self.rating2Button.setText(QCoreApplication.translate("PublicationPageScreen", u"\u2605 2", None))
        self.rating3Button.setText(QCoreApplication.translate("PublicationPageScreen", u"\u2605 3", None))
        self.rating4Button.setText(QCoreApplication.translate("PublicationPageScreen", u"\u2605 4", None))
        self.rating5Button.setText(QCoreApplication.translate("PublicationPageScreen", u"\u2605 5", None))
        self.commentsTitleLabel.setText(QCoreApplication.translate("PublicationPageScreen", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438:", None))
        self.commentLabel.setText(QCoreApplication.translate("PublicationPageScreen", u"[ \u0410\u0432\u0442\u043e\u0440 ]: \u0442\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f", None))
        self.commentEdit.setPlaceholderText(QCoreApplication.translate("PublicationPageScreen", u"[ \u043f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f ]", None))
        self.sendButton.setText(QCoreApplication.translate("PublicationPageScreen", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

