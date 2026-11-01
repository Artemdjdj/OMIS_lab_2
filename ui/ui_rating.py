# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rating.ui'
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
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_RatingScreen(object):
    def setupUi(self, RatingScreen):
        if not RatingScreen.objectName():
            RatingScreen.setObjectName(u"RatingScreen")
        RatingScreen.resize(720, 660)
        RatingScreen.setMinimumSize(QSize(720, 660))
        self.mainLayout = QVBoxLayout(RatingScreen)
        self.mainLayout.setSpacing(8)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 16, 20, 16)
        self.myRatingTitleLabel = QLabel(RatingScreen)
        self.myRatingTitleLabel.setObjectName(u"myRatingTitleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.myRatingTitleLabel.setFont(font)
        self.myRatingTitleLabel.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.myRatingTitleLabel)

        self.pointsLayout = QHBoxLayout()
        self.pointsLayout.setSpacing(8)
        self.pointsLayout.setObjectName(u"pointsLayout")
        self.pointsLabel = QLabel(RatingScreen)
        self.pointsLabel.setObjectName(u"pointsLabel")

        self.pointsLayout.addWidget(self.pointsLabel)

        self.pointsValueLabel = QLabel(RatingScreen)
        self.pointsValueLabel.setObjectName(u"pointsValueLabel")

        self.pointsLayout.addWidget(self.pointsValueLabel)

        self.pointsSeparator = QLabel(RatingScreen)
        self.pointsSeparator.setObjectName(u"pointsSeparator")

        self.pointsLayout.addWidget(self.pointsSeparator)

        self.levelLabel = QLabel(RatingScreen)
        self.levelLabel.setObjectName(u"levelLabel")

        self.pointsLayout.addWidget(self.levelLabel)

        self.levelValueLabel = QLabel(RatingScreen)
        self.levelValueLabel.setObjectName(u"levelValueLabel")

        self.pointsLayout.addWidget(self.levelValueLabel)

        self.pointsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.pointsLayout.addItem(self.pointsSpacer)


        self.mainLayout.addLayout(self.pointsLayout)

        self.levelProgressBar = QProgressBar(RatingScreen)
        self.levelProgressBar.setObjectName(u"levelProgressBar")
        self.levelProgressBar.setValue(0)
        self.levelProgressBar.setTextVisible(True)

        self.mainLayout.addWidget(self.levelProgressBar)

        self.sectionSeparator1 = QFrame(RatingScreen)
        self.sectionSeparator1.setObjectName(u"sectionSeparator1")
        self.sectionSeparator1.setFrameShape(QFrame.HLine)
        self.sectionSeparator1.setFrameShadow(QFrame.Plain)

        self.mainLayout.addWidget(self.sectionSeparator1)

        self.achievementsTitleLabel = QLabel(RatingScreen)
        self.achievementsTitleLabel.setObjectName(u"achievementsTitleLabel")

        self.mainLayout.addWidget(self.achievementsTitleLabel)

        self.achievementsSeparator1 = QFrame(RatingScreen)
        self.achievementsSeparator1.setObjectName(u"achievementsSeparator1")
        self.achievementsSeparator1.setFrameShape(QFrame.HLine)
        self.achievementsSeparator1.setFrameShadow(QFrame.Plain)

        self.mainLayout.addWidget(self.achievementsSeparator1)

        self.achievement1Label = QLabel(RatingScreen)
        self.achievement1Label.setObjectName(u"achievement1Label")
        self.achievement1Label.setMinimumSize(QSize(0, 36))
        self.achievement1Label.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.achievement1Label)

        self.achievementsSeparator2 = QFrame(RatingScreen)
        self.achievementsSeparator2.setObjectName(u"achievementsSeparator2")
        self.achievementsSeparator2.setFrameShape(QFrame.HLine)
        self.achievementsSeparator2.setFrameShadow(QFrame.Plain)

        self.mainLayout.addWidget(self.achievementsSeparator2)

        self.achievement2Label = QLabel(RatingScreen)
        self.achievement2Label.setObjectName(u"achievement2Label")
        self.achievement2Label.setMinimumSize(QSize(0, 36))
        self.achievement2Label.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.achievement2Label)

        self.achievementsSeparator3 = QFrame(RatingScreen)
        self.achievementsSeparator3.setObjectName(u"achievementsSeparator3")
        self.achievementsSeparator3.setFrameShape(QFrame.HLine)
        self.achievementsSeparator3.setFrameShadow(QFrame.Plain)

        self.mainLayout.addWidget(self.achievementsSeparator3)

        self.achievement3Label = QLabel(RatingScreen)
        self.achievement3Label.setObjectName(u"achievement3Label")
        self.achievement3Label.setMinimumSize(QSize(0, 36))
        self.achievement3Label.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.achievement3Label)

        self.sectionSeparator2 = QFrame(RatingScreen)
        self.sectionSeparator2.setObjectName(u"sectionSeparator2")
        self.sectionSeparator2.setFrameShape(QFrame.HLine)
        self.sectionSeparator2.setFrameShadow(QFrame.Plain)

        self.mainLayout.addWidget(self.sectionSeparator2)

        self.specialistsTitleLabel = QLabel(RatingScreen)
        self.specialistsTitleLabel.setObjectName(u"specialistsTitleLabel")

        self.mainLayout.addWidget(self.specialistsTitleLabel)

        self.specialist1Label = QLabel(RatingScreen)
        self.specialist1Label.setObjectName(u"specialist1Label")

        self.mainLayout.addWidget(self.specialist1Label)

        self.specialist2Label = QLabel(RatingScreen)
        self.specialist2Label.setObjectName(u"specialist2Label")

        self.mainLayout.addWidget(self.specialist2Label)

        self.specialist3Label = QLabel(RatingScreen)
        self.specialist3Label.setObjectName(u"specialist3Label")

        self.mainLayout.addWidget(self.specialist3Label)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)


        self.retranslateUi(RatingScreen)

        QMetaObject.connectSlotsByName(RatingScreen)
    # setupUi

    def retranslateUi(self, RatingScreen):
        RatingScreen.setWindowTitle(QCoreApplication.translate("RatingScreen", u"9. \u042d\u043a\u0440\u0430\u043d \u0440\u0435\u0439\u0442\u0438\u043d\u0433\u0430 \u0438 \u0434\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u0439 (\u043f\u0435\u0440\u0441\u043f\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439)", None))
        self.myRatingTitleLabel.setText(QCoreApplication.translate("RatingScreen", u"\u041c\u043e\u0439 \u0440\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.pointsLabel.setText(QCoreApplication.translate("RatingScreen", u"\u0411\u0430\u043b\u043b\u044b:", None))
        self.pointsValueLabel.setText(QCoreApplication.translate("RatingScreen", u"[ ... ]", None))
        self.pointsSeparator.setText(QCoreApplication.translate("RatingScreen", u"|", None))
        self.levelLabel.setText(QCoreApplication.translate("RatingScreen", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c:", None))
        self.levelValueLabel.setText(QCoreApplication.translate("RatingScreen", u"[ ... ]", None))
        self.levelProgressBar.setFormat(QCoreApplication.translate("RatingScreen", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441-\u0431\u0430\u0440 \u0434\u043e \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f", None))
        self.achievementsTitleLabel.setText(QCoreApplication.translate("RatingScreen", u"\u0414\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u044f:", None))
        self.achievement1Label.setText(QCoreApplication.translate("RatingScreen", u"[ \u0414\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u0435 1 ]", None))
        self.achievement2Label.setText(QCoreApplication.translate("RatingScreen", u"[ \u0414\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u0435 2 ]", None))
        self.achievement3Label.setText(QCoreApplication.translate("RatingScreen", u"[ \u0414\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u0435 3 ]", None))
        self.specialistsTitleLabel.setText(QCoreApplication.translate("RatingScreen", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432:", None))
        self.specialist1Label.setText(QCoreApplication.translate("RatingScreen", u"1. [\u0418\u043c\u044f] \u2014 ... \u0431\u0430\u043b\u043b\u043e\u0432", None))
        self.specialist2Label.setText(QCoreApplication.translate("RatingScreen", u"2. [\u0418\u043c\u044f] \u2014 ... \u0431\u0430\u043b\u043b\u043e\u0432", None))
        self.specialist3Label.setText(QCoreApplication.translate("RatingScreen", u"3. [\u0418\u043c\u044f] \u2014 ... \u0431\u0430\u043b\u043b\u043e\u0432", None))
    # retranslateUi

