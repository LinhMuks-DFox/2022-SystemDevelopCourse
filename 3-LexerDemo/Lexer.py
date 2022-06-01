# Author: Mux
import enum
import re
from typing import NamedTuple
from configs import *
from unicodedata import east_asian_width

if DETECT_ENCODE:
    try:
        import chardet
    except ImportError as ierr:
        print("Cannnot find pacakge chardet, install it before use this script")
        print("Or you can disable Text encode detect feature, change the value in configs.py")
        print("configs.DETECT_ENCODE = False")
        exit(-1)

class TokenType(enum.Enum):
    string = 0
    integer = 1
    new_line = 2


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


class LexerDemo():

    def lex_up(self, input_content: str):
        token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
            ('NEWLINE',  r'[\n\r]'),           # Line endings
            ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
            ('STRING', r"[a-zA-Z0-9]*"),
            ('MISMATCH', r".")
        ]
        tok_regex = '|'.join('(?P<%s>%s)' %
                             pair for pair in token_specification)
        line_num = 1
        line_start = 0
        for mo in re.finditer(tok_regex, input_content):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - line_start
            if kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)
            elif kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
            elif kind == 'MISMATCH':
                if east_asian_width(value) in "FW":
                    kind = "FULLWIDTH CHARACTER"
            yield Token(kind, value, line_num, column)


if __name__ == "__main__":

    if INPUT_MODE == "FILE":
        if DETECT_ENCODE:
            print(f"Mode: FILE, File encode: {chardet.detect((content:=open(INPUT_HANDLE, 'r').read()))}")
        for t in LexerDemo().lex_up(content):
            print(t)

    elif INPUT_MODE == "STDIO":
        print("Mode: STDIO, please input:")
        inputs = input()
        if DETECT_ENCODE:
            print(f"Encode of inputs: {chardet.detect(inputs)}")
        for t in LexerDemo().lex_up(inputs):
            print(t)
