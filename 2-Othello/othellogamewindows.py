import os
import platform
import sys
from enum import Enum

import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from WindowsGUI import Ui_MainWindow

# Configs
if platform.system() == "Windows":
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

PIECE_BUTTON_DEFAULT_STYLE_SHEET = "background-color:light gray;"
PIECE_BUTTON_BLACK_STYLE_SHEET = "background-color:Black; color: White" # set font color to white
PIECE_BUTTON_WHITE_STYLE_SHEET = "background-color:White; color: Black"
DEBUG = True
class Color(Enum):
    Black = 0
    White = 1
    NotSet = 2
    def __str__(self):
        return f"{self.name}"
    __repr__ = __str__

class OthelloGameWindows(QMainWindow):
    def __init__(self):
        super(OthelloGameWindows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.piece_buttons = [
            getattr(self.ui, attrname) for attrname in [
                f"{alpha}{num}" for alpha in "abcdefgh" for num in range(1, 9)
            ]
        ]
        # set piece_buttons's click function
        self.ui.reset_button.clicked.connect(self.reset_game)
        self._current_player = Color.Black
        self._game_check_board = [[Color.NotSet for _ in range(8)] for _ in range(8)]
        # set click function to all piece_button
        for pb in self.piece_buttons:
            pb.clicked.connect(
                (lambda _=None, pb=pb: self.click(
                    pb.objectName()))
            )
        self.black_p_cnt, self.white_p_cnt = 0, 0
        self.reset_game()

    def _foreach_piece_button(self, func):
        for pb in self.piece_buttons:
            func(pb)

    def reset_game(self):
        self.ui.GameInfoLabel.setText("Reset/Init game!")
        def _reset_ui(pb: QPushButton):
            pb.setText("")
            pb.setEnabled(True)
            pb.setStyleSheet(PIECE_BUTTON_DEFAULT_STYLE_SHEET)
        self._foreach_piece_button(_reset_ui)
        self._set_piece("d4", Color.White)
        self._set_piece("e5", Color.White)
        self._set_piece("e4", Color.Black)
        self._set_piece("d5", Color.Black)

    def click(self, pos: str):
        self._set_piece(pos, self._current_player)
        if self._current_player == Color.Black:
            self.ui.GameInfoLabel.setText("White Next")
        else:
            self.ui.GameInfoLabel.setText("Black Next")

        # flip player
        self._current_player = Color.White if self._current_player == Color.Black else Color.Black

        if DEBUG:
            self._print_game_board()

    def _set_piece(self, position: str, color: Color) -> bool:
        '''
        1. To set game_board
        2. To set ui
        :param position:
        :param color:
        :return:
        '''
        # Set UI after click
        cur_pb = getattr(self.ui, position)
        if color == Color.Black:
            cur_pb.setText("B")
            cur_pb.setStyleSheet(PIECE_BUTTON_BLACK_STYLE_SHEET)
        else:
            cur_pb.setText("W")
            cur_pb.setStyleSheet(PIECE_BUTTON_WHITE_STYLE_SHEET)
        cur_pb.setEnabled(False)
        # Set game check board after click
        i, j = self._get_indexes(position)
        if self._game_check_board[i][j] is not Color.NotSet:
            return False
        else:
            self._game_check_board[i][j] = color
            return True

    @staticmethod
    def _get_indexes(position: str):
        if len(position) > 2:
            raise ValueError(f"Argument {position} is invalid.")
        return int(position[1]) - 1, "abcdefgh".index(position[0])  # (row, col)

    def get_color(self, pos: str) -> Color:
        i, j = self._get_indexes(pos)
        return ret if (ret := self._game_check_board[i][j]) is not None else Color.NotSet

    # Pragma region Debug Functions:
    def _print_game_board(self):
        print("".join(["=" for _ in range(88)]))
        print(f"count of white: {self.white_p_cnt}")
        print(f"count of black: {self.black_p_cnt}")
        print("\n".join([str(row) for row in self._game_check_board]))
        print("".join(["=" for _ in range(88)]))
    # Pragma region Debug Functions

    def get_piece_count(self, color: Color):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    OthelloGameWindows().show()
    sys.exit(app.exec())
