"""
Author: Mux
"""

import collections
import enum
import os
import platform
import sys

import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import WindowsGUI
from Configs import *

# Configs
if platform.system() == "Windows":
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


# Pragma region Constants

class Color(enum.Enum):
    Black = 0
    White = 1
    NotSet = 2

    def __str__(self):
        return f"{self.name}"

    __repr__ = __str__


class OthelloGame(QMainWindow):
    def __init__(self):
        super(OthelloGame, self).__init__()
        self.ui = WindowsGUI.Ui_MainWindow()
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
            pb.clicked.connect((lambda _=None, pb=pb: self.click(pb.objectName())))
        self.pressed_button_cnt = 0
        self.reset_game()

    def foreach_piece_button(self, func, **kwargs):
        for pb in kwargs["btn_list"] if len(kwargs) != 0 else self.piece_buttons:
            func(pb)

    def reset_game(self):
        self.ui.GameInfoLabel.setText("Reset/Init game!")

        def _reset_ui(pb: QPushButton):
            pb.setText("")
            pb.setEnabled(True)
            pb.setStyleSheet(PIECE_BUTTON_DEFAULT_STYLE_SHEET)

        self.foreach_piece_button(_reset_ui)
        self._game_check_board = [[Color.NotSet for _ in range(8)] for _ in range(8)]
        self.set_piece("d4", Color.White)
        self.set_piece("e5", Color.White)
        self.set_piece("e4", Color.Black)
        self.set_piece("d5", Color.Black)
        self.pressed_button_cnt = 4
        self.ui.TotalCounter.setText(f"Total: {self.pressed_button_cnt}")
        self.ui.BlackPieceCounter.setText(f"Black: {2}")
        self.ui.WhitePieceCounter.setText(f"White: {2}")
        self.rander_valid_place(Color.Black)
        self._current_player = Color.Black

    def pb_enable(self, b):
        def _able(pb: QPushButton):
            pb.setEnabled(b)

        self.foreach_piece_button(_able)

    def click(self, pos: str):

        # TODO: Check if piece is placed at a valid position
        # pre_valid_place = self._get_valid_place(self._current_player)
        # if pos not in pre_valid_place:
        #     return

        # Set piece
        self.set_piece(pos, self._current_player)
        # check if winner occurred
        if 64 - self.pressed_button_cnt == 0:
            self.ui.GameInfoLabel.setText(f"Winner is: {self.check_winner()}!")
            self.pb_enable(False)
            return

        # TODO: Rander valid place here
        # self._rander_valid_place(self._current_player)

        # Change next player message
        if self._current_player == Color.Black:
            self.ui.GameInfoLabel.setText("White Next")
        else:
            self.ui.GameInfoLabel.setText("Black Next")

        # flip player
        self._current_player = Color.White if self._current_player == Color.Black else Color.Black
        self.ui.TotalCounter.setText(f"Total: {self.pressed_button_cnt}")
        self.ui.BlackPieceCounter.setText(f"Black: {self.count_color(Color.Black)}")
        self.ui.WhitePieceCounter.setText(f"White: {self.count_color(Color.White)}")

        if DEBUG:
            self.print_game_board()

    def set_piece(self, position: str, color: Color):
        '''
        1. To set game_board
        2. To set ui
        :param position:
        :param color:
        :return:
        '''
        # For flip color:
        i, j = self.string2indexes(position)
        if self._game_check_board[i][j] is Color.NotSet:
            self._game_check_board[i][j] = color
        else:
            self._game_check_board[i][j] = Color.Black if color == Color.White else Color.White

        # Set UI after click
        cur_pb = getattr(self.ui, position)
        if color == Color.Black:
            cur_pb.setText("B")
            cur_pb.setStyleSheet(PIECE_BUTTON_BLACK_STYLE_SHEET)
        else:
            cur_pb.setText("W")
            cur_pb.setStyleSheet(PIECE_BUTTON_WHITE_STYLE_SHEET)

        self.pressed_button_cnt += 1
        cur_pb.setEnabled(False)

    @staticmethod
    def string2indexes(position: str) -> tuple:
        """
        Convert Button's name to 2D array indexes
        a1 -> (0, 0)
        :param position: [a-h][1-8]
        :return: a tuple of index in (i row, j colum)
        """
        if len(position) > 2:
            raise ValueError(f"Argument {position} is invalid.")
        return int(position[1]) - 1, "abcdefgh".index(position[0])  # (row, col)

    @staticmethod
    def indexes2string(i_row, j_col) -> str:
        if not 0 < i_row < 8 or not 0 < j_col < 8:
            raise ValueError(f"Index is out of range:({i_row}, {j_col})")
        return f'{"abcdefgh"[j_col]}{i_row}'

    def get_color_of_index(self, pos: str) -> Color:
        """
        Get the color of a position
        :param pos: position
        :return: Color
        """
        i, j = self.string2indexes(pos)
        return self._game_check_board[i][j]

    def print_game_board(self):
        print("".join(["=" for _ in range(88)]))
        print(f"Total pressed button: {self.pressed_button_cnt}")
        print(f"Total unpressed: {self.count_color(Color.NotSet)}")
        print("\n".join([str(row) for row in self._game_check_board]))
        print("".join(["=" for _ in range(88)]))

    def count_color(self, color: Color) -> int:
        return sum([collections.Counter(row)[color] for row in self._game_check_board])

    def check_winner(self) -> Color:
        return Color.Black if self.count_color(Color.Black) > self.count_color(Color.White) else Color.White

    def get_placed_piece(self, target: Color):
        ret = []
        for i, r in enumerate(self._game_check_board):
            for j, c in enumerate(r):
                if c == target:
                    ret.append(f"{'abcdefgh'[i]}{j+1}")
        return ret

    # TODO: Complete this method
    def get_valid_place(self, color: Color) -> list:
        """
        找到每一个棋子的周围的位置s，对每一个位置进行一次是否可以放入棋子的判断
        可以就放入返回的列表中
        """
        valid_place = list()
        placed_color = self.get_placed_piece(color)

        for pc in placed_color:
            around_move, around_space = self.get_around(pc)
            around_move = {v: k for k, v in around_move.items()}
            around_move_list = []

            # 去除已经被占用的
            for i in around_move.keys():
                if self.get_color_of_index(i) == Color.NotSet:
                    around_move_list.append(i)

            # 对于没有被占用的空间来说，
            for i in around_move_list:
                if self.get_color_of_index(around_space[around_move[i]]) != Color.NotSet and \
                    self.get_color_of_index(around_space[around_move[i]]) != color:
                    valid_place.append(i)
        return valid_place

    # TODO: Complete this method
    def check_color_flip(self, pos):
        pass

    def get_around(self, pos: str) -> [dict, dict]:
        row, col = int(pos[1]), pos[0]
        row_idx, col_idx = self.string2indexes(pos)
        direction = {
            "u": True,  # up
            "d": True,  # down
            "l": True,  # left
            "r": True,  # right
        }
        move_ment = {
            "u": lambda: f"{col}{row - 2}",
            "d": lambda: f"{col}{row + 2}",
            "l": lambda: f"{'abcdefgh'[col_idx - 2]}{row}",
            "r": lambda: f"{'abcdefgh'[col_idx + 2]}{row}",

            "ul": lambda: f"{'abcdefgh'[col_idx - 2]}{row - 2}",
            "ur": lambda: f"{'abcdefgh'[col_idx + 2]}{row - 2}",
            "dl": lambda: f"{'abcdefgh'[col_idx - 2]}{row + 2}",
            "dr": lambda: f"{'abcdefgh'[col_idx + 2]}{row + 2}",
        }
        around_space_f = {
            "u": lambda: f"{col}{row - 1}",
            "d": lambda: f"{col}{row + 1}",
            "l": lambda: f"{'abcdefgh'[col_idx - 1]}{row}",
            "r": lambda: f"{'abcdefgh'[col_idx + 1]}{row}",

            "ul": lambda: f"{'abcdefgh'[col_idx - 1]}{row - 1}",
            "ur": lambda: f"{'abcdefgh'[col_idx + 1]}{row - 1}",
            "dl": lambda: f"{'abcdefgh'[col_idx - 1]}{row + 1}",
            "dr": lambda: f"{'abcdefgh'[col_idx + 1]}{row + 1}",
        }
        around, around_space = dict(), dict()
        if col in "ab":
            direction["l"] = False
        if col in "gh":
            direction["r"] = False
        if row in [1, 2]:
            direction["u"] = False
        if row in [7, 8]:
            direction["d"] = False

        for k, v in direction.items():
            if v:
                around[k] = move_ment[k]()
                around_space[k] = around_space_f[k]()

        if direction["u"] and direction["l"]:
            around["ul"] = move_ment["ul"]()
            around_space["ul"] = around_space_f["ul"]()

        if direction["u"] and direction["r"]:
            around["ur"] = move_ment["ur"]()
            around_space["ur"] = around_space_f["ur"]()

        if direction["d"] and direction["l"]:
            around["dl"] = move_ment["dl"]()
            around_space["dl"] = around_space_f["dl"]()

        if direction["d"] and direction["r"]:
            around["dr"] = move_ment["dr"]()
            around_space["dr"] = around_space_f["dr"]()

        return [around, around_space]

    def rander_valid_place(self, color: Color):
        def bunt_rander(pb: QPushButton):
            pb.setStyleSheet(PIECE_BUTTON_VALID_PLACE_STYLE_SHEET)
            pb.setText("V")
        self.foreach_piece_button(
            bunt_rander,
            btn_list=[getattr(self.ui, name) for name in self.get_valid_place(color)]
        )


if __name__ == "__main__":
    if sys.version_info[1] < 8:
        print("Python version should greater than 3.8")
        exit(-1)
    app = QApplication(sys.argv)
    game = OthelloGame()
    game.show()
    print(game.get_valid_place(Color.Black))
    sys.exit(app.exec())
