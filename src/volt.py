################################################
#                 CONSTANTS                    #
################################################

DIGITS = '0123456789'

################################################
#                   TOKENS                     #
################################################

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MULTIPLY = 'MULTIPLY'
TT_DIVIDE = 'DIVIDE'
TT_LPAREN = '('
TT_RPAREN = ')'


class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        if self.value : return f'{self.type}:{self.value}'
        return f'{self.type}'
        

################################################
#                    LEXER                     #
################################################

class Lexer:
    def __init__(self, text : str):
        self.text = text
        self.position = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.position += 1
        self.current_char = self.text[self.position] if self.position < len(self.text) else None

    def tokenize(self):
        tokens = []

        while self.current_char:
            if self.current_char in ' \t':
                self.advance()

            if self.current_char in DIGITS:
                self.advance()
                tokens.append(Token(TT_INT))
            
            if self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            
            if self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()

            if self.current_char == '*':
                tokens.append(Token(TT_MULTIPLY))
                self.advance()

            if self.current_char == '/':
                tokens.append(Token(TT_DIVIDE))
                self.advance()

            if self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()

            if self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
        
        return tokens

    def create_number(self):
        self.advance()


################################################
#                     RUN                      #
################################################

def run(text : str):
    
    # Lexing

    lexer = Lexer(text)
    tokens = lexer.tokenize()
    print(tokens)

