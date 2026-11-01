# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mentor.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MentoringScreen(object):
    def setupUi(self, MentoringScreen):
        if not MentoringScreen.objectName():
            MentoringScreen.setObjectName(u"MentoringScreen")
        MentoringScreen.resize(820, 560)
        MentoringScreen.setMinimumSize(QSize(820, 560))
        self.mainLayout = QVBoxLayout(MentoringScreen)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 16, 20, 16)
        self.titleFrame = QFrame(MentoringScreen)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.Box)
        self.titleFrame.setFrameShadow(QFrame.Plain)
        self.titleLayout = QVBoxLayout(self.titleFrame)
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLayout.setContentsMargins(8, 8, 8, 8)
        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.titleLayout.addWidget(self.titleLabel)


        self.mainLayout.addWidget(self.titleFrame)

        self.filterFrame = QFrame(MentoringScreen)
        self.filterFrame.setObjectName(u"filterFrame")
        self.filterFrame.setFrameShape(QFrame.Box)
        self.filterFrame.setFrameShadow(QFrame.Plain)
        self.filterLayout = QHBoxLayout(self.filterFrame)
        self.filterLayout.setSpacing(8)
        self.filterLayout.setObjectName(u"filterLayout")
        self.filterLayout.setContentsMargins(8, 6, 8, 6)
        self.themeLabel = QLabel(self.filterFrame)
        self.themeLabel.setObjectName(u"themeLabel")

        self.filterLayout.addWidget(self.themeLabel)

        self.themeCombo = QComboBox(self.filterFrame)
        self.themeCombo.setObjectName(u"themeCombo")
        self.themeCombo.setMinimumSize(QSize(180, 0))

        self.filterLayout.addWidget(self.themeCombo)

        self.filterSeparator = QLabel(self.filterFrame)
        self.filterSeparator.setObjectName(u"filterSeparator")

        self.filterLayout.addWidget(self.filterSeparator)

        self.searchButton = QPushButton(self.filterFrame)
        self.searchButton.setObjectName(u"searchButton")

        self.filterLayout.addWidget(self.searchButton)

        self.filterSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filterLayout.addItem(self.filterSpacer)


        self.mainLayout.addWidget(self.filterFrame)

        self.mentorRow1 = QFrame(MentoringScreen)
        self.mentorRow1.setObjectName(u"mentorRow1")
        self.mentorRow1.setFrameShape(QFrame.Box)
        self.mentorRow1.setFrameShadow(QFrame.Plain)
        self.mentor1Layout = QHBoxLayout(self.mentorRow1)
        self.mentor1Layout.setSpacing(8)
        self.mentor1Layout.setObjectName(u"mentor1Layout")
        self.mentor1Layout.setContentsMargins(8, 6, 8, 6)
        self.mentor1TagLabel = QLabel(self.mentorRow1)
        self.mentor1TagLabel.setObjectName(u"mentor1TagLabel")

        self.mentor1Layout.addWidget(self.mentor1TagLabel)

        self.mentor1NameLabel = QLabel(self.mentorRow1)
        self.mentor1NameLabel.setObjectName(u"mentor1NameLabel")

        self.mentor1Layout.addWidget(self.mentor1NameLabel)

        self.mentor1Separator1 = QLabel(self.mentorRow1)
        self.mentor1Separator1.setObjectName(u"mentor1Separator1")

        self.mentor1Layout.addWidget(self.mentor1Separator1)

        self.mentor1ThemeLabel = QLabel(self.mentorRow1)
        self.mentor1ThemeLabel.setObjectName(u"mentor1ThemeLabel")

        self.mentor1Layout.addWidget(self.mentor1ThemeLabel)

        self.mentor1Separator2 = QLabel(self.mentorRow1)
        self.mentor1Separator2.setObjectName(u"mentor1Separator2")

        self.mentor1Layout.addWidget(self.mentor1Separator2)

        self.mentor1ExperienceLabel = QLabel(self.mentorRow1)
        self.mentor1ExperienceLabel.setObjectName(u"mentor1ExperienceLabel")

        self.mentor1Layout.addWidget(self.mentor1ExperienceLabel)

        self.mentor1Separator3 = QLabel(self.mentorRow1)
        self.mentor1Separator3.setObjectName(u"mentor1Separator3")

        self.mentor1Layout.addWidget(self.mentor1Separator3)

        self.mentor1Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mentor1Layout.addItem(self.mentor1Spacer)

        self.mentor1RequestButton = QPushButton(self.mentorRow1)
        self.mentor1RequestButton.setObjectName(u"mentor1RequestButton")

        self.mentor1Layout.addWidget(self.mentor1RequestButton)


        self.mainLayout.addWidget(self.mentorRow1)

        self.mentorRow2 = QFrame(MentoringScreen)
        self.mentorRow2.setObjectName(u"mentorRow2")
        self.mentorRow2.setFrameShape(QFrame.Box)
        self.mentorRow2.setFrameShadow(QFrame.Plain)
        self.mentor2Layout = QHBoxLayout(self.mentorRow2)
        self.mentor2Layout.setSpacing(8)
        self.mentor2Layout.setObjectName(u"mentor2Layout")
        self.mentor2Layout.setContentsMargins(8, 6, 8, 6)
        self.mentor2TagLabel = QLabel(self.mentorRow2)
        self.mentor2TagLabel.setObjectName(u"mentor2TagLabel")

        self.mentor2Layout.addWidget(self.mentor2TagLabel)

        self.mentor2NameLabel = QLabel(self.mentorRow2)
        self.mentor2NameLabel.setObjectName(u"mentor2NameLabel")

        self.mentor2Layout.addWidget(self.mentor2NameLabel)

        self.mentor2Separator1 = QLabel(self.mentorRow2)
        self.mentor2Separator1.setObjectName(u"mentor2Separator1")

        self.mentor2Layout.addWidget(self.mentor2Separator1)

        self.mentor2ThemeLabel = QLabel(self.mentorRow2)
        self.mentor2ThemeLabel.setObjectName(u"mentor2ThemeLabel")

        self.mentor2Layout.addWidget(self.mentor2ThemeLabel)

        self.mentor2Separator2 = QLabel(self.mentorRow2)
        self.mentor2Separator2.setObjectName(u"mentor2Separator2")

        self.mentor2Layout.addWidget(self.mentor2Separator2)

        self.mentor2ExperienceLabel = QLabel(self.mentorRow2)
        self.mentor2ExperienceLabel.setObjectName(u"mentor2ExperienceLabel")

        self.mentor2Layout.addWidget(self.mentor2ExperienceLabel)

        self.mentor2Separator3 = QLabel(self.mentorRow2)
        self.mentor2Separator3.setObjectName(u"mentor2Separator3")

        self.mentor2Layout.addWidget(self.mentor2Separator3)

        self.mentor2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mentor2Layout.addItem(self.mentor2Spacer)

        self.mentor2RequestButton = QPushButton(self.mentorRow2)
        self.mentor2RequestButton.setObjectName(u"mentor2RequestButton")

        self.mentor2Layout.addWidget(self.mentor2RequestButton)


        self.mainLayout.addWidget(self.mentorRow2)

        self.mentorRow3 = QFrame(MentoringScreen)
        self.mentorRow3.setObjectName(u"mentorRow3")
        self.mentorRow3.setFrameShape(QFrame.Box)
        self.mentorRow3.setFrameShadow(QFrame.Plain)
        self.mentor3Layout = QHBoxLayout(self.mentorRow3)
        self.mentor3Layout.setSpacing(8)
        self.mentor3Layout.setObjectName(u"mentor3Layout")
        self.mentor3Layout.setContentsMargins(8, 6, 8, 6)
        self.mentor3TagLabel = QLabel(self.mentorRow3)
        self.mentor3TagLabel.setObjectName(u"mentor3TagLabel")

        self.mentor3Layout.addWidget(self.mentor3TagLabel)

        self.mentor3NameLabel = QLabel(self.mentorRow3)
        self.mentor3NameLabel.setObjectName(u"mentor3NameLabel")

        self.mentor3Layout.addWidget(self.mentor3NameLabel)

        self.mentor3Separator1 = QLabel(self.mentorRow3)
        self.mentor3Separator1.setObjectName(u"mentor3Separator1")

        self.mentor3Layout.addWidget(self.mentor3Separator1)

        self.mentor3ThemeLabel = QLabel(self.mentorRow3)
        self.mentor3ThemeLabel.setObjectName(u"mentor3ThemeLabel")

        self.mentor3Layout.addWidget(self.mentor3ThemeLabel)

        self.mentor3Separator2 = QLabel(self.mentorRow3)
        self.mentor3Separator2.setObjectName(u"mentor3Separator2")

        self.mentor3Layout.addWidget(self.mentor3Separator2)

        self.mentor3ExperienceLabel = QLabel(self.mentorRow3)
        self.mentor3ExperienceLabel.setObjectName(u"mentor3ExperienceLabel")

        self.mentor3Layout.addWidget(self.mentor3ExperienceLabel)

        self.mentor3Separator3 = QLabel(self.mentorRow3)
        self.mentor3Separator3.setObjectName(u"mentor3Separator3")

        self.mentor3Layout.addWidget(self.mentor3Separator3)

        self.mentor3Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mentor3Layout.addItem(self.mentor3Spacer)

        self.mentor3RequestButton = QPushButton(self.mentorRow3)
        self.mentor3RequestButton.setObjectName(u"mentor3RequestButton")

        self.mentor3Layout.addWidget(self.mentor3RequestButton)


        self.mainLayout.addWidget(self.mentorRow3)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)

        self.requestsButtonLayout = QHBoxLayout()
        self.requestsButtonLayout.setObjectName(u"requestsButtonLayout")
        self.requestsLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.requestsButtonLayout.addItem(self.requestsLeftSpacer)

        self.myRequestsButton = QPushButton(MentoringScreen)
        self.myRequestsButton.setObjectName(u"myRequestsButton")

        self.requestsButtonLayout.addWidget(self.myRequestsButton)

        self.requestsRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.requestsButtonLayout.addItem(self.requestsRightSpacer)


        self.mainLayout.addLayout(self.requestsButtonLayout)


        self.retranslateUi(MentoringScreen)

        QMetaObject.connectSlotsByName(MentoringScreen)
    # setupUi

    def retranslateUi(self, MentoringScreen):
        MentoringScreen.setWindowTitle(QCoreApplication.translate("MentoringScreen", u"8. \u042d\u043a\u0440\u0430\u043d \u043d\u0430\u0441\u0442\u0430\u0432\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430 (\u043f\u0435\u0440\u0441\u043f\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439)", None))
        self.titleLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u041d\u0430\u0441\u0442\u0430\u0432\u043d\u0438\u043a\u0438", None))
        self.themeLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u0422\u0435\u043c\u0430:", None))
        self.filterSeparator.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.searchButton.setText(QCoreApplication.translate("MentoringScreen", u"\u043f\u043e\u0438\u0441\u043a", None))
        self.mentor1TagLabel.setText(QCoreApplication.translate("MentoringScreen", u"[ \u041d\u0430\u0441\u0442\u0430\u0432\u043d\u0438\u043a: ]", None))
        self.mentor1NameLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u0418\u043c\u044f", None))
        self.mentor1Separator1.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor1ThemeLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u0422\u0435\u043c\u0430", None))
        self.mentor1Separator2.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor1ExperienceLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u041e\u043f\u044b\u0442", None))
        self.mentor1Separator3.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor1RequestButton.setText(QCoreApplication.translate("MentoringScreen", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443", None))
        self.mentor2TagLabel.setText(QCoreApplication.translate("MentoringScreen", u"[ \u041d\u0430\u0441\u0442\u0430\u0432\u043d\u0438\u043a: ]", None))
        self.mentor2NameLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u0418\u043c\u044f", None))
        self.mentor2Separator1.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor2ThemeLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u0422\u0435\u043c\u0430", None))
        self.mentor2Separator2.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor2ExperienceLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u041e\u043f\u044b\u0442", None))
        self.mentor2Separator3.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor2RequestButton.setText(QCoreApplication.translate("MentoringScreen", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443", None))
        self.mentor3TagLabel.setText(QCoreApplication.translate("MentoringScreen", u"[ \u041d\u0430\u0441\u0442\u0430\u0432\u043d\u0438\u043a: ]", None))
        self.mentor3NameLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u0418\u043c\u044f", None))
        self.mentor3Separator1.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor3ThemeLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u0422\u0435\u043c\u0430", None))
        self.mentor3Separator2.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor3ExperienceLabel.setText(QCoreApplication.translate("MentoringScreen", u"\u041e\u043f\u044b\u0442", None))
        self.mentor3Separator3.setText(QCoreApplication.translate("MentoringScreen", u"|", None))
        self.mentor3RequestButton.setText(QCoreApplication.translate("MentoringScreen", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443", None))
        self.myRequestsButton.setText(QCoreApplication.translate("MentoringScreen", u"\u041c\u043e\u0438 \u0437\u0430\u044f\u0432\u043a\u0438", None))
    # retranslateUi

