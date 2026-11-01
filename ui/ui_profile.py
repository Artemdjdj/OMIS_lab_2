# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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

class Ui_ProfileScreen(object):
    def setupUi(self, ProfileScreen):
        if not ProfileScreen.objectName():
            ProfileScreen.setObjectName(u"ProfileScreen")
        ProfileScreen.resize(680, 640)
        ProfileScreen.setMinimumSize(QSize(680, 640))
        self.mainLayout = QVBoxLayout(ProfileScreen)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 16, 20, 16)
        self.profileLayout = QHBoxLayout()
        self.profileLayout.setSpacing(16)
        self.profileLayout.setObjectName(u"profileLayout")
        self.photoLabel = QLabel(ProfileScreen)
        self.photoLabel.setObjectName(u"photoLabel")
        self.photoLabel.setMinimumSize(QSize(130, 150))
        self.photoLabel.setFrameShape(QFrame.Box)
        self.photoLabel.setFrameShadow(QFrame.Plain)
        self.photoLabel.setAlignment(Qt.AlignCenter)

        self.profileLayout.addWidget(self.photoLabel)

        self.infoLayout = QVBoxLayout()
        self.infoLayout.setSpacing(10)
        self.infoLayout.setObjectName(u"infoLayout")
        self.nameRowLayout = QHBoxLayout()
        self.nameRowLayout.setSpacing(8)
        self.nameRowLayout.setObjectName(u"nameRowLayout")
        self.nameLabel = QLabel(ProfileScreen)
        self.nameLabel.setObjectName(u"nameLabel")

        self.nameRowLayout.addWidget(self.nameLabel)

        self.nameValueLabel = QLabel(ProfileScreen)
        self.nameValueLabel.setObjectName(u"nameValueLabel")

        self.nameRowLayout.addWidget(self.nameValueLabel)

        self.nameRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.nameRowLayout.addItem(self.nameRowSpacer)


        self.infoLayout.addLayout(self.nameRowLayout)

        self.specializationRowLayout = QHBoxLayout()
        self.specializationRowLayout.setSpacing(8)
        self.specializationRowLayout.setObjectName(u"specializationRowLayout")
        self.specializationLabel = QLabel(ProfileScreen)
        self.specializationLabel.setObjectName(u"specializationLabel")

        self.specializationRowLayout.addWidget(self.specializationLabel)

        self.specializationValueLabel = QLabel(ProfileScreen)
        self.specializationValueLabel.setObjectName(u"specializationValueLabel")

        self.specializationRowLayout.addWidget(self.specializationValueLabel)

        self.specializationRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.specializationRowLayout.addItem(self.specializationRowSpacer)


        self.infoLayout.addLayout(self.specializationRowLayout)

        self.experienceRowLayout = QHBoxLayout()
        self.experienceRowLayout.setSpacing(8)
        self.experienceRowLayout.setObjectName(u"experienceRowLayout")
        self.experienceLabel = QLabel(ProfileScreen)
        self.experienceLabel.setObjectName(u"experienceLabel")

        self.experienceRowLayout.addWidget(self.experienceLabel)

        self.experienceValueLabel = QLabel(ProfileScreen)
        self.experienceValueLabel.setObjectName(u"experienceValueLabel")

        self.experienceRowLayout.addWidget(self.experienceValueLabel)

        self.experienceRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.experienceRowLayout.addItem(self.experienceRowSpacer)


        self.infoLayout.addLayout(self.experienceRowLayout)

        self.aboutRowLayout = QHBoxLayout()
        self.aboutRowLayout.setSpacing(8)
        self.aboutRowLayout.setObjectName(u"aboutRowLayout")
        self.aboutLabel = QLabel(ProfileScreen)
        self.aboutLabel.setObjectName(u"aboutLabel")

        self.aboutRowLayout.addWidget(self.aboutLabel)

        self.aboutValueLabel = QLabel(ProfileScreen)
        self.aboutValueLabel.setObjectName(u"aboutValueLabel")

        self.aboutRowLayout.addWidget(self.aboutValueLabel)

        self.aboutRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.aboutRowLayout.addItem(self.aboutRowSpacer)


        self.infoLayout.addLayout(self.aboutRowLayout)

        self.infoBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.infoLayout.addItem(self.infoBottomSpacer)


        self.profileLayout.addLayout(self.infoLayout)


        self.mainLayout.addLayout(self.profileLayout)

        self.editButtonLayout = QHBoxLayout()
        self.editButtonLayout.setObjectName(u"editButtonLayout")
        self.editLeftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editButtonLayout.addItem(self.editLeftSpacer)

        self.editProfileButton = QPushButton(ProfileScreen)
        self.editProfileButton.setObjectName(u"editProfileButton")

        self.editButtonLayout.addWidget(self.editProfileButton)

        self.editRightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editButtonLayout.addItem(self.editRightSpacer)


        self.mainLayout.addLayout(self.editButtonLayout)

        self.publicationsTitleLabel = QLabel(ProfileScreen)
        self.publicationsTitleLabel.setObjectName(u"publicationsTitleLabel")

        self.mainLayout.addWidget(self.publicationsTitleLabel)

        self.publicationRow1 = QFrame(ProfileScreen)
        self.publicationRow1.setObjectName(u"publicationRow1")
        self.publicationRow1.setFrameShape(QFrame.Box)
        self.publicationRow1.setFrameShadow(QFrame.Plain)
        self.row1Layout = QHBoxLayout(self.publicationRow1)
        self.row1Layout.setSpacing(8)
        self.row1Layout.setObjectName(u"row1Layout")
        self.row1Layout.setContentsMargins(8, 6, 8, 6)
        self.row1TitleLabel = QLabel(self.publicationRow1)
        self.row1TitleLabel.setObjectName(u"row1TitleLabel")

        self.row1Layout.addWidget(self.row1TitleLabel)

        self.row1Separator1 = QLabel(self.publicationRow1)
        self.row1Separator1.setObjectName(u"row1Separator1")

        self.row1Layout.addWidget(self.row1Separator1)

        self.row1CategoryLabel = QLabel(self.publicationRow1)
        self.row1CategoryLabel.setObjectName(u"row1CategoryLabel")

        self.row1Layout.addWidget(self.row1CategoryLabel)

        self.row1Separator2 = QLabel(self.publicationRow1)
        self.row1Separator2.setObjectName(u"row1Separator2")

        self.row1Layout.addWidget(self.row1Separator2)

        self.row1RatingLabel = QLabel(self.publicationRow1)
        self.row1RatingLabel.setObjectName(u"row1RatingLabel")

        self.row1Layout.addWidget(self.row1RatingLabel)

        self.row1Separator3 = QLabel(self.publicationRow1)
        self.row1Separator3.setObjectName(u"row1Separator3")

        self.row1Layout.addWidget(self.row1Separator3)

        self.row1EditButton = QPushButton(self.publicationRow1)
        self.row1EditButton.setObjectName(u"row1EditButton")

        self.row1Layout.addWidget(self.row1EditButton)

        self.row1DeleteButton = QPushButton(self.publicationRow1)
        self.row1DeleteButton.setObjectName(u"row1DeleteButton")

        self.row1Layout.addWidget(self.row1DeleteButton)

        self.row1Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.row1Layout.addItem(self.row1Spacer)


        self.mainLayout.addWidget(self.publicationRow1)

        self.publicationRow2 = QFrame(ProfileScreen)
        self.publicationRow2.setObjectName(u"publicationRow2")
        self.publicationRow2.setFrameShape(QFrame.Box)
        self.publicationRow2.setFrameShadow(QFrame.Plain)
        self.row2Layout = QHBoxLayout(self.publicationRow2)
        self.row2Layout.setSpacing(8)
        self.row2Layout.setObjectName(u"row2Layout")
        self.row2Layout.setContentsMargins(8, 6, 8, 6)
        self.row2TitleLabel = QLabel(self.publicationRow2)
        self.row2TitleLabel.setObjectName(u"row2TitleLabel")

        self.row2Layout.addWidget(self.row2TitleLabel)

        self.row2Separator1 = QLabel(self.publicationRow2)
        self.row2Separator1.setObjectName(u"row2Separator1")

        self.row2Layout.addWidget(self.row2Separator1)

        self.row2CategoryLabel = QLabel(self.publicationRow2)
        self.row2CategoryLabel.setObjectName(u"row2CategoryLabel")

        self.row2Layout.addWidget(self.row2CategoryLabel)

        self.row2Separator2 = QLabel(self.publicationRow2)
        self.row2Separator2.setObjectName(u"row2Separator2")

        self.row2Layout.addWidget(self.row2Separator2)

        self.row2RatingLabel = QLabel(self.publicationRow2)
        self.row2RatingLabel.setObjectName(u"row2RatingLabel")

        self.row2Layout.addWidget(self.row2RatingLabel)

        self.row2Separator3 = QLabel(self.publicationRow2)
        self.row2Separator3.setObjectName(u"row2Separator3")

        self.row2Layout.addWidget(self.row2Separator3)

        self.row2EditButton = QPushButton(self.publicationRow2)
        self.row2EditButton.setObjectName(u"row2EditButton")

        self.row2Layout.addWidget(self.row2EditButton)

        self.row2DeleteButton = QPushButton(self.publicationRow2)
        self.row2DeleteButton.setObjectName(u"row2DeleteButton")

        self.row2Layout.addWidget(self.row2DeleteButton)

        self.row2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.row2Layout.addItem(self.row2Spacer)


        self.mainLayout.addWidget(self.publicationRow2)

        self.publicationRow3 = QFrame(ProfileScreen)
        self.publicationRow3.setObjectName(u"publicationRow3")
        self.publicationRow3.setFrameShape(QFrame.Box)
        self.publicationRow3.setFrameShadow(QFrame.Plain)
        self.row3Layout = QHBoxLayout(self.publicationRow3)
        self.row3Layout.setSpacing(8)
        self.row3Layout.setObjectName(u"row3Layout")
        self.row3Layout.setContentsMargins(8, 6, 8, 6)
        self.row3TitleLabel = QLabel(self.publicationRow3)
        self.row3TitleLabel.setObjectName(u"row3TitleLabel")

        self.row3Layout.addWidget(self.row3TitleLabel)

        self.row3Separator1 = QLabel(self.publicationRow3)
        self.row3Separator1.setObjectName(u"row3Separator1")

        self.row3Layout.addWidget(self.row3Separator1)

        self.row3CategoryLabel = QLabel(self.publicationRow3)
        self.row3CategoryLabel.setObjectName(u"row3CategoryLabel")

        self.row3Layout.addWidget(self.row3CategoryLabel)

        self.row3Separator2 = QLabel(self.publicationRow3)
        self.row3Separator2.setObjectName(u"row3Separator2")

        self.row3Layout.addWidget(self.row3Separator2)

        self.row3RatingLabel = QLabel(self.publicationRow3)
        self.row3RatingLabel.setObjectName(u"row3RatingLabel")

        self.row3Layout.addWidget(self.row3RatingLabel)

        self.row3Separator3 = QLabel(self.publicationRow3)
        self.row3Separator3.setObjectName(u"row3Separator3")

        self.row3Layout.addWidget(self.row3Separator3)

        self.row3EditButton = QPushButton(self.publicationRow3)
        self.row3EditButton.setObjectName(u"row3EditButton")

        self.row3Layout.addWidget(self.row3EditButton)

        self.row3DeleteButton = QPushButton(self.publicationRow3)
        self.row3DeleteButton.setObjectName(u"row3DeleteButton")

        self.row3Layout.addWidget(self.row3DeleteButton)

        self.row3Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.row3Layout.addItem(self.row3Spacer)


        self.mainLayout.addWidget(self.publicationRow3)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)


        self.retranslateUi(ProfileScreen)

        QMetaObject.connectSlotsByName(ProfileScreen)
    # setupUi

    def retranslateUi(self, ProfileScreen):
        ProfileScreen.setWindowTitle(QCoreApplication.translate("ProfileScreen", u"6. \u041f\u0440\u043e\u0444\u0438\u043b\u044c \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0430", None))
        self.photoLabel.setText(QCoreApplication.translate("ProfileScreen", u"[\u0424\u043e\u0442\u043e]", None))
        self.nameLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u0418\u043c\u044f:", None))
        self.nameValueLabel.setText(QCoreApplication.translate("ProfileScreen", u"[...]", None))
        self.specializationLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.specializationValueLabel.setText(QCoreApplication.translate("ProfileScreen", u"[...]", None))
        self.experienceLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u041e\u043f\u044b\u0442:", None))
        self.experienceValueLabel.setText(QCoreApplication.translate("ProfileScreen", u"[...]", None))
        self.aboutLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u041e \u0441\u0435\u0431\u0435:", None))
        self.aboutValueLabel.setText(QCoreApplication.translate("ProfileScreen", u"[...]", None))
        self.editProfileButton.setText(QCoreApplication.translate("ProfileScreen", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.publicationsTitleLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u041c\u043e\u0438 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438:", None))
        self.row1TitleLabel.setText(QCoreApplication.translate("ProfileScreen", u"[\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435]", None))
        self.row1Separator1.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row1CategoryLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.row1Separator2.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row1RatingLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u2605 ...", None))
        self.row1Separator3.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row1EditButton.setText(QCoreApplication.translate("ProfileScreen", u"\u0420\u0435\u0434", None))
        self.row1DeleteButton.setText(QCoreApplication.translate("ProfileScreen", u"\u0423\u0434\u0430\u043b", None))
        self.row2TitleLabel.setText(QCoreApplication.translate("ProfileScreen", u"[\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435]", None))
        self.row2Separator1.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row2CategoryLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.row2Separator2.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row2RatingLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u2605 ...", None))
        self.row2Separator3.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row2EditButton.setText(QCoreApplication.translate("ProfileScreen", u"\u0420\u0435\u0434", None))
        self.row2DeleteButton.setText(QCoreApplication.translate("ProfileScreen", u"\u0423\u0434\u0430\u043b", None))
        self.row3TitleLabel.setText(QCoreApplication.translate("ProfileScreen", u"[\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435]", None))
        self.row3Separator1.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row3CategoryLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.row3Separator2.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row3RatingLabel.setText(QCoreApplication.translate("ProfileScreen", u"\u2605 ...", None))
        self.row3Separator3.setText(QCoreApplication.translate("ProfileScreen", u"|", None))
        self.row3EditButton.setText(QCoreApplication.translate("ProfileScreen", u"\u0420\u0435\u0434", None))
        self.row3DeleteButton.setText(QCoreApplication.translate("ProfileScreen", u"\u0423\u0434\u0430\u043b", None))
    # retranslateUi

