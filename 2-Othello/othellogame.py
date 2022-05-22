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
        self._current_player = Color.Black
        self.re_rander_ui()

    def pb_enable(self, b):
        def _able(pb: QPushButton):
            pb.setEnabled(b)

        self.foreach_piece_button(_able)

    def click(self, pos: str):

        valid_place = self.get_valid_place(self._current_player)
        if pos not in valid_place:
            return

        # Set piece
        self.set_piece(pos, self._current_player)

        # Flip Colors
        self.check_color_flip(pos, self._current_player)
        self.print_game_board()

        # check if winner occurred
        if 64 - self.pressed_button_cnt == 0:
            self.winner_occurred()
            return

        # flip player
        self._current_player = Color.White if self._current_player == Color.Black else Color.Black
        self.re_rander_ui()

    def winner_occurred(self):
        self.ui.GameInfoLabel.setText(f"Winner is: {self.check_winner()}!")
        self.pb_enable(False)

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

        self._game_check_board[i][j] = color

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
                    ret.append(f"{'abcdefgh'[i]}{j + 1}")
        return ret

    def get_valid_place(self, color: Color) -> [str, ...]:
        """
        找到每一个棋子的周围的位置s，对每一个位置进行一次是否可以放入棋子的判断
        可以就放入返回的列表中
        """
        valid_place = list()
        placed_color = self.get_placed_piece(color)

        for pc in placed_color:
            outer_around, inner_around = self.get_around(pc)
            outer_around = {v: k for k, v in outer_around.items()}
            around_move_list = []

            # 去除已经被占用的
            for i in outer_around.keys():
                if self.get_color_of_index(i) == Color.NotSet:
                    around_move_list.append(i)

            # 对于没有被占用的空间来说，
            for i in around_move_list:
                inner_color = self.get_color_of_index(inner_around[outer_around[i]])
                if inner_color != Color.NotSet and inner_color != color:
                    valid_place.append(i)
        return valid_place

    # TODO: Complete this method
    def check_color_flip(self, pos, color: Color):
        idx_i, idx_j = self.string2indexes(pos)
        should_be_detected_directions = self.get_around(pos)[1].keys()
        u_all_items = lambda: [f"{pos[0]}{i}" for i in range(idx_i, 0, -1)]
        d_all_items = lambda: [f"{pos[0]}{i}" for i in range(idx_i + 2, 9)]
        l_all_items = lambda: [f"{'abcdefgh'[j]}{pos[1]}" for j in range(idx_j - 1, -1, -1)]
        r_all_items = lambda: [f"{'abcdefgh'[j]}{pos[1]}" for j in range(idx_j + 1, 8)]

        def ul_alL_items():
            ret = []
            i, j = idx_i, idx_j - 1
            while i != -1 and j != -1:
                ret.append(f"{'abcdefgh'[j]}{i}")
                i -= 1
                j -= 1
            return ret

        def ur_alL_items():
            ret = []
            i, j = idx_i, idx_j + 1
            while i != 0 and j != 8:
                ret.append(f"{'abcdefgh'[j]}{i}")
                i -= 1
                j += 1
            return ret

        def dl_all_items():
            ret = []
            i, j = idx_i + 2, idx_j - 1
            while i != 9 and j != -1:
                ret.append(f"{'abcdefgh'[j]}{i}")
                i += 1
                j -= 1
            return ret

        def dr_all_items():
            ret = []
            i, j = idx_i + 2, idx_j + 1
            while i != 9 and j != 8:
                ret.append(f"{'abcdefgh'[j]}{i}")
                i += 1
                j += 1
            return ret

        detect_directions_items = {
            "u": u_all_items,
            "d": d_all_items,
            "l": l_all_items,
            "r": r_all_items,
            "ul": ul_alL_items,
            "ur": ur_alL_items,
            "dl": dl_all_items,
            "dr": dr_all_items
        }

        should_be_flip_pieces = []

        for direction in should_be_detected_directions:
            # 找到边界
            boarder = -1
            for i, item in enumerate(items := detect_directions_items[direction]()):
                cur_item_color = self.get_color_of_index(item)
                if cur_item_color == color:
                    boarder = i
                    break
                if cur_item_color == Color.NotSet:
                    break

            if boarder != -1:
                should_be_flip_pieces += items[:boarder]
            else:
                continue

        print(should_be_flip_pieces, f"should be set to {color}")

        for p in should_be_flip_pieces:
            self.set_piece(p, color)

    def get_around(self, pos: str) -> [dict, dict]:
        row, col = int(pos[1]), pos[0]
        row_idx, col_idx = self.string2indexes(pos)
        direction = {
            "u": True,  # up
            "d": True,  # down
            "l": True,  # left
            "r": True,  # right
        }
        outer_around = {
            "u": lambda: f"{col}{row - 2}",
            "d": lambda: f"{col}{row + 2}",
            "l": lambda: f"{'abcdefgh'[col_idx - 2]}{row}",
            "r": lambda: f"{'abcdefgh'[col_idx + 2]}{row}",

            "ul": lambda: f"{'abcdefgh'[col_idx - 2]}{row - 2}",
            "ur": lambda: f"{'abcdefgh'[col_idx + 2]}{row - 2}",
            "dl": lambda: f"{'abcdefgh'[col_idx - 2]}{row + 2}",
            "dr": lambda: f"{'abcdefgh'[col_idx + 2]}{row + 2}",
        }
        inner_around = {
            "u": lambda: f"{col}{row - 1}",
            "d": lambda: f"{col}{row + 1}",
            "l": lambda: f"{'abcdefgh'[col_idx - 1]}{row}",
            "r": lambda: f"{'abcdefgh'[col_idx + 1]}{row}",

            "ul": lambda: f"{'abcdefgh'[col_idx - 1]}{row - 1}",
            "ur": lambda: f"{'abcdefgh'[col_idx + 1]}{row - 1}",
            "dl": lambda: f"{'abcdefgh'[col_idx - 1]}{row + 1}",
            "dr": lambda: f"{'abcdefgh'[col_idx + 1]}{row + 1}",
        }
        outer, inner = dict(), dict()
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
                outer[k] = outer_around[k]()
                inner[k] = inner_around[k]()

        if direction["u"] and direction["l"]:
            outer["ul"] = outer_around["ul"]()
            inner["ul"] = inner_around["ul"]()

        if direction["u"] and direction["r"]:
            outer["ur"] = outer_around["ur"]()
            inner["ur"] = inner_around["ur"]()

        if direction["d"] and direction["l"]:
            outer["dl"] = outer_around["dl"]()
            inner["dl"] = inner_around["dl"]()

        if direction["d"] and direction["r"]:
            outer["dr"] = outer_around["dr"]()
            inner["dr"] = inner_around["dr"]()

        return [outer, inner]

    def re_rander_ui(self):
        self.ui.TotalCounter.setText(f"Total: {self.pressed_button_cnt}")
        self.ui.BlackPieceCounter.setText(f"Black: {self.count_color(Color.Black)}")
        self.ui.WhitePieceCounter.setText(f"White: {self.count_color(Color.White)}")
        self.ui.GameInfoLabel.setText(f"{self._current_player} Step")

        def rander_nor(pb: QPushButton):
            color_of_bnt = self.get_color_of_index(pb.objectName())
            if color_of_bnt == Color.NotSet:
                pb.setStyleSheet(PIECE_BUTTON_DEFAULT_STYLE_SHEET)
                pb.setText("")
            else:
                pb.setText("W" if color_of_bnt == Color.White else "B")
                pb.setStyleSheet(
                    PIECE_BUTTON_BLACK_STYLE_SHEET
                    if color_of_bnt == Color.Black else
                    PIECE_BUTTON_WHITE_STYLE_SHEET
                )

        def rander_hint(pb: QPushButton):
            pb.setText("V")
            pb.setStyleSheet(PIECE_BUTTON_VALID_PLACE_STYLE_SHEET)

        self.foreach_piece_button(
            rander_nor
        )
        self.foreach_piece_button(
            rander_hint, btn_list=[getattr(self.ui, name) for name in self.get_valid_place(self._current_player)]
        )


if __name__ == "__main__":
    if sys.version_info[1] < 8:
        print("Python version should greater than 3.8")
        exit(-1)
    app = QApplication(sys.argv)
    game = OthelloGame()
    # game.click("d3")
    # game.click("e3")
    # print(game.get_valid_place(Color.Black))
    # game.click("f3")
    # game.click("f4")
    # game.click("c3")
    # a = 0
    game.show()
    sys.exit(app.exec())
