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
    "CLASS",
    "TITLE",
    "DOCTYPE",
    "INCLUDE",
    "CASE",
    "WHEN",
    "DEFAULT",
    "EACH",
    "FOR",
    "IF",
    "ELSE"
)


specific_tokens = ["if", "else","title", "each", "for", "include", "case", "default", "when", "title", "doctype"]

negative_lookahead = rf"({'|'.join([f'(?!{token})' for token in specific_tokens])})"

states = (
    ("insidedot", "exclusive"),
)

def t_ANY_COMMENT(t):
    r"//.*((?=[\n])|$)"
    t.value = t.value[2:]
    return t


def t_FOR(t):
    r"for\s+[^\n]+"
    t.value = t.value[4:].strip()
    return t

def t_EACH(t):
    r"each\s+[\w-]+\s+in\s+.*"
    t.value = t.value[5:].strip()
    return t

def t_CASE(t):
    r"case\s+[\w-]+"
    t.value = t.value[5:].strip()
    return t

def t_WHEN(t):
    r"when\s+[\w-]+"
    t.value = t.value[5:].strip()
    return t

def t_DEFAULT(t):
    r"default"
    return t

def t_CLASS(t):
    r"(?<=\w)\.[\w-]+"
    t.value = t.value[1:]
    return t

def t_DOCTYPE(t):
    r"doctype\s+[^\n]+"
    t.value = re.sub(r"doctype\s+", "", t.value)
    return t

def t_INCLUDE(t):
    r"include\s+[^\n]+"
    t.value = re.sub(r"include\s+", "", t.value)
    return t

def t_TITLE(t):
    r"title\s*=\s*\"?[^\n\"]*\"?"
    t.value = re.sub(r"title\s*=\s*", "", t.value)
    return t

def t_IF(t):
    r"if"
    return t

def t_ELSE(t):
    r"else"
    return t

r_tag = rf"({negative_lookahead} \w+)"
@lex.TOKEN(r_tag)
def t_TAG(t):
    return t



r_string = r'"[^"]*"'
r_bool = r"(true|false)"
r_num = r'[-+]?\d*\.?\d+([eE][-+]?\d+)?'
r_var_value = rf"({r_string}|{r_bool}|{r_num})"
r_var_key = r"\w+"
r_assignment = rf"^\s*-\s+var\s+{r_var_key}\s*=\s*{r_var_value}\s*;[ \t]*"
r_attribute = r"(\w+\s*=\s*((\"|')|{)[^\n\\]*(}|(\"|')))"
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
    attrs = re.sub(r"(?<!{)(\s|,)+(?![^{}]*})", " ", t.value[1:-1].strip())
    attrs = re.sub(r"\s*=\s*", "=", attrs)
    t.value = {}
    if attrs != "":
        if attrs.startswith("style"):
            [k, v] = attrs.split("=")
            t.value[k.strip()] = v.strip()
        else:
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
    r"\.(?!\w)"
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
    if t.value[0] == " ":
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
        "input": "#container.col\n  p This is inline text.",
        "output": [('ID', 'container'), ('CLASS', 'col'), ('INDENT', '\n  '), ('TAG', 'p'), ('INLINE_TEXT', 'This is inline text.')]
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
        "input": "script(type='text/javascript').\n inside\n inside\noutside",
        "output": [('TAG', 'script'), ('ATTRIBUTES', {'type': 'text/javascript'}), ('DOT', '.'), ('INDENT', '\n '), ('DOT_BLOCK', 'inside'), ('INDENT', '\n '), ('DOT_BLOCK', 'inside'), ('NEWLINE', '\n'), ('TAG', 'outside')]
    })
    tests.append({
        "input": "title= Stuff",
        "output": [('TITLE', 'Stuff')]
    })
    tests.append({
        "input": "if youAreUsingPug\n  p You are amazing\nelse\n  p Get on it!",
        "output": [('IF','if'),('INLINE_TEXT', 'youAreUsingPug'), ('INDENT', '\n  '), ('TAG', 'p'), ('INLINE_TEXT', 'You are amazing'), ('NEWLINE', '\n'), ('ELSE', 'else'), ('INDENT', '\n  '), ('TAG', 'p'), ('INLINE_TEXT', 'Get on it!')]
    })
    tests.append({
        "input": "if youAreUsingPug\n  p You are amazing",
        "output": [('IF','if'),('INLINE_TEXT', 'youAreUsingPug'), ('INDENT', '\n  '), ('TAG', 'p'), ('INLINE_TEXT', 'You are amazing')]
    })

    tests.append({
        "input": "- var title = 3;",
        "output": [('ASSIGNMENT', ('title', '3'))]
    })
    tests.append({
        "input": "//var title = 3;\n",
        "output": [('COMMENT', 'var title = 3;'), ('NEWLINE', '\n')]
    })
    tests.append({
        "input": "a(style={color: 'red', background: 'green'})",
        "output": [('TAG', 'a'), ('ATTRIBUTES', {'style': "{color: 'red', background: 'green'}"})]
    })
    tests.append({
        "input": "doctype html",
        "output": [('DOCTYPE', 'html')]
    })
    tests.append({
        "input": 'doctype html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN"',
        "output": [('DOCTYPE', 'html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN"')]
    })
    tests.append({
        "input": "include includes/head.pug",
        "output": [('INCLUDE', 'includes/head.pug')]
    })
    tests.append({
        "input": "case friends\n when 0\n  p you have no friends\n when 1\n  p you have a friend\n default\n  p you have #{friends} friends",
        "output": [('CASE', 'friends'), ('INDENT', '\n '), ('WHEN', '0'), ('INDENT', '\n  '), ('TAG', 'p'), ('INLINE_TEXT', 'you have no friends'), ('INDENT', '\n '), ('WHEN', '1'), ('INDENT', '\n  '), ('TAG', 'p'), ('INLINE_TEXT', 'you have a friend'), ('INDENT', '\n '), ('DEFAULT', 'default'), ('INDENT', '\n  '), ('TAG', 'p'), ('INLINE_TEXT', 'you have #{friends} friends')]
        })
    tests.append({
        "input": "each val in [1, 2, 3]\n  li= val",
        "output": [('EACH', 'val in [1, 2, 3]'), ('INDENT', '\n  '), ('TAG', 'li'), ('INLINE_TEXT', 'val')]
    })
    tests.append({
        "input": "for (var x = 0; x < 3; x++)\n  li item",
        "output": [('FOR', '(var x = 0; x < 3; x++)'), ('INDENT', '\n  '), ('TAG', 'li'), ('INLINE_TEXT', 'item')]
    })
    tests.append({
        "input": "html(lang='en')\n  head\n    title= pageTitle\n    script(type='text/javascript').\n      if (foo) bar(1 + 5)\n  body\n    h1 Pug - node template engine",
        "output" : [('TAG', 'html'), ('ATTRIBUTES', {'lang': 'en'}), ('INDENT', '\n  '), ('TAG', 'head'), ('INDENT', '\n    '), ('TITLE', 'pageTitle'), ('INDENT', '\n    '), ('TAG', 'script'), ('ATTRIBUTES', {'type': 'text/javascript'}), ('DOT', '.'), ('INDENT', '\n      '), ('DOT_BLOCK', 'if (foo) bar(1 + 5)'), ('INDENT', '\n  '), ('TAG', 'body'), ('INDENT', '\n    '), ('TAG', 'h1'), ('INLINE_TEXT', 'Pug - node template engine')]
    })
    tests.append({
        "input": "html(lang='en')\n  head\n    title= pageTitle\n  body\n    h1 Pug - node template engine\n    div\n      if youAreUsingPug\n        p You are amazing\n      else\n        p Get on it!\n      p.\n        Pug is a terse and simple templating language with a strong focus on performance and powerful features""",
        "output": [('TAG', 'html'), ('ATTRIBUTES', {'lang': 'en'}), ('INDENT', '\n  '), ('TAG', 'head'), ('INDENT', '\n    '), ('TITLE', 'pageTitle'), ('INDENT', '\n  '), ('TAG', 'body'), ('INDENT', '\n    '), ('TAG', 'h1'), ('INLINE_TEXT', 'Pug - node template engine'), ('INDENT', '\n    '), ('TAG', 'div'), ('INDENT', '\n      '), ('IF', 'if'), ('INLINE_TEXT', 'youAreUsingPug'), ('INDENT', '\n        '), ('TAG', 'p'), ('INLINE_TEXT', 'You are amazing'), ('INDENT', '\n      '), ('ELSE', 'else'), ('INDENT', '\n        '), ('TAG', 'p'), ('INLINE_TEXT', 'Get on it!'), ('INDENT', '\n      '), ('TAG', 'p'), ('DOT', '.'), ('INDENT', '\n        '), ('DOT_BLOCK', 'Pug is a terse and simple templating language with a strong focus on performance and powerful features')]
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
