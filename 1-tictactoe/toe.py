# Author: Mux
# Author's Tokai student number: 0cdi2210
# This UI File was created by the instructions below:
# https://www.youtube.com/watch?v=5yyD-dQojC4&t56s
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
    WIN_FORMS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self):
        super(UI, self).__init__()
        # Loading UI File
        uic.loadUi("main.ui", self)

        self._counter = 0  # 0 and 1 repr whose turn
        self.checkerboard = [
            None for _ in range(9)
        ]
        # Defining widgets
        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")
        self.label = self.findChild(QLabel, "label")

        # Click the button
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)

        self._game_button_list = {
            self.button1: 0,
            self.button2: 3,
            self.button3: 6,
            self.button4: 1,
            self.button5: 4,
            self.button6: 7,
            self.button7: 2,
            self.button8: 5,
            self.button9: 8,
        }

        # Show The App
        self.show()

    def win_msg(self):
        self.label.setText("")

    def clicker(self, b: QPushButton):

        # Flip button
        mark = "X" if self._counter % 2 == 0 else "O"
        turn = "X" if mark == "O" else "O"
        b.setText(mark)
        self.label.setText(f"{turn}'s turn!")
        b.setEnabled(False)

        # Mark to checkboard
        self.checkerboard[self._game_button_list[b]] = mark
        self._counter += 1

        # Winner Check here
        if self.check_win("X"):
            self.label.setText("X is winner!")
            for b in self._game_button_list:
                b.setEnabled(False)
        elif self.check_win("O"):
            self.label.setText("O is winner!")
            for b in self._game_button_list:
                b.setEnabled(False)
        # if Full than reset
        if self._counter == 9:
            self.reset()

    def reset(self):
        for b in self._game_button_list.keys():
            b.setText("")
            b.setEnabled(True)
        self._counter = 0
        self.label.setText("X Gose First!")
        self.checkerboard = [None for _ in range(9)]

    def check_win(self, mark) -> bool:
        marks = []
        for form in self.WIN_FORMS:
            for idx in form:
                marks.append(
                    True if self.checkerboard[idx] == mark and self.checkerboard[idx] is not None else False
                )
            if all(marks):
                return True
            marks = []
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
