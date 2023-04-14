# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'replace_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)

from PySide6.QtWidgets import (QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton)

class Ui_replace_window(object):
    def setupUi(self, replace_window):
        if not replace_window.objectName():
            replace_window.setObjectName(u"replace_window")
        replace_window.resize(514, 182)
        self.label = QLabel(replace_window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 61, 31))
        self.wraparound_check = QCheckBox(replace_window)
        self.wraparound_check.setObjectName(u"wraparound_check")
        self.wraparound_check.setGeometry(QRect(20, 150, 111, 30))
        self.find_text = QLineEdit(replace_window)
        self.find_text.setObjectName(u"find_text")
        self.find_text.setGeometry(QRect(100, 20, 271, 31))
        self.findnext_btn = QPushButton(replace_window)
        self.findnext_btn.setObjectName(u"findnext_btn")
        self.findnext_btn.setGeometry(QRect(400, 20, 101, 31))
        self.direction_gbox = QGroupBox(replace_window)
        self.direction_gbox.setObjectName(u"direction_gbox")
        self.direction_gbox.setGeometry(QRect(230, 110, 141, 61))
        self.up_rdbtn = QRadioButton(self.direction_gbox)
        self.up_rdbtn.setObjectName(u"up_rdbtn")
        self.up_rdbtn.setGeometry(QRect(10, 30, 41, 20))
        self.up_rdbtn.setChecked(True)
        self.down_rdbtn = QRadioButton(self.direction_gbox)
        self.down_rdbtn.setObjectName(u"down_rdbtn")
        self.down_rdbtn.setGeometry(QRect(70, 30, 71, 20))
        self.matchcase_check = QCheckBox(replace_window)
        self.matchcase_check.setObjectName(u"matchcase_check")
        self.matchcase_check.setGeometry(QRect(20, 120, 111, 30))
        self.cancel_btn = QPushButton(replace_window)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(400, 140, 101, 31))
        self.replace_btn = QPushButton(replace_window)
        self.replace_btn.setObjectName(u"replace_btn")
        self.replace_btn.setGeometry(QRect(400, 60, 101, 31))
        self.replaceall_btn = QPushButton(replace_window)
        self.replaceall_btn.setObjectName(u"replaceall_btn")
        self.replaceall_btn.setGeometry(QRect(400, 100, 101, 31))
        self.replacewith_text = QLineEdit(replace_window)
        self.replacewith_text.setObjectName(u"replacewith_text")
        self.replacewith_text.setGeometry(QRect(100, 70, 271, 31))
        self.label_2 = QLabel(replace_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 81, 31))

        self.retranslateUi(replace_window)

        QMetaObject.connectSlotsByName(replace_window)
    # setupUi

    def retranslateUi(self, replace_window):
        replace_window.setWindowTitle(QCoreApplication.translate("replace_window", u"Replace", None))
        self.label.setText(QCoreApplication.translate("replace_window", u"Find what:", None))
        self.wraparound_check.setText(QCoreApplication.translate("replace_window", u"Wrap around", None))
        self.findnext_btn.setText(QCoreApplication.translate("replace_window", u"Find next", None))
        self.direction_gbox.setTitle(QCoreApplication.translate("replace_window", u"Direction", None))
        self.up_rdbtn.setText(QCoreApplication.translate("replace_window", u"Up", None))
        self.down_rdbtn.setText(QCoreApplication.translate("replace_window", u"Down", None))
        self.matchcase_check.setText(QCoreApplication.translate("replace_window", u"Match case", None))
        self.cancel_btn.setText(QCoreApplication.translate("replace_window", u"Cancel", None))
        self.replace_btn.setText(QCoreApplication.translate("replace_window", u"Replace", None))
        self.replaceall_btn.setText(QCoreApplication.translate("replace_window", u"Replace All", None))
        self.replacewith_text.setText("")
        self.label_2.setText(QCoreApplication.translate("replace_window", u"Replace with:", None))
    # retranslateUi

