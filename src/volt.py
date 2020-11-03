######################################
# VOLT
######################################

from enum import Enum
from collections import defaultdict
from os import error
from typing import Dict, List
import sys

TT = Enum("TT", "INT STR PLUS MINUS MUL DIV LPAREN RPAREN")

class Token:
    def __init__(self, line, column, kind: TT, data):
        self.kind = kind 
        self.data = data
        self.line = line
        self.column = column

class Lexer:
    src = []
    idx = 0
    kws = defaultdict(lambda: TT.IDENT)
    
    def __init__(self, src):
        self.src = src 
        self.kws['('] = TT.LPAREN 
        self.kws[')'] = TT.RPAREN
        self.kws['+'] = TT.PLUS
        self.kws['-'] = TT.MINUS
        self.kws['*'] = TT.MUL
        self.kws['/'] = TT.DIV

        self.row = 1
        self.column = 1

    def lex_num(self):
        match = ""
        while self.idx < len(self.src) and self.src[self.idx].isdigit():
            match += self.src[self.idx]
            self.eat()
        return Token(self.row, self.column, TT.INT, int(match))

    def current_char_is_valid_in_an_identifier(self):
        current = self.src[self.idx]
        return current.isidentifier()

    def lex_ident(self):
        match = ""
        while self.idx < len(self.src) and self.current_char_is_valid_in_an_identifier():
            match += self.src[self.idx]
            self.eat()
        
        kind = self.kws[match]
        return Token(self.row, self.column, kind, match)

    def consume_whitespace(self):
        while self.idx < len(self.src) and self.src[self.idx].isspace():
            self.eat()

    def __iter__(self):
        return self

    # RECOGNIZE NEXT TOKEN
    def __next__(self):
        if self.idx >= len(self.src):
            raise StopIteration
        self.consume_whitespace()
        ch = self.src[self.idx]
        if ch.isalpha():
            return self.lex_ident()
        elif ch.isdigit():
            return self.lex_num()
        elif ch == '"':
            return self.lex_string_literal()
        elif ch == "'":
            return self.lex_single_quote_literal()
        else:
            kind = self.kws[ch]
            self.eat()
            if kind == TT.IDENT:
                kind = TT.UNKNOWN
            return Token(self.row, self.column, kind, ch)

    # FOR EVALUATING STRINGS
    def lex_string_literal(self):
        assert(self.src[self.idx] == '"')
        self.eat()

        literal = ""
        while self.idx < len(self.src) and self.src[self.idx] != '"':
            literal += self.src[self.idx]
            self.eat()
        
        if self.idx >= len(self.src):
            print("Missing end of string delimiter!")
            return Token(self.row, self.column, TT.UNKNOWN, literal)
        assert(self.src[self.idx] == '"')
        self.eat()
        return Token(self.row, self.column, TT.STRING, literal)
    
    def lex_single_quote_literal(self):
        assert(self.src[self.idx] == "'")
        self.eat()

        literal = ""
        while self.idx < len(self.src) and self.src[self.idx] != "'":
            literal += self.src[self.idx]
            self.eat()
        
        if self.idx >= len(self.src):
            print("Missing end of string delimiter!")
            return Token(self.row, self.column, TT.UNKNOWN, literal)
        assert(self.src[self.idx] == "'")
        self.eat()
        return Token(self.row, self.column, TT.STRING, literal)

    def eat(self):
        if self.src[self.idx] == "\n":
            self.row += 1
            self.column = 1
        else:
            self.column += 1
        self.idx += 1
