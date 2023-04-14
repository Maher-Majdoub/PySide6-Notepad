from PySide6.QtWidgets import QWidget
from ui.replace_window_ui import Ui_replace_window
from utils.tools import *
class ReplaceWindow(QWidget, Ui_replace_window):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.findnext_btn.clicked.connect(self.findNext)
        self.replace_btn.clicked.connect(self.replace) 
        self.replaceall_btn.clicked.connect(self.replaceAll)       
        
    
        
    def findNext(self):
        text_edit = self.parent.text_edit
        text = self.find_text.text()
        direction = 'up' if self.up_rdbtn.isChecked() else 'down'
        match_case = self.matchcase_check.isChecked()
        wrap_around = self.wraparound_check.isChecked()

        find(text, text_edit, direction, match_case, wrap_around)
        
        
    def replace(self):
        selected_text = self.parent.text_edit.textCursor().selectedText()
        if self.find_text.text() == '' or selected_text !=  self.find_text.text():
            return
        
        self.parent.text_edit.textCursor().insertText(self.replacewith_text.text())   
        self.findNext()   
        
    def replaceAll(self):
        if self.find_text.text() == '':
            return
        new_text = self.parent.text_edit.toPlainText().replace(self.find_text.text(), self.replacewith_text.text())
        self.parent.text_edit.setText(new_text)