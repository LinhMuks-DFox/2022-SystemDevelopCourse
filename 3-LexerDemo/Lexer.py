# Author: Mux
import dataclasses
import enum
from secrets import token_bytes

from configs import *


class TokenType(enum.Enum):
    string = 0
    integer = 1
    new_line = 2


@dataclasses.dataclass
class Token:
    content: str
    token_type: TokenType
    encode: str

    def __str__(self) -> str:
        return f"Token Object: '{content}‘, {token_type}, {encode}"

    __repr__ = __str__


class LexerDemo():

    def __init__(self) -> None:
        pass

    def lex_up(self, input_content: str) -> None:
        pass


if __name__ == "__main__":

    if INPUT_MODE == "FILE":
        LexerDemo(open(INPUT_HANDLE, "r").read())

    elif INPUT_MODE == "STDIO":
        inputs = input()
        LexerDemo(inputs)
