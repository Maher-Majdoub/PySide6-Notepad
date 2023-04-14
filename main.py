from PySide6.QtWidgets import QApplication
from components.main_window import MainWindow


if __name__ == '__main__': 
    app = QApplication()
    window = MainWindow(app)
    window.show()
    app.exec()
