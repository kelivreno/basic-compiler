import enum


class Lexer:
    
    def __init__(self, source):
        self.source = source + '\n' # Source code to lex as a string. Append a new line to simplify lexing/parsing the last token/statement.
        self.curChar = '' # Current character in the string.
        self.curPos = -1 # Current position in the string.
        self.nextChar()
    # Process the next character
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]
    # Return the lookahead character.
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]
    # Invalid token found, print error message
    def abort(self,message):
        pass
    # Skip whitespace except newlines
    # to indicate the end of a statement
    def skipWhitespace(self):
        pass

    # Skip comments in the code
    def skipComment(self):
        pass
    
    # Return the next token
    def getToken(self):
        token = None
        # Check the first character of this token to see if we can decide what it is.
        # If it is a mulitple character operator (e.g., !=), number, identifier, or keyword the we will prcoess the rest of it.
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS )
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS )
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK )
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH )
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        else:
            # Uknown token!
            pass

        self.nextChar()
        return token

class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    #KEYWORDS:
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 105
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    #Operators:
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
