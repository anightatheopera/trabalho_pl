import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = (
    "START_LEFT_ANGLE_BRACKET",
    "IDENTIFIER",
    "SPACE",
    "WHITESPACE",
    "DOT",
    "NONWHITESPACE",
    "PIPE",
    "NEWLINE"
)

def t_DOT(t):
    r'\.'
    return t

def t_START_LEFT_ANGLE_BRACKET(t):
    r"^<"
    return t

def t_PIPE(t):
    r"^[ \t]*\|"
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_IDENTIFIER = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_SPACE = r"[ ]"
t_WHITESPACE = r"[\t\r]"
t_NONWHITESPACE = r"[^\s]+"



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    sys.exit(1)


def p_start(p):
    """start : inline
             | literal
             | piped"""
    p[0] = p[1]

"""
literal = START_LEFT_ANGLE_BRACKET content
"""

def p_literal_term(p):
    "literal : START_LEFT_ANGLE_BRACKET content"
    p[0] = p[1] + p[2]

"""
tag = IDENTIFIER
"""

def p_identifier_term(p):
    "tag : IDENTIFIER"
    p[0] = p[1]

"""
ws = SPACE
wss = ws | wss ws
"""

def p_ws_term(p):
    """ws : SPACE
          | WHITESPACE"""
    p[0] = p[1]

def p_wss_term(p):
    "wss : ws"
    p[0] = p[1]

def p_wss_ws(p):
    "wss : wss ws"
    p[0] = p[1] + p[2]

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
        | content wss
"""

def p_content_term(p):
    "content : word"
    p[0] = p[1]

def p_content_cont(p):
    """content : content wss
               | content word"""
    p[0] = p[1] + p[2]


"""
inline = tag ws content | tag SPACE NEWLINE piped
"""

def p_inline_term(p):
    "inline : tag ws content"
    p[0] = { "ident": 0, "tag": p[1], "content": p[3] }

def p_inline_ident(p):
    "inline : ws inline"
    p[0] = p[2]
    p[0]["ident"] += 1
    
"""
piped = PIPE content | PIPE wss content
"""    

def p_piped_term(p):
    "piped : PIPE content"
    p[0] = { "indent": len(p[1]), "content": p[2] }

def p_piped_wss(p):
    "piped : PIPE wss content"
    p[0] = { "indent": len(p[1]), "content": p[3] }

def p_piped_pipe(p):
    "piped : piped NEWLINE PIPE content"
    assert p[1]["indent"] == len(p[3]), "unexpected indentation level"
    p[0] = {"indent": len(p[3]), "content": f"{p[1]['content']}\n{p[4]}"}


"""
block_tag = tag DOT NEWLINE wss content | tag NEWLINE wss content NEWLINE wss content
"""

def p_block_tag_term(p):
    "block_tag : tag DOT NEWLINE wss content"
    p[0] = {"tag": p[1], "indent": len(p[4]) , "content": p[5]}

def p_block_tag_term2(p):
    "block_tag : tag NEWLINE wss content NEWLINE wss content"
    p[0] = {"tag": p[1], "indent": len(p[6]) , "content": p[4], "inside_content": p[7]}

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
        "input": " p This is plain old <em>text</em> content.",
        "output": [' ','p', ' ', 'This', ' ', 'is', ' ', 'plain', ' ', 'old', ' ', '<em>text</em>', ' ', 'content', '.']
    })
    tests.append({
        "input": "  h1 indented",
        "output": [' ', ' ', 'h1', ' ', 'indented']
    })
    tests.append({
        "input": "script.\n conteudo em plain text",
        "output": ['script', '.', '\n', ' ', 'conteudo', ' ', 'em', ' ', 'plain', ' ', 'text']
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
        "input": "p This is plain old <em>text</em>  content.",
        "output": {'ident': 0, 'tag': 'p', 'content': 'This is plain old <em>text</em>  content.'}
    })
    tests.append({
        "input": "  h1 indented",
        "output": {'ident': 2, 'tag': 'h1', 'content': 'indented'}
    })
    tests.append({
        "input": "<html>",
        "output": "<html>"
    })
    for test in tests:
        lexer.input(test["input"])
        output = parser.parse(test["input"])
        if output != test["output"]:
            print("Failed test: %s" % test["input"])
            print("Expected: %s" % test["output"])
            print("Got:      %s" % output)
            lexer.input(test["input"])
            # for token in lexer:
            #     print(token, end=" ")
            # print()
            sys.exit(1)
        else:
            print("Passed test: %s" % test["input"])

lexer_test()
parser_test()