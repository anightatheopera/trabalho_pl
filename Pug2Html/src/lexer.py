import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = (
    "IDENTIFIER",
    "WHITESPACE",
    "NONWHITESPACE",
)

t_IDENTIFIER = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_WHITESPACE = r"[ \t]+"
t_NONWHITESPACE = r"[^ \t\r\n]+"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    sys.exit(1)


def p_start(p):
    "start : inlinetag"
    p[0] = p[1]

"""
tag = IDENTIFIER
"""
def p_identifier_term(p):
    "tag : IDENTIFIER"
    p[0] = p[1]

"""
word = IDENTIFIER | NONWHITESPACE
"""
def p_word_ident(p):
    """word : IDENTIFIER
            | NONWHITESPACE"""
    p[0] = p[1]


"""
content = word
        | content word
        | content NONWHITESPACE
"""

def p_content_term(p):
    "content : word"
    p[0] = p[1]

def p_content_ws(p):
    "content : content WHITESPACE"
    p[0] = p[1] + p[2]

def p_content_nws(p):
    "content : content word"
    p[0] = p[1] + p[2]

"""
inlinetag = tag WHITESPACE content
"""

def p_inlinetag_term(p):
    "inlinetag : tag WHITESPACE content"
    p[0] = { "tag": p[1], "content": p[3] }


def p_error(p):
    if p:
        print(f"Syntax error at token '{p}'")
    else:
        print("Syntax error at end of input")

lexer = lex.lex()
parser = yacc.yacc()

def lexer_test():
    tests = []
    tests.append({
        "input": "p This is plain old <em>text</em> content.",
        "output": ['p', ' ', 'This', ' ', 'is', ' ', 'plain', ' ', 'old', ' ', '<em>text</em>', ' ', 'content', '.']
    })

    for test in tests:
        lexer.input(test["input"])
        output = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            output.append(tok.value)
        if output != test["output"]:
            print("Failed test: %s" % test["input"])
            print("Expected: %s" % test["output"])
            print("Got: %s" % output)
            sys.exit(1)
        else:
            print("Passed test: %s" % test["input"])

def parser_test():
    tests = []
    tests.append({
        "input": "p This is plain old <em>text</em> content.",
        "output": {'tag': 'p', 'content': 'This is plain old <em>text</em> content.'}
    })

    for test in tests:
        lexer.input(test["input"])
        output = parser.parse(test["input"])
        if output != test["output"]:
            print("Failed test: %s" % test["input"])
            print("Expected: %s" % test["output"])
            print("Got: %s" % output)
            lexer.input(test["input"])
            for token in lexer:
                print(token, end=" ")
            print()
            sys.exit(1)
        else:
            print("Passed test: %s" % test["input"])

lexer_test()
parser_test()