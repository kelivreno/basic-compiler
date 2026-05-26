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
        # Check the first character of this token to see if we can decide what it is.
        # If it is a mulitple character operator (e.g., !=), number, identifier, or keyword the we will prcoess the rest of it.
        if self.curChar == '+':
            pass
        elif self.curChar == '-':
            pass
        elif self.curChar == '*':
            pass
        elif self.curChar == '/':
            pass
        elif self.curChar == '\n':
            pass
        elif self.curChar == '\0':
            pass
        else:
            # Uknown token!
            pass

        self.nextChar()