from PySide6.QtWidgets import QFileDialog, QTextEdit, QDialog
from PySide6.QtGui import QTextDocument, QTextCursor
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
import os, yaml


def saveFile(text : str, path = ''):
    #if we dont pass a value for path in the parameter we will choose a path manually
    if path == '':
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  #desktop location
        path = QFileDialog().getSaveFileName(dir = desktop, filter= '*.txt')[0]
        
    with open(f'{path}.txt', 'w') as f:
        f.write(text)
    return path
                
def openFile(text_edit):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  #desktop location
    path = QFileDialog().getOpenFileName(dir = desktop, filter= '*.txt')[0]
    if path != '':
        with open(path, 'r') as f:
            text = f.read()
            text_edit.setText(text)
        return path

def getSettings(): 
    with open('settings.yml', 'r') as f:
        settings = yaml.safe_load(f)

    return settings

def updateFontSettings(family, style, size, strikeout, underline):
    settings = getSettings()
    f_settings = settings['font_settings']
    f_settings['family'] = family
    f_settings['style'] = style
    f_settings['size'] = size
    f_settings['strikeout'] = strikeout
    f_settings['underline'] = underline
       
    with open('settings.yml', 'w') as f:
        yaml.dump(settings, f)
                
def find(text, text_edit: QTextEdit, direction = 'up', match_case = True, wrap_around = False):
    if text == '' or text_edit.toPlainText().find(text) == -1:
        return
    f1 = QTextDocument.FindFlag.FindWholeWords 
    f2 = QTextDocument.FindFlag.FindCaseSensitively if match_case else f1
    f3 = QTextDocument.FindFlag.FindBackward if direction == 'down' else f1
    
    cursor = text_edit.find(text, f1 | f2 | f3)
    if not cursor and wrap_around:
        new_cursor = QTextCursor(text_edit.document())
        new_cursor.setPosition(0 if direction == 'up' else len(text_edit.toPlainText()))
        text_edit.setTextCursor(new_cursor)
        find(text, text_edit, direction, match_case, wrap_around)

def printFile(text_edit):
    printer = QPrinter()
    dialog = QPrintDialog(printer, text_edit)
    if dialog.exec_() == QDialog.Accepted:
        document = QTextDocument()
        document.setPlainText(text_edit.toPlainText())
        document.print_(printer)
        