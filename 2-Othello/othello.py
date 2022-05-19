# Author: Mux
# Author's Tokai student number: 0cdi2210
try:
    from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
    from PyQt5 import uic
except ImportError as imper:
    print("PyQt5 is not usable, use this program after install it.")
    exit(-1)
from cProfile import label
from dataclasses import dataclass
import sys


@dataclass
class PiecesButton:
    button: QPushButton
    name: str


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        # Loading UI File
        uic.loadUi("main.ui", self)
        self._checkerboard = [[None for _ in range(8)] for _ in range(8)]

        self.pieces_button = [
            self.findChild(QPushButton, i)
            for i in [
                f"{x}{y}" for x in "abcdefgh" for y in range(1, 9)
            ]
        ]

        self.reset_button = self.findChild(QPushButton, "reset_button")
        self.game_info_label = self.findChild(QLabel, "GameInfoLabel")

        # self.button{number}.clicked.connect(lambda: self.clicker(self.button9))
        self.reset_button.clicked.connect(self.reset)

        # Show The App
        self.show()

    def clicker(self, b):
        print(b.name)

    def reset(self):
        print(type(self.reset_button))


if __name__ == "__main__":
    try:
        import os
        assert os.path.exists("main.ui")
    except AssertionError:
        print("Cannot find ui file.")
        exit(-1)
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
