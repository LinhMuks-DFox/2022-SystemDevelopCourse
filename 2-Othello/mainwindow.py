from enum import Enum
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from WindowsGUI import Ui_MainWindow
import PySide6
import os

# Configs
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class Color(Enum):
    Black = 0
    White = 1
    NotSetted = 2


class OthelloGame:
    def __init__(self):
        self.check_board = [[None for _ in range(8)] for _ in range(8)]

    def change_piece(self, position: str, color: Color) -> bool:
        i, j = self._get_indexes(position)
        if self.check_board[i][j] is not None:
            return False
        else:
            self.check_board[i][j] = color
            return True

    def get_color(self, pos: str) -> Color:
        i, j = self._get_indexes(pos)
        return self.check_board[i][j]

    @staticmethod
    def _get_indexes(position: str):
        if len(position) > 2:
            raise ValueError(f"Argument {position} is invalid.")
        return int(position[1]), "abcdefg".index(position[0])  # (row, col)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.othello = OthelloGame()
        self.piece_buttons = [
            getattr(self.ui, attrname) for attrname in [
                f"{alpha}{num}" for alpha in "abcdefgh" for num in range(1, 9)
            ]
        ]
        # set piece_buttons's click function
        for pb in self.piece_buttons:
            pb.clicked.connect(
                (lambda _=None, pb=pb: self.click(
                    pb.objectName()))
            )
        self.ui.reset_button.clicked.connect(self.reset_ui)

    def reset_ui(self):
        self.ui.GameInfoLabel.setText("Reset game!")
        print("reset_button pressed.")

    def click(self, pos: str):
        self.othello.change_piece(pos, Color.Black)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow().show()
    sys.exit(app.exec())
