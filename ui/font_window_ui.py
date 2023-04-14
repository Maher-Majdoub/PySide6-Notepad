# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'font_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont)
from PySide6.QtWidgets import (QComboBox, QGroupBox, QLabel, QPushButton, QSpinBox)

class Ui_Font_Window(object):
    def setupUi(self, Font_Window):
        if not Font_Window.objectName():
            Font_Window.setObjectName(u"Font_Window")
        Font_Window.resize(470, 580)
        Font_Window.setMinimumSize(QSize(470, 580))
        Font_Window.setMaximumSize(QSize(470, 580))
        self.label = QLabel(Font_Window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 41))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.label_2 = QLabel(Font_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 10, 111, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Font_Window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 10, 81, 41))
        self.label_3.setFont(font1)
        self.groupBox = QGroupBox(Font_Window)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(150, 270, 301, 121))
        self.groupBox.setFont(font1)
        self.sample_label = QLabel(self.groupBox)
        self.sample_label.setObjectName(u"sample_label")
        self.sample_label.setGeometry(QRect(20, 30, 271, 71))
        self.sample_label.setFont(font1)
        self.sample_label.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Font_Window)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 400, 71, 31))
        self.label_5.setFont(font1)
        self.fontsize_sbox = QSpinBox(Font_Window)
        self.fontsize_sbox.setObjectName(u"fontsize_sbox")
        self.fontsize_sbox.setGeometry(QRect(370, 51, 81, 31))
        self.fontsize_sbox.setMinimum(1)
        self.ok_btn = QPushButton(Font_Window)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(240, 520, 101, 31))
        self.ok_btn.setFont(font1)
        self.cancel_btn = QPushButton(Font_Window)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(350, 520, 101, 31))
        self.cancel_btn.setFont(font1)
        self.show_more_label = QLabel(Font_Window)
        self.show_more_label.setObjectName(u"show_more_label")
        self.show_more_label.setGeometry(QRect(20, 480, 121, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setUnderline(True)
        self.show_more_label.setFont(font2)
        self.show_more_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_more_label.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.script_cbox = QComboBox(Font_Window)
        self.script_cbox.addItem("")
        self.script_cbox.setObjectName(u"script_cbox")
        self.script_cbox.setGeometry(QRect(220, 430, 231, 31))
        self.script_cbox.setFont(font1)
        self.script_cbox.setDuplicatesEnabled(False)
        self.fontfamily_cbox = QComboBox(Font_Window)
        self.fontfamily_cbox.setObjectName(u"fontfamily_cbox")
        self.fontfamily_cbox.setGeometry(QRect(20, 50, 181, 31))
        self.fontfamily_cbox.setEditable(True)
        self.fontstyle_cbox = QComboBox(Font_Window)
        self.fontstyle_cbox.setObjectName(u"fontstyle_cbox")
        self.fontstyle_cbox.setGeometry(QRect(220, 50, 131, 31))
        self.fontstyle_cbox.setEditable(True)

        self.retranslateUi(Font_Window)

        QMetaObject.connectSlotsByName(Font_Window)
    # setupUi

    def retranslateUi(self, Font_Window):
        Font_Window.setWindowTitle(QCoreApplication.translate("Font_Window", u"Font", None))
        self.label.setText(QCoreApplication.translate("Font_Window", u"Font:", None))
        self.label_2.setText(QCoreApplication.translate("Font_Window", u"Font style :", None))
        self.label_3.setText(QCoreApplication.translate("Font_Window", u"Size:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Font_Window", u"Sample", None))
        self.sample_label.setText(QCoreApplication.translate("Font_Window", u"AaBbYyZz", None))
        self.label_5.setText(QCoreApplication.translate("Font_Window", u"Script:", None))
        self.ok_btn.setText(QCoreApplication.translate("Font_Window", u"Ok", None))
        self.cancel_btn.setText(QCoreApplication.translate("Font_Window", u"Cancel", None))
        self.show_more_label.setText(QCoreApplication.translate("Font_Window", u"Show more fonts", None))
        self.script_cbox.setItemText(0, QCoreApplication.translate("Font_Window", u"Western", None))

    # retranslateUi

