# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.resize(900, 620)
        MainScreen.setMinimumSize(QSize(900, 620))
        self.mainLayout = QVBoxLayout(MainScreen)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(16, 14, 16, 14)
        self.headerFrame = QFrame(MainScreen)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.Box)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.headerLayout = QVBoxLayout(self.headerFrame)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(8, 10, 8, 10)
        self.headerLabel = QLabel(self.headerFrame)
        self.headerLabel.setObjectName(u"headerLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.headerLayout.addWidget(self.headerLabel)


        self.mainLayout.addWidget(self.headerFrame)

        self.filterLayout = QHBoxLayout()
        self.filterLayout.setSpacing(8)
        self.filterLayout.setObjectName(u"filterLayout")
        self.searchEdit = QLineEdit(MainScreen)
        self.searchEdit.setObjectName(u"searchEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)

        self.filterLayout.addWidget(self.searchEdit)

        self.categoryLabel = QLabel(MainScreen)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.filterLayout.addWidget(self.categoryLabel)

        self.categoryCombo = QComboBox(MainScreen)
        self.categoryCombo.setObjectName(u"categoryCombo")
        self.categoryCombo.setMinimumSize(QSize(150, 0))

        self.filterLayout.addWidget(self.categoryCombo)


        self.mainLayout.addLayout(self.filterLayout)

        self.actionsLayout = QHBoxLayout()
        self.actionsLayout.setSpacing(8)
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.createPublicationButton = QPushButton(MainScreen)
        self.createPublicationButton.setObjectName(u"createPublicationButton")

        self.actionsLayout.addWidget(self.createPublicationButton)

        self.profileButton = QPushButton(MainScreen)
        self.profileButton.setObjectName(u"profileButton")

        self.actionsLayout.addWidget(self.profileButton)

        self.logoutButton = QPushButton(MainScreen)
        self.logoutButton.setObjectName(u"logoutButton")

        self.actionsLayout.addWidget(self.logoutButton)


        self.mainLayout.addLayout(self.actionsLayout)

        self.publicationsContainer = QWidget(MainScreen)
        self.publicationsContainer.setObjectName(u"publicationsContainer")
        self.publicationsLayout = QVBoxLayout(self.publicationsContainer)
        self.publicationsLayout.setSpacing(10)
        self.publicationsLayout.setObjectName(u"publicationsLayout")
        self.publicationsLayout.setContentsMargins(0, 0, 0, 0)
        self.publicationCard1 = QFrame(self.publicationsContainer)
        self.publicationCard1.setObjectName(u"publicationCard1")
        self.publicationCard1.setFrameShape(QFrame.Box)
        self.publicationCard1.setFrameShadow(QFrame.Plain)
        self.card1Layout = QVBoxLayout(self.publicationCard1)
        self.card1Layout.setSpacing(6)
        self.card1Layout.setObjectName(u"card1Layout")
        self.card1Layout.setContentsMargins(10, 8, 10, 8)
        self.card1HeaderLabel = QLabel(self.publicationCard1)
        self.card1HeaderLabel.setObjectName(u"card1HeaderLabel")

        self.card1Layout.addWidget(self.card1HeaderLabel)

        self.card1TitleLabel = QLabel(self.publicationCard1)
        self.card1TitleLabel.setObjectName(u"card1TitleLabel")

        self.card1Layout.addWidget(self.card1TitleLabel)

        self.card1MetaLabel = QLabel(self.publicationCard1)
        self.card1MetaLabel.setObjectName(u"card1MetaLabel")

        self.card1Layout.addWidget(self.card1MetaLabel)

        self.card1TextLabel = QLabel(self.publicationCard1)
        self.card1TextLabel.setObjectName(u"card1TextLabel")
        self.card1TextLabel.setWordWrap(True)

        self.card1Layout.addWidget(self.card1TextLabel)

        self.card1StatsLabel = QLabel(self.publicationCard1)
        self.card1StatsLabel.setObjectName(u"card1StatsLabel")

        self.card1Layout.addWidget(self.card1StatsLabel)


        self.publicationsLayout.addWidget(self.publicationCard1)

        self.publicationCard2 = QFrame(self.publicationsContainer)
        self.publicationCard2.setObjectName(u"publicationCard2")
        self.publicationCard2.setFrameShape(QFrame.Box)
        self.publicationCard2.setFrameShadow(QFrame.Plain)
        self.card2Layout = QVBoxLayout(self.publicationCard2)
        self.card2Layout.setSpacing(6)
        self.card2Layout.setObjectName(u"card2Layout")
        self.card2Layout.setContentsMargins(10, 8, 10, 8)
        self.card2HeaderLabel = QLabel(self.publicationCard2)
        self.card2HeaderLabel.setObjectName(u"card2HeaderLabel")

        self.card2Layout.addWidget(self.card2HeaderLabel)

        self.card2TitleLabel = QLabel(self.publicationCard2)
        self.card2TitleLabel.setObjectName(u"card2TitleLabel")

        self.card2Layout.addWidget(self.card2TitleLabel)

        self.card2MetaLabel = QLabel(self.publicationCard2)
        self.card2MetaLabel.setObjectName(u"card2MetaLabel")

        self.card2Layout.addWidget(self.card2MetaLabel)

        self.card2TextLabel = QLabel(self.publicationCard2)
        self.card2TextLabel.setObjectName(u"card2TextLabel")
        self.card2TextLabel.setWordWrap(True)

        self.card2Layout.addWidget(self.card2TextLabel)

        self.card2StatsLabel = QLabel(self.publicationCard2)
        self.card2StatsLabel.setObjectName(u"card2StatsLabel")

        self.card2Layout.addWidget(self.card2StatsLabel)


        self.publicationsLayout.addWidget(self.publicationCard2)

        self.cardsBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.publicationsLayout.addItem(self.cardsBottomSpacer)


        self.mainLayout.addWidget(self.publicationsContainer)

        self.paginationLayout = QHBoxLayout()
        self.paginationLayout.setSpacing(6)
        self.paginationLayout.setObjectName(u"paginationLayout")
        self.paginationLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.paginationLayout.addItem(self.paginationLeftSpacer)

        self.prevPageButton = QPushButton(MainScreen)
        self.prevPageButton.setObjectName(u"prevPageButton")
        self.prevPageButton.setMaximumSize(QSize(36, 16777215))

        self.paginationLayout.addWidget(self.prevPageButton)

        self.page1Button = QPushButton(MainScreen)
        self.page1Button.setObjectName(u"page1Button")
        self.page1Button.setMaximumSize(QSize(36, 16777215))

        self.paginationLayout.addWidget(self.page1Button)

        self.page2Button = QPushButton(MainScreen)
        self.page2Button.setObjectName(u"page2Button")
        self.page2Button.setMaximumSize(QSize(36, 16777215))

        self.paginationLayout.addWidget(self.page2Button)

        self.page3Button = QPushButton(MainScreen)
        self.page3Button.setObjectName(u"page3Button")
        self.page3Button.setMaximumSize(QSize(36, 16777215))

        self.paginationLayout.addWidget(self.page3Button)

        self.paginationEllipsisLabel = QLabel(MainScreen)
        self.paginationEllipsisLabel.setObjectName(u"paginationEllipsisLabel")
        self.paginationEllipsisLabel.setAlignment(Qt.AlignCenter)

        self.paginationLayout.addWidget(self.paginationEllipsisLabel)

        self.nextPageButton = QPushButton(MainScreen)
        self.nextPageButton.setObjectName(u"nextPageButton")
        self.nextPageButton.setMaximumSize(QSize(36, 16777215))

        self.paginationLayout.addWidget(self.nextPageButton)

        self.paginationRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.paginationLayout.addItem(self.paginationRightSpacer)


        self.mainLayout.addLayout(self.paginationLayout)


        self.retranslateUi(MainScreen)

        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"3. \u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 (\u043b\u0435\u043d\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0439)", None))
        self.headerLabel.setText(QCoreApplication.translate("MainScreen", u"\u041f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0430 \u043e\u0431\u043c\u0435\u043d\u0430 \u0437\u043d\u0430\u043d\u0438\u044f\u043c\u0438", None))
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainScreen", u"[ \u043f\u043e\u0438\u0441\u043a \u043f\u043e \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u043c \u0441\u043b\u043e\u0432\u0430\u043c ]", None))
        self.categoryLabel.setText(QCoreApplication.translate("MainScreen", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.createPublicationButton.setText(QCoreApplication.translate("MainScreen", u"+ \u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044e", None))
        self.profileButton.setText(QCoreApplication.translate("MainScreen", u"\u041c\u043e\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.logoutButton.setText(QCoreApplication.translate("MainScreen", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.card1HeaderLabel.setText(QCoreApplication.translate("MainScreen", u"[ \u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438 ]", None))
        self.card1TitleLabel.setText(QCoreApplication.translate("MainScreen", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ...", None))
        self.card1MetaLabel.setText(QCoreApplication.translate("MainScreen", u"\u0410\u0432\u0442\u043e\u0440: ... | \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: ...", None))
        self.card1TextLabel.setText(QCoreApplication.translate("MainScreen", u"\u041a\u0440\u0430\u0442\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442: ...", None))
        self.card1StatsLabel.setText(QCoreApplication.translate("MainScreen", u"\u2605 \u0420\u0435\u0439\u0442\u0438\u043d\u0433: ... | \ud83d\udcac \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438: ...", None))
        self.card2HeaderLabel.setText(QCoreApplication.translate("MainScreen", u"[ \u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438 ]", None))
        self.card2TitleLabel.setText(QCoreApplication.translate("MainScreen", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ...", None))
        self.card2MetaLabel.setText(QCoreApplication.translate("MainScreen", u"\u0410\u0432\u0442\u043e\u0440: ... | \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: ...", None))
        self.card2TextLabel.setText(QCoreApplication.translate("MainScreen", u"\u041a\u0440\u0430\u0442\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442: ...", None))
        self.card2StatsLabel.setText(QCoreApplication.translate("MainScreen", u"\u2605 \u0420\u0435\u0439\u0442\u0438\u043d\u0433: ... | \ud83d\udcac \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438: ...", None))
        self.prevPageButton.setText(QCoreApplication.translate("MainScreen", u"<", None))
        self.page1Button.setText(QCoreApplication.translate("MainScreen", u"1", None))
        self.page2Button.setText(QCoreApplication.translate("MainScreen", u"2", None))
        self.page3Button.setText(QCoreApplication.translate("MainScreen", u"3", None))
        self.paginationEllipsisLabel.setText(QCoreApplication.translate("MainScreen", u"...", None))
        self.nextPageButton.setText(QCoreApplication.translate("MainScreen", u">", None))
    # retranslateUi

