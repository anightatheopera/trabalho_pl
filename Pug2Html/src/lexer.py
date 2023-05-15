import ply.lex as lex
import sys
import re

tokens = (
    "TAG",
    "ID",
    "ATTRIBUTES",
    "INDENT",
    "NEWLINE",
    "INLINE_TEXT",
    "PIPED_TEXT",
    "LITERAL",
    "DOT",
    "DOT_BLOCK",
    "COMMENT",
    "STRING",
    "BOOL",
    "NUM",
    "VAR_KEY",
    "VAR_VALUE",
    "ASSIGNMENT",
    "MIXIN",
    
)

states = (
    ("insidedot", "exclusive"),
)


def t_ANY_COMMENT(t):
    r"^//.*\n"


def t_TAG(t):
    r"\w+"
    return t


r_string = r'"[^"]*"'
r_bool = r"(true|false)"
r_num = r'[-+]?\d*\.?\d+([eE][-+]?\d+)?'
r_var_value = rf"({r_string}|{r_bool}|{r_num})"
r_var_key = r"\w+"
r_assignment = rf"^\s*-\s+var\s+{r_var_key}\s*=\s*{r_var_value}\s*;[ \t]*"
r_attribute = r"(\w+\s*=\s*'[^\n\\]*')"
r_attribute_comma = r"(\s*([\s,\n])\s*)"
r_attributes = rf"\(\s*{r_attribute}?({r_attribute_comma}{r_attribute})*?\s*\)"




@lex.TOKEN(r_assignment)
def t_ASSIGNMENT(t):
    index = t.value.find("var")
    index = index + 3
    t.value = t.value.strip()
    t.value = t.value[index:-1]
    foo = t.value.split("=")
    key = foo[0].strip()
    value = foo[1].strip()
    if value[0] == "'" or value[0] == '"':
        value = value[1:-1]
    t.value = (key, value)
    return t
 
    
@lex.TOKEN(r_attributes)
def t_ATTRIBUTES(t):
    attrs = re.sub("(\s|,)+", " ", t.value[1:-1].strip())
    attrs = re.sub("\s*=\s*", "=", attrs)
    t.value = {}
    if attrs != "":
        for attr in attrs.split(" "):
            [k, v] = attr.strip().split("=")
            t.value[k.strip()] = v.strip()[1:-1]
    return t


def t_ID(t):
    r"\#[\w-]+"
    t.value = t.value[1:]
    return t


def t_LITERAL(t):
    r"\<.*$"
    return t


def t_DOT(t):
    r"\."
    t.lexer.dot_indent = t.lexer.indent
    t.lexer.begin("insidedot")
    return t


def t_ANY_INDENT(t):
    r"(\n|^)[ ]+"
    t.lexer.indent = t.value.count(" ")
    if t.lexer.dot_indent and t.lexer.indent <= t.lexer.dot_indent:
        t.lexer.dot_indent = None
        t.lexer.begin("INITIAL")
    return t


def t_ANY_NEWLINE(t):
    r"\s*\n"
    t.lexer.indent = 0
    t.lexer.dot_indent = None
    t.lexer.begin("INITIAL")
    return t


def t_PIPED_TEXT(t):
    r"\|[^\n]+"
    if t.value[1] == " ":
        t.value = t.value[2:]
    else:
        t.value = t.value[1:]
    return t


def t_INLINE_TEXT(t):
    r" [^\n]+"
    t.value = t.value[1:]
    return t


def t_insidedot_DOT_BLOCK(t):
    r" [^\n]+"
    return t


def t_ANY_error(t):
    print(f"Illegal character `{t.value[0]}`")
    print(f"Lexer state `{t}`")
    sys.exit(1)

def build_lexer():
    lexer = lex.lex()
    lexer.dot_indent = None
    lexer.indent = 0
    return lexer


lexer = build_lexer()


def run_lexer_tests():
    tests = []
    tests.append({
        "input": "div",
        "output": [('TAG', 'div')]
    })
    tests.append({
        "input": "div() foo",
        "output": [('TAG', 'div'), ('ATTRIBUTES', {}), ('INLINE_TEXT', 'foo')]
    })
    tests.append({
        "input": "div(  x = '1' ) foo",
        "output": [('TAG', 'div'), ('ATTRIBUTES', {'x': '1'}), ('INLINE_TEXT', 'foo')]
    })
    tests.append({
        "input": "div#hello(x='1') foo",
        "output": [('TAG', 'div'), ('ID', 'hello'), ('ATTRIBUTES', {'x': '1'}), ('INLINE_TEXT', 'foo')]
    })
    tests.append({
        "input": "div(x='1' ,   y = '2') foo",
        "output": [('TAG', 'div'), ('ATTRIBUTES', {'x': '1', 'y': '2'}), ('INLINE_TEXT', 'foo')]
    })
    tests.append({
        "input": "div This is inline text.",
        "output": [('TAG', 'div'), ('INLINE_TEXT', 'This is inline text.')]
    })
    tests.append({
        "input": "div\n | This is piped text\n |More",
        "output": [('TAG', 'div'), ('INDENT', '\n '), ('PIPED_TEXT', 'This is piped text'), ('INDENT', '\n '), ('PIPED_TEXT', 'More')]
    })
    tests.append({
        "input": "<This> is a literal line </This>",
        "output": [('LITERAL', '<This> is a literal line </This>')]
    })
    tests.append({
        "input": "script.\n inside\n inside\noutside",
        "output": [('TAG', 'script'), ('DOT', '.'), ('INDENT', '\n '), ('DOT_BLOCK', 'inside'), ('INDENT', '\n '), ('DOT_BLOCK', 'inside'), ('NEWLINE', '\n'), ('TAG', 'outside')]
    })
    tests.append({
        "input": "- var title = 3;",
        "output": [('ASSIGNMENT', ('title', '3'))]
    })
    tests.append({
        "input": "mixing list\n\tul\n\t\tli foo\n\t\tli bar\n\t\tli baz\n+list",
        "output": [('INLINE_TEXT', 'mixing list'), ('INDENT', '\n\t'), ('TAG', 'ul'), ('INDENT', '\n\t\t'), ('TAG', 'li'), ('INLINE_TEXT', 'foo'), ('INDENT', '\n\t\t'), ('TAG', 'li'), ('INLINE_TEXT', 'bar'), ('INDENT', '\n\t\t'), ('TAG', 'li'), ('INLINE_TEXT', 'baz'), ('NEWLINE', '\n'), ('INLINE_TEXT', '+list')]
    })


    for test in tests:
        lexer = build_lexer()
        lexer.input(test["input"])

        tokens = []
        for tok in lexer:
            tokens.append((tok.type, tok.value))

        if tokens != test["output"]:
            print(f"Failed test {repr(test['input'])}")
            print(f"Expected: `{test['output']}`")
            print(f"Obtained: `{tokens}`")
            sys.exit(1)
        else:
            print(f"Passed test {repr(test['input'])}")
