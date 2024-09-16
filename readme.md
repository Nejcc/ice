run: 
```
python -m src.cli run examples/hello_world.ice
```

Tree

```
ice-language/
├── src/
│   ├── __init__.py            # Makes 'src' a Python package
│   ├── cli.py                 # CLI tool for handling commands
│   ├── lexer.py               # Lexer: Tokenizes the source code
│   ├── parser.py              # Parser: Creates AST from tokens
│   ├── interpreter.py         # Interpreter: Executes the AST
│   ├── compiler.py            # Compiler: Compiles the AST into machine code or intermediate representation
│   ├── runtime/
│   │   └── runtime.py         # Handles memory management, function calls, etc.
│   └── stdlib/
│       ├── io.ice             # IO functions
│       ├── math.ice           # Math functions
│       └── string.ice         # String manipulation functions
├── examples/
│   ├── hello_world.ice        # Example ICE program
│   ├── test.ice               # Another example program for testing
│   └── more_examples/
├── tests/
│   ├── lexer_test.py          # Tests for lexer
│   ├── parser_test.py         # Tests for parser
│   ├── interpreter_test.py    # Tests for interpreter
│   └── compiler_test.py       # Tests for compiler
├── build/
│   ├── output/                # Compiled output files
│   └── cache/                 # Cache for intermediate files or compilation data
├── docs/
│   ├── language_spec.md       # Language specifications
│   └── user_guide.md          # User guide for ICE language
└── README.md                  # Readme file
```
