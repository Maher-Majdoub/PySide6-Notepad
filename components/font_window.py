from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtGui import QFontDatabase
from ui.font_window_ui import Ui_Font_Window
from utils.tools import *



class FontWindow(QWidget, Ui_Font_Window):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.font_families = QFontDatabase.families()
        self.fontfamily_cbox.addItems(self.font_families)
        self.fontfamily_cbox.setAutoFillBackground(True)

        settings = getSettings()['font_settings']
        self.fontfamily_cbox.setEditText(settings['font_family'])   
        self.fontsize_sbox.setValue(settings['font_size'])
        self.fontstyle_cbox.setEditText(settings['font_style'])
        self.updateSample()

        self.fontfamily_cbox.currentTextChanged.connect(self.fontChanged)
        self.fontstyle_cbox.currentTextChanged.connect(self.updateSample)
        self.fontsize_sbox.valueChanged.connect(self.updateSample)
        self.ok_btn.clicked.connect(self.saveSettings)
        self.cancel_btn.clicked.connect(self.close)

    
    def verifyEntries(self):
        font_family = self.fontfamily_cbox.currentText()
        font_style = self.fontstyle_cbox.currentText()
        return font_family in self.font_families and font_style in QFontDatabase.styles(font_family)
    
     
    def fontChanged(self):
        font_family = self.fontfamily_cbox.currentText()
        if font_family in self.font_families:
            styles = QFontDatabase.styles(font_family)
            self.fontstyle_cbox.clear()
            self.fontstyle_cbox.addItems(styles)
            self.updateSample()
            
    def updateSample(self):
        if self.verifyEntries():
            label = self.sample_label
            font = QFont()
            font.setPointSize(self.fontsize_sbox.value())
            font.setFamily(self.fontfamily_cbox.currentText())
            font.setBold(True if self.fontstyle_cbox.currentText().lower().find('bold') != -1 else False)
            font.setItalic(True if self.fontstyle_cbox.currentText().lower().find('italic') != -1 else False)
            label.setFont(font)
            
    def saveSettings(self):
        if self.verifyEntries():
            updateFontSettings(self.fontfamily_cbox.currentText(), self.fontstyle_cbox.currentText(), self.fontsize_sbox.value(), self.script_cbox.currentText())
            self.parent.updateStyleSheet()
            self.close()
            
        else:
            QMessageBox.warning(self, 'Invalid Font Settings', 'Please choose valid font settings !', QMessageBox.Ok)