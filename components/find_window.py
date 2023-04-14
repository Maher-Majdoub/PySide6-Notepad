from PySide6.QtWidgets import QWidget
from ui.find_window_ui import Ui_find_window
from utils.tools import find



class FindWindow(QWidget, Ui_find_window):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.findnext_btn.clicked.connect(self.findNext)
        self.cancel_btn.clicked.connect(self.close)

    def findNext(self):
        text_edit = self.parent.text_edit
        text = self.find_text.text()

        direction = 'up' if self.up_rdbtn.isChecked() else 'down'
        match_case = self.matchcase_check.isChecked()
        wrap_around = self.wraparound_check.isChecked()

        find(text, text_edit, direction, match_case, wrap_around)
