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


class Color(Enum):
    Black = 0
    White = 1
    NotSetted = 2


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
        self.ui.reset_button.clicked.connect(self.reset_ui)
        self._current_player = Color.Black
        self._game_check_board = [[None for _ in range(8)] for _ in range(8)]
        # set click function to all piece_button
        for pb in self.piece_buttons:
            pb.clicked.connect(
                (lambda _=None, pb=pb: self.click(
                    pb.objectName()))
            )
        self.reset_ui()

    def _foreach_piece_button(self, func):
        for pb in self.piece_buttons:
            func(pb)

    def reset_ui(self):
        self.ui.GameInfoLabel.setText("Reset/Init game!")

        def _reset_ui(pb: QPushButton):
            pb.setText("")
            pb.setEnabled(True)
            pb.setStyleSheet("background-color:light gray;")

        self._foreach_piece_button(_reset_ui)

    def click(self, pos: str):
        self._change_game_board(pos, self._current_player)
        cur_pb = getattr(self.ui, pos)
        if self._current_player == Color.Black:
            cur_pb.setText("B")
            cur_pb.setStyleSheet("background-color:Black; color: White")
            self.ui.GameInfoLabel.setText("White Next")
        else:
            cur_pb.setText("W")
            cur_pb.setStyleSheet("background-color:White; color: Black")
            self.ui.GameInfoLabel.setText("Black Next")

        cur_pb.setEnabled(False)
        # 反转玩家
        self._current_player = Color.White if self._current_player == Color.Black else Color.Black

        self._print_game_board()

    def _change_game_board(self, position: str, color: Color) -> bool:
        i, j = self._get_indexes(position)
        if self._game_check_board[i][j] is not None:
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
        return ret if (ret := self._game_check_board[i][j]) is not None else Color.NotSetted

    # Pragma region Debug Functions:
    def _print_game_board(self):
        print("".join(["=" for _ in range(88)]))
        print("\n".join([str(row) for row in self._game_check_board]))
        print("".join(["=" for _ in range(88)]))
    # Pragma region Debug Functions


if __name__ == "__main__":
    app = QApplication(sys.argv)
    OthelloGameWindows().show()
    sys.exit(app.exec())
