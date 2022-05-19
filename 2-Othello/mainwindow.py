import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from WindowsGUI import Ui_MainWindow
import PySide6
import os

# Configs
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class OthelloGame:
    def __init__(self):
        self.check_board = [[None for _ in range(8)] for _ in range(8)]

    def change_piece(self, position: str):
        print(position)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.othello = OthelloGame()
        self.piece_bottons = [
            getattr(self.ui, attrname) for attrname in [
                f"{alpha}{num}" for alpha in "abcdefgh" for num in range(1, 9)
            ]
        ]
        for pb in self.piece_bottons:
            pb.clicked.connect(
                (lambda _=None, pb=pb: self.othello.change_piece(
                    pb.objectName()))
            )

        self.ui.reset_button.clicked.connect(self.reset)
        self.show()

    def reset(self):
        self.ui.GameInfoLabel.setText("Reset game!")
        print("reset_button pressed.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
