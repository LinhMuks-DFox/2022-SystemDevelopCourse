# Author: Mux
# Author's Tokai student number: 0cdi2210
try:
    from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
    from PyQt5 import uic
except ImportError as imper:
    print("PyQt5 is not usable, use this program after install it.")
import sys

try:
    import os
    assert os.path.exists("main.ui")
except AssertionError:
    print("Cannot find ui file.")


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        # Loading UI File
        uic.loadUi("main.ui", self)

        self._counter = 0  # 0 and 1 repr whose turn
        self.checkerboard = [
            None for _ in range(9)
        ]

        self.pieces_button = [
            self.findChild(QPushButton, f"{i}")
            for i in [f"{x}{y}"for x in "abcdefgh" for y in range(1, 9)]
        ]
        self.reset_button = self.findChild(QPushButton, "reset_button")
        # Defining widgets
        self.game_info_label = self.findChild(QLabel, "GameInforLabel")

        # Click the button
        # self.button{number}.clicked.connect(lambda: self.clicker(self.button9))
        self.reset_button.clicked.connect(self.reset)
        # Show The App
        self.show()

    def clicker(self, b: QPushButton):
        pass

    def reset(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
