import ply.yacc as yacc
import re
import sys
from blocks import Tag,  Ast, push_ast

from lexer import build_lexer, tokens


def p_asts(p):
    """
    asts : asts ast
         | ast
    """
    p[0] = p[1]
    if len(p) == 3:
        if p[1] != None:
            push_ast(p[1], p[2][0])
        else:
            p[0] = p[2]

def p_ast_vars(p):
    "ast : ASSIGNMENT"
    p[0] = None
    (key,value) = p[1] 
    p.parser.variables[key] = value 

def p_ast_term(p):
    """
    ast : tag
        | literal
    """
    p[0] = [p[1]]


def p_indent_term(p):
    """
    indent : INDENT
            | NEWLINE
    """
    p[0] = p[1].count(" ")


def p_tag_term(p):
    """
    tag : TAG
        | indent TAG
    """
    if len(p) == 2:
        p[0] = Ast(0, Tag(p[1], {}), [])
    else:
        p[0] = Ast(p[1], Tag(p[2], {}), [])


def p_tag_id(p):
    "tag : tag ID"
    p[0] = p[1]
    p[0].value.attrs["id"] = p[2]


def p_tag_attrs(p):
    "tag : tag ATTRIBUTES"
    p[0] = p[1]
    p[0].value.attrs.update(p[2])


def p_tag_inline_text(p):
    "tag : tag INLINE_TEXT"
    p[0] = p[1]
    p[0].value.inline_text = p[2]


def p_literal_piped_text(p):
    """
    literal : PIPED_TEXT
            | indent PIPED_TEXT
    """
    if len(p) == 2:
        p[0] = Ast(0, 0, [])
    else:
        p[0] = Ast(p[1], p[2], [])


def p_literal_term(p):
    "literal : LITERAL"
    p[0] = Ast(0, p[1], [])

def p_literal_comment(p):
    "literal : COMMENT"
    p[0] = Ast(0, f"<!-- {p[1]} -->", [])


def p_dotblock_ind(p):
    "dotblock : indent DOT_BLOCK"
    p[0] = p[2]


def p_dotblocks_term(p):
    "dotblocks : dotblock"
    p[0] = p[1]


def p_dot_blocks(p):
    "dotblocks : dotblocks dotblock"
    p[0] = p[1] + "\n" + p[2]


def p_literal_block(p):
    "literal : DOT dotblocks"
    p[0] = Ast(0,  p[2], [])


def p_literal_block_ind(p):
    "literal : indent DOT dotblocks"
    p[0] = Ast(p[1],  p[3], [])


def p_tag_dot(p):
    "tag : tag DOT dotblocks"
    p[0] = p[1]
    p[0].value.inline_text = p[3]
    
    

def p_error(p):
    print(f"Syntax error in input! {p}")


def build_parser():
    lexer = build_lexer()
    parser = yacc.yacc()
    parser.variables = {}
    return parser


parser = build_parser()


def run_parser_tests():
    tests = []
    tests.append({
        "input": "div",
        "output": [Ast(0, Tag('div', {}), [])]
    })
    tests.append({
        "input": "div\ndiv",
        "output": [Ast(0, Tag('div', {}), []), Ast(0, Tag('div', {}), [])]
    })
    tests.append({
        "input": "div\n p",
        "output": [Ast(0, Tag('div', {}), [Ast(1, Tag('p', {}), [])])]
    })
    tests.append({
        "input": "div#hello(x='1')",
        "output": [Ast(0, Tag('div', {'id': 'hello', 'x': '1'}), [])]
    })
    tests.append({
        "input": "div#hello foo bar",
        "output": [Ast(0, Tag('div', {'id': 'hello'}, 'foo bar'), [])]
    })
    tests.append({
        "input": "foo\n| bar",
        "output": [Ast(0, Tag('foo', {}, None), []), Ast(0, 'bar', [])]
    })
    tests.append({
        "input": "foo\n  | bar",
        "output": [Ast(0, Tag('foo', {}, None), [Ast(2, 'bar', [])])]
    })
    tests.append({
        "input": "<html>",
        "output": [Ast(0, '<html>', [])]
    })
    tests.append({
        "input": ".\n is lit",
        "output": [Ast(0, 'is lit', [])]
    })
    tests.append({
        "input": " .\n  is lit\n  more lit",
        "output": [Ast(1, 'is lit\nmore lit', [])]
    })
    tests.append({
        "input": "script.\n if(true) big true",
        "output": [Ast(0, Tag('script', {}, 'if(true) big true'), [])]
    })
    tests.append({
        "input": "//var title = 3;\nvar title = 3;",
        "output": [Ast(0,'<!-- var title = 3; -->',[]), Ast(0,Tag('var', {}, 'title = 3;'),[])]
    })
    
    for test in tests:
        parser = build_parser()
        output = parser.parse(test["input"])
        if output != test["output"]:
            print(f"Failed test {repr(test['input'])}")
            print(f"Expected: {repr(test['output'])}")
            print(f"Obtained: {repr(output)}")
            sys.exit(1)
        else:
            print(f"Passed test {repr(test['input'])}")