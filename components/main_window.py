from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMessageBox, QFontDialog
from PySide6.QtGui import QFont, QKeySequence
from .find_window import FindWindow
from .replace_window import ReplaceWindow
from .menu_bar import MenuBar
from .go_to import GoTo
from utils.tools import *
from datetime import datetime as dt
import webbrowser



class MainWindow(QMainWindow):
    def __init__(self, app : QApplication):
        super().__init__()
        self.app = app
        self.setWindowTitle('Text editor')
          
        self.menubar = MenuBar()
        self.find_window = FindWindow(self)
        self.replace_window = ReplaceWindow(self)
        self.goto_window = GoTo(self)
        
        self.text_edit = QTextEdit()
        self.setMenuBar(self.menubar)
        self.setCentralWidget(self.text_edit)
        self.file_path = ''
        self.file_saved = False
        self.loadFont()

        self.text_edit.textChanged.connect(self.textChanged)
        
        #file menu actions
        self.menubar.new_file_act.triggered.connect(self.newFile)
        self.menubar.new_file_act.setShortcut(QKeySequence('Ctrl+N'))
        # self.menubar.new_win_act.triggered.connect(app.exec)
        self.menubar.new_win_act.setShortcut(QKeySequence('Ctrl+Shift+N'))   
        self.menubar.open_file_act.triggered.connect(self.open)
        self.menubar.open_file_act.setShortcut(QKeySequence('Ctrl+O'))        
        self.menubar.save_file_act.triggered.connect(self.save)
        self.menubar.save_file_act.setShortcut(QKeySequence('Ctrl+S'))   
        self.menubar.saveas_file_act.triggered.connect(self.saveAs)
        self.menubar.saveas_file_act.setShortcut(QKeySequence('Ctrl+Shift+S'))   
        self.menubar.print_act.triggered.connect(lambda : printFile(self.text_edit))
        self.menubar.print_act.setShortcut(QKeySequence('Ctrl+P'))   
        self.menubar.exit_app_act.triggered.connect(self.app.quit)
            
        #edit menu actions
        self.menubar.undo_act.triggered.connect(self.text_edit.undo)
        self.menubar.undo_act.setShortcut(QKeySequence('Ctrl+Z')) 
        self.menubar.redo_act.triggered.connect(self.text_edit.redo)
        self.menubar.redo_act.setShortcut(QKeySequence('Ctrl+Y')) 
        self.menubar.cut_act.triggered.connect(self.text_edit.cut)
        self.menubar.cut_act.setShortcut(QKeySequence('Ctrl+X')) 
        self.menubar.copy_act.triggered.connect(self.text_edit.copy)
        self.menubar.copy_act.setShortcut(QKeySequence('Ctrl+C')) 
        self.menubar.paste_act.triggered.connect(self.text_edit.paste)
        self.menubar.paste_act.setShortcut(QKeySequence('Ctrl+V'))   
        self.menubar.delete_act.triggered.connect(self.text_edit.cut)
        self.menubar.googleit_act.triggered.connect(self.google)
        self.menubar.googleit_act.setShortcut(QKeySequence('Ctrl+E')) 
        self.menubar.find_act.triggered.connect(self.findText)
        self.menubar.find_act.setShortcut(QKeySequence('Ctrl+F'))
        self.menubar.find_next_act.triggered.connect(self.findNext)
        self.menubar.find_next_act.setShortcut(QKeySequence('F3'))
        self.menubar.find_previous_act.triggered.connect(self.findPrevious)
        self.menubar.find_previous_act.setShortcut(QKeySequence('Shift+F3'))
        self.menubar.replace_act.triggered.connect(self.replaceText)
        self.menubar.replace_act.setShortcut(QKeySequence('Ctrl+H'))
        self.menubar.goto_act.triggered.connect(self.goTo)
        self.menubar.goto_act.setShortcut(QKeySequence('Ctrl+G'))
        self.menubar.select_all_act.triggered.connect(self.text_edit.selectAll)
        self.menubar.select_all_act.setShortcut(QKeySequence('Ctrl+A'))
        self.menubar.time_date_act.triggered.connect(self.add_datetime)
        self.menubar.time_date_act.setShortcut(QKeySequence('F5'))
        
        #format menu actions
        self.menubar.word_wrap_act.triggered.connect(self.setWordWrap)
        self.menubar.font_act.triggered.connect(self.updateFont)
        
        #view menu actions
        self.menubar.zoom_in_act.triggered.connect(self.text_edit.zoomIn)
        self.menubar.zoom_in_act.setShortcut(QKeySequence('Ctrl++'))
        self.menubar.zoom_out_act.triggered.connect(self.text_edit.zoomOut)
        self.menubar.zoom_out_act.setShortcut(QKeySequence('Ctrl+-'))
        self.menubar.restore_default_act.triggered.connect(self.loadFont)
        self.menubar.restore_default_act.setShortcut(QKeySequence('Ctrl+Plus'))
        
        #help menu actions
        self.menubar.help_act.triggered.connect(self.showHelp)
        self.menubar.send_feedback_act.triggered.connect(self.showSendFeedback)
        self.menubar.about_me_act.triggered.connect(self.aboutMe)
 
            
    def updateFont(self):
        diag = QFontDialog.getFont(self.text_edit.font(), self)
        response = diag[0]
        if response:
            font = diag[1]
            self.text_edit.setFont(font)
            family = font.family()
            style = font.styleName()
            size = font.pointSize()
            strikeout = font.strikeOut()
            underline = font.underline()
            print(family, style, size, strikeout, underline)
            updateFontSettings(family, style, size, strikeout, underline)
    
    def loadFont(self):
        font = QFont()
        settings = getSettings()['font_settings']
        font.setFamily(settings['family'])
        style = settings['style'].lower()
        font.setBold(style.find('bold') != -1)
        font.setItalic(style.find('italic') != -1)
        
        font.setPointSize(settings['size'])
        font.setStrikeOut(settings['strikeout'])
        font.setUnderline(settings['underline'])
        
        self.text_edit.setFont(font)
        
        
    def textChanged(self):
        self.file_saved = False
        
             
    def save(self):
        if not self.file_saved:
            if self.file_path == '':
                path = saveFile(self.text_edit.toPlainText())
                if path != '':  #file saved
                    self.file_path = path
                    self.file_saved = True
            else: #we are already working on a file
                saveFile(self.text_edit.toPlainText(), self.file_path)
                self.file_saved = True
            
    def saveAs(self):
        path = saveFile(self.text_edit.toPlainText())
        self.file_path = path
        self.file_saved = True
      
    def checkSaving(self):
        if not self.file_saved and self.text_edit.toPlainText() != '' :
            res = QMessageBox().warning(self, 'File not saved', 'Do you want to save changes ?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if res == QMessageBox.Yes:
                self.menubar.save_file_act.trigger()
            elif res == QMessageBox.Cancel:
                return False
        return True
        
    def newFile(self):
        if self.checkSaving():
            self.file_saved = False
            self.file_path = ''
            self.text_edit.setText('')
            
    def open(self):
        if self.checkSaving():
            openFile(self.text_edit)
            
            
        
    def google(self):
        text = self.text_edit.textCursor().selectedText()
        if text != '':
            url = f'https://www.google.com/search?q={text.replace(" ", "+")}'
            webbrowser.open_new_tab(url)
        else:
            QMessageBox.warning(self,  'No Selected Text', 'Please select a text to google it', QMessageBox.Ok)
                    
    def findText(self):
        window = self.find_window
        window.find_text.setText(self.text_edit.textCursor().selectedText())
        window.show()
    
    def replaceText(self):
        window = self.replace_window
        window.find_text.setText(self.text_edit.textCursor().selectedText())
        window.show()
        
    def goTo(self):
        window = self.goto_window
        window.show()
        
    def add_datetime(self):
        now = dt.now()
        date = now.strftime('%I:%M %p %d/%m/%y')
        self.text_edit.textCursor().insertText(date)
        
    def setWordWrap(self):
        wrap = self.menubar.word_wrap_act.isChecked()
        self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap if wrap else QTextEdit.LineWrapMode.WidgetWidth)
        
    def showHelp(self):
        QMessageBox.information(self, 'what?', 'Dude are you serious?\nYou need help for a simple text editor app??', QMessageBox.Ok)
    
    def showSendFeedback(self):
        QMessageBox.information(self, 'Sorry', 'Thanks but not now :)', QMessageBox.Ok)
        
    def aboutMe(self):
        QMessageBox.information(self, 'Meher Majdoub', '**Just a guy who likes programming :)**\nmail: maher.majjdoub@gmail.com', QMessageBox.Ok)

    def findNext(self):
        text = self.text_edit.textCursor().selectedText()
        text_edit = self.text_edit
        find(text, text_edit)
        
        
    def findPrevious(self):
        text = self.text_edit.textCursor().selectedText()
        text_edit = self.text_edit
        direction = 'down'
        find(text, text_edit, direction)
        
        

        
        