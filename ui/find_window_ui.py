# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)

from PySide6.QtWidgets import (QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,)

class Ui_find_window(object):
    def setupUi(self, find_window):
        if not find_window.objectName():
            find_window.setObjectName(u"find_window")
        find_window.resize(500, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(find_window.sizePolicy().hasHeightForWidth())
        find_window.setSizePolicy(sizePolicy)
        find_window.setMinimumSize(QSize(500, 160))
        find_window.setMaximumSize(QSize(500, 160))
        find_window.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label = QLabel(find_window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 31))
        self.find_text = QLineEdit(find_window)
        self.find_text.setObjectName(u"find_text")
        self.find_text.setGeometry(QRect(90, 20, 271, 31))
        self.findnext_btn = QPushButton(find_window)
        self.findnext_btn.setObjectName(u"findnext_btn")
        self.findnext_btn.setGeometry(QRect(390, 20, 101, 31))
        self.cancel_btn = QPushButton(find_window)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(390, 60, 101, 31))
        self.direction_gbox = QGroupBox(find_window)
        self.direction_gbox.setObjectName(u"direction_gbox")
        self.direction_gbox.setGeometry(QRect(220, 70, 141, 61))
        self.up_rdbtn = QRadioButton(self.direction_gbox)
        self.up_rdbtn.setObjectName(u"up_rdbtn")
        self.up_rdbtn.setGeometry(QRect(10, 30, 41, 20))
        self.up_rdbtn.setChecked(True)
        self.down_rdbtn = QRadioButton(self.direction_gbox)
        self.down_rdbtn.setObjectName(u"down_rdbtn")
        self.down_rdbtn.setGeometry(QRect(70, 30, 71, 20))
        self.matchcase_check = QCheckBox(find_window)
        self.matchcase_check.setObjectName(u"matchcase_check")
        self.matchcase_check.setGeometry(QRect(10, 80, 111, 30))
        self.wraparound_check = QCheckBox(find_window)
        self.wraparound_check.setObjectName(u"wraparound_check")
        self.wraparound_check.setGeometry(QRect(10, 110, 111, 30))

        self.retranslateUi(find_window)

        QMetaObject.connectSlotsByName(find_window)
    # setupUi

    def retranslateUi(self, find_window):
        find_window.setWindowTitle(QCoreApplication.translate("find_window", u"Find", None))
        self.label.setText(QCoreApplication.translate("find_window", u"Find what:", None))
        self.findnext_btn.setText(QCoreApplication.translate("find_window", u"Find next", None))
        self.cancel_btn.setText(QCoreApplication.translate("find_window", u"Cancel", None))
        self.direction_gbox.setTitle(QCoreApplication.translate("find_window", u"Direction", None))
        self.up_rdbtn.setText(QCoreApplication.translate("find_window", u"Up", None))
        self.down_rdbtn.setText(QCoreApplication.translate("find_window", u"Down", None))
        self.matchcase_check.setText(QCoreApplication.translate("find_window", u"Match case", None))
        self.wraparound_check.setText(QCoreApplication.translate("find_window", u"Wrap around", None))
    # retranslateUi

