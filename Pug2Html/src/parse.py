import ply.yacc as yacc
import sys
from blocks import Tag, Literal, BLOCK_TAG

from lexer import build_lexer, tokens


def p_blocks_term(p):
    """
    block : tag
          | literal
    """
    p[0] = p[1]


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
        p[0] = Tag(p[1], 0, {}, [])
    else:
        p[0] = Tag(p[2], p[1], {}, [])


def p_tag_id(p):
    "tag : tag ID"
    p[0] = p[1]
    p[0].attrs["id"] = p[2]


def p_tag_attrs(p):
    "tag : tag ATTRIBUTES"
    p[0] = p[1]
    p[0].attrs.update(p[2])


def p_tag_inline_text(p):
    "tag : tag INLINE_TEXT"
    p[0] = p[1]
    p[0].children.append(p[2])


def p_literal_piped_text(p):
    """
    literal : PIPED_TEXT
            | indent PIPED_TEXT
    """
    if len(p) == 2:
        p[0] = Literal(p[1], 0)
    else:
        p[0] = Literal(p[2], p[1])


def p_literal_term(p):
    "literal : LITERAL"
    p[0] = Literal(p[1], 0)


def p_dot_blocks_term(p):
    """
    dot_blocks : indent DOT_BLOCK
               | dot_blocks INDENT DOT_BLOCK
    """
    if len(p) == 3:
        p[0] = Literal(p[2], p[1])
    else:
        p[0] = Literal(p[1].value + p[2] + p[3], p[1].indent)


def p_literal_block(p):
    """
    literal : DOT dot_blocks
            | indent DOT dot_blocks
    """
    if len(p) == 3:
        p[0] = Literal(p[2].value, 0)
    else:
        # TODO: cleanup indentation for p[3]
        p[0] = Literal(p[3].value, p[1])


def p_tag_dot(p):
    "tag : tag DOT dot_blocks"
    p[0] = p[1]
    p[0].children.append(p[3])


def p_error(p):
    print("Syntax error in input!")


def build_parser():
    lexer = build_lexer()
    parser = yacc.yacc()
    parser.indents = []
    return parser


parser = build_parser()


def run_parser_tests():
    tests = []
    tests.append({
        "input": "div",
        "output": Tag('div', 0, {}, [])
    })
    tests.append({
        "input": "div#hello(x='1')",
        "output": Tag('div', 0, {'id': 'hello', 'x': '1'}, [])
    })
    tests.append({
        "input": "div#hello foo bar",
        "output": Tag('div', 0, {'id': 'hello'}, ['foo bar'])
    })
    tests.append({
        "input": "| bar",
        "output": Literal('bar', 0)
    })
    tests.append({
        "input": "<html>",
        "output": Literal('<html>', 0)
    })
    tests.append({
        "input": ".\n is lit",
        "output": Literal('is lit', 0)
    })
    tests.append({
        "input": ".\n is lit\n more lit",
        "output": Literal('is lit\n more lit', 0)
    })
    tests.append({
        "input": "script.\n if(true) big true",
        "output": Tag('script', 0, {}, [Literal('if(true) big true', 1)])
    })

    for test in tests:
        parser = build_parser()
        output = parser.parse(test["input"])
        if output != test["output"]:
            print(f"Failed test {repr(test['input'])}")
            print(f"Expected: `{test['output']}`")
            print(f"Obtained: `{output}`")
            sys.exit(1)
        else:
            print(f"Passed test {repr(test['input'])}")
