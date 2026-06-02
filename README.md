# A Tiny Compiler

A simple compiler written in Python that translates a custom language into executable code. Supports basic programming language features.

## Features

- Numerical variables
- Basic arithmetic
- If statements
- While loops
- Print text and numbers
- User input
- Labels and goto statements
- Comments

> **Note:** String handling in `PRINT` and full `LABEL`/`GOTO` support are partially implemented at the lexer level and are still in progress.

## Requirements

- Python 3.6 or higher
- No third-party dependencies

## Usage

```bash
python compiler.py <source_file>
```

Example:

```bash
python compiler.py program.teeny
```

## Compilation Process

```
Source Code -> [LEXER] -> Tokens -> [PARSER] -> Program Tree -> [EMITTER] -> Compiled Code
```

## Example Program

```
# Print numbers from 1 to 5
LET i = 1
WHILE i <= 5 REPEAT
    PRINT i
    LET i = i + 1
ENDWHILE
```

## Known Limitations

- Only numeric (float) variables are supported; no string variables
- No functions or procedures
- `LABEL` and `GOTO` are tokenized but not yet fully implemented in the parser/emitter
- Strings are only supported as arguments to `PRINT`, not as variable values

## Project Structure

```
compiler.py   # Lexer, Token, and TokenType definitions
```

Parser and Emitter stages are not yet implemented.

## License

MIT
