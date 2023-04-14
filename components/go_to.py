from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QIntValidator, QTextCursor

class GoTo(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('Go To Line')
        label = QLabel('Line Number : ')
        self.line_number = QLineEdit()
        self.line_number.setValidator(QIntValidator())
        self.go_btn = QPushButton('Go')
        self.cancel_btn = QPushButton('Cancel')
        
        btns_layout = QHBoxLayout()
        btns_layout.addWidget(self.go_btn)
        btns_layout.addWidget(self.cancel_btn)
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.line_number)
        layout.addLayout(btns_layout)
        
        self.setLayout(layout)

        self.cancel_btn.clicked.connect(self.close)
        self.go_btn.clicked.connect(self.goTo)
        
        
    def goTo(self):
        line = self.line_number.text()
        
        if line != '':
            if not line.isnumeric():
                raise Exception('Line number must be integer')
            text_edit = self.parent.text_edit
            num_lines = text_edit.document().blockCount()
            if (int(line) <= num_lines):
                cursor = QTextCursor(text_edit.document().findBlockByLineNumber(int(line) - 1))
                text_edit.setTextCursor(cursor)
                self.close()
            else:
                self.showWarnig(f'This file contains only {num_lines} lines!')
        else:
            self.showWarnig('Please Enter The Line Number!')
    
    
    def showWarnig(self, text):
        QMessageBox.warning(self, 'Invalid Line Number' ,text, QMessageBox.Ok)
                
        
            
        
        
        
        
        
        