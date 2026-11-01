# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recommendation.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_RecommendationsScreen(object):
    def setupUi(self, RecommendationsScreen):
        if not RecommendationsScreen.objectName():
            RecommendationsScreen.setObjectName(u"RecommendationsScreen")
        RecommendationsScreen.resize(720, 560)
        RecommendationsScreen.setMinimumSize(QSize(720, 560))
        self.mainLayout = QVBoxLayout(RecommendationsScreen)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 16, 20, 16)
        self.headerFrame = QFrame(RecommendationsScreen)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.Box)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.headerLayout = QVBoxLayout(self.headerFrame)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(8, 10, 8, 10)
        self.titleLabel = QLabel(self.headerFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.headerLayout.addWidget(self.titleLabel)


        self.mainLayout.addWidget(self.headerFrame)

        self.subtitleLabel = QLabel(RecommendationsScreen)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        font1 = QFont()
        font1.setItalic(True)
        self.subtitleLabel.setFont(font1)
        self.subtitleLabel.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.subtitleLabel)

        self.recommendationCard1 = QFrame(RecommendationsScreen)
        self.recommendationCard1.setObjectName(u"recommendationCard1")
        self.recommendationCard1.setFrameShape(QFrame.Box)
        self.recommendationCard1.setFrameShadow(QFrame.Plain)
        self.card1Layout = QVBoxLayout(self.recommendationCard1)
        self.card1Layout.setSpacing(6)
        self.card1Layout.setObjectName(u"card1Layout")
        self.card1Layout.setContentsMargins(10, 8, 10, 8)
        self.card1HeaderLabel = QLabel(self.recommendationCard1)
        self.card1HeaderLabel.setObjectName(u"card1HeaderLabel")

        self.card1Layout.addWidget(self.card1HeaderLabel)

        self.card1TitleLabel = QLabel(self.recommendationCard1)
        self.card1TitleLabel.setObjectName(u"card1TitleLabel")

        self.card1Layout.addWidget(self.card1TitleLabel)

        self.card1MetaLabel = QLabel(self.recommendationCard1)
        self.card1MetaLabel.setObjectName(u"card1MetaLabel")

        self.card1Layout.addWidget(self.card1MetaLabel)

        self.card1RelevanceLabel = QLabel(self.recommendationCard1)
        self.card1RelevanceLabel.setObjectName(u"card1RelevanceLabel")

        self.card1Layout.addWidget(self.card1RelevanceLabel)


        self.mainLayout.addWidget(self.recommendationCard1)

        self.recommendationCard2 = QFrame(RecommendationsScreen)
        self.recommendationCard2.setObjectName(u"recommendationCard2")
        self.recommendationCard2.setFrameShape(QFrame.Box)
        self.recommendationCard2.setFrameShadow(QFrame.Plain)
        self.card2Layout = QVBoxLayout(self.recommendationCard2)
        self.card2Layout.setSpacing(6)
        self.card2Layout.setObjectName(u"card2Layout")
        self.card2Layout.setContentsMargins(10, 8, 10, 8)
        self.card2HeaderLabel = QLabel(self.recommendationCard2)
        self.card2HeaderLabel.setObjectName(u"card2HeaderLabel")

        self.card2Layout.addWidget(self.card2HeaderLabel)

        self.card2TitleLabel = QLabel(self.recommendationCard2)
        self.card2TitleLabel.setObjectName(u"card2TitleLabel")

        self.card2Layout.addWidget(self.card2TitleLabel)

        self.card2MetaLabel = QLabel(self.recommendationCard2)
        self.card2MetaLabel.setObjectName(u"card2MetaLabel")

        self.card2Layout.addWidget(self.card2MetaLabel)

        self.card2RelevanceLabel = QLabel(self.recommendationCard2)
        self.card2RelevanceLabel.setObjectName(u"card2RelevanceLabel")

        self.card2Layout.addWidget(self.card2RelevanceLabel)


        self.mainLayout.addWidget(self.recommendationCard2)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)

        self.interestsButtonLayout = QHBoxLayout()
        self.interestsButtonLayout.setObjectName(u"interestsButtonLayout")
        self.interestsLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.interestsButtonLayout.addItem(self.interestsLeftSpacer)

        self.configureInterestsButton = QPushButton(RecommendationsScreen)
        self.configureInterestsButton.setObjectName(u"configureInterestsButton")

        self.interestsButtonLayout.addWidget(self.configureInterestsButton)

        self.interestsRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.interestsButtonLayout.addItem(self.interestsRightSpacer)


        self.mainLayout.addLayout(self.interestsButtonLayout)


        self.retranslateUi(RecommendationsScreen)

        QMetaObject.connectSlotsByName(RecommendationsScreen)
    # setupUi

    def retranslateUi(self, RecommendationsScreen):
        RecommendationsScreen.setWindowTitle(QCoreApplication.translate("RecommendationsScreen", u"7. \u042d\u043a\u0440\u0430\u043d \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0439 (\u043f\u0435\u0440\u0441\u043f\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439)", None))
        self.titleLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438 \u0434\u043b\u044f \u0432\u0430\u0441", None))
        self.subtitleLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u041d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u0432\u0430\u0448\u0438\u0445 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043e\u0432 \u0438 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432", None))
        self.card1HeaderLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"[ \u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f ]", None))
        self.card1TitleLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ...", None))
        self.card1MetaLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u0410\u0432\u0442\u043e\u0440: ... | \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: ...", None))
        self.card1RelevanceLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u0420\u0435\u043b\u0435\u0432\u0430\u043d\u0442\u043d\u043e\u0441\u0442\u044c: ...%", None))
        self.card2HeaderLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"[ \u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f ]", None))
        self.card2TitleLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ...", None))
        self.card2MetaLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u0410\u0432\u0442\u043e\u0440: ... | \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: ...", None))
        self.card2RelevanceLabel.setText(QCoreApplication.translate("RecommendationsScreen", u"\u0420\u0435\u043b\u0435\u0432\u0430\u043d\u0442\u043d\u043e\u0441\u0442\u044c: ...%", None))
        self.configureInterestsButton.setText(QCoreApplication.translate("RecommendationsScreen", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u044b", None))
    # retranslateUi

