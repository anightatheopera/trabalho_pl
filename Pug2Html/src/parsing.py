import ply.yacc as yacc
import sys
from blocks import *

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

def p_ast_term(p):
    """
    ast : title
        | tag
        | literal
        | case
        | include
        | doctype
        | each
        | for
    """
    p[0] = [p[1]]



def p_for(p):
    """
    for : FOR ast
        | indent FOR ast
    """
    if len(p) == 3:
        (var, condition, increment) = p[1].split(";",2)
        (var,init_call) = var.split("=")
        p[0] = Ast(0, For(var, init_call, condition, increment, p[2]), [])
    else:
        (var, condition, increment) = p[2].split(";",2)
        (var,init_call) = var.split("=")
        p[0] = Ast(p[1], For(var, init_call, condition, increment, p[3]), [])


def p_each(p):
    """
    each : EACH ast
         | indent EACH ast
    """
    if len(p) == 3:
        var = p[1].split(" ",2)[0]
        rng = p[1].split(" ",2)[2] 
        p[0] = Ast(0, Each(var,rng,p[2]), [])
    else:
        var = p[2].split(" ",2)[0]
        rng = p[2].split(" ",2)[2] 
        p[0] = Ast(p[1], Each(var,rng,p[3]), [])

def p_include(p):
    """
    include : INCLUDE
            | indent INCLUDE
    """
    if len(p) == 2:
        p[0] = Ast(0, Include(p[1]), [])
    else:
        p[0] = Ast(p[1], Include(p[2]), [])

def p_doctype(p):
    """
    doctype : DOCTYPE
            | indent DOCTYPE
    """
    if len(p) == 2:
        p[0] = Ast(0, f"<!DOCTYPE {p[1]}", [])
    else:
        p[0] = Ast(p[1], f"<!DOCTYPE {p[1]}", [])

def p_title(p):
    """
    title : TITLE
          | indent TITLE
    """
    if len(p) == 2:
        p[0] = Ast(0, Tag("title",{'title':p[1]}), [])
    else:
        p[0] = Ast(p[1], Tag("title",{'title':p[2]}), [])


def p_if_else(p):
    """
    if_else  : if else
             | if
    """
    if len(p) == 3:
        p[0] = p[1]
        p[0].value.else_ = p[2]
    else:
        p[0] = p[1]
    
def p_if(p):
    """
    if : IF INLINE_TEXT ast
       | indent IF INLINE_TEXT ast
    """
    if len(p) == 4:
        p[0] = Ast(0, If(p[2], [p[3]], None), [])
    else:
        p[0] = Ast(p[1], If(p[2], [p[3]], None), [])

def p_else(p):
    """
    else : NEWLINE ELSE ast
         | indent ELSE ast
    """
    if isinstance(p[1], int):
        p[0] = Ast(p[1], p[3], [])
    else:
        p[0] = Ast(0, p[2], [])

def p_case(p):
    """
    case : CASE when
         | indent CASE when
    """
    if len(p) == 4:
        p[0] = Ast(p[1], Case(p[2], p[3]), [])
    else:
        p[0] = Ast(0, Case(p[1], p[2]), [])

def p_when(p):
    """
    when : indent WHEN ast when
           | indent DEFAULT ast
           | WHEN ast when
           | DEFAULT ast
    """
    p_dict = {}
    if len(p) == 5:
        p_dict[p[2]] = p[3]
        p_dict.update(p[4])
    elif len(p) == 4:
        if isinstance(p[1], int):
            p_dict[p[2]]= p[3]
        else:
            p_dict[p[1]]= p[2]
            p_dict.update(p[3])
    else:
        p_dict[p[1]]= p[2]
    p[0] = p_dict

def p_ast_vars(p):
    "ast : ASSIGNMENT"
    p[0] = None
    (key,value) = p[1] 
    p.parser.variables[key] = value 

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
    
 

def p_dotblock_ind(p):
    "dotblock : indent DOT_BLOCK"
    p[0] = p[2]


def p_dot_blocks(p):
    """dotblocks : dotblocks dotblock
                 | dotblock
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + "\n" + p[2]

def p_error(p):
    print(f"Syntax error in input! {p}")


def build_parser():
    lexer = build_lexer()
    parser = yacc.yacc(debug=True)
    parser.variables = {}
    return parser


def parse_pug(pug):
    parser = build_parser()
    output = parser.parse(pug)
    return output

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
    tests.append({
        "input": "title= title",
        "output": [Ast(0, Tag('title', {'title': 'title'}, None), [])]
    })
    #tests.append({
    #    "input": "if youAreUsingPug\n  p You are amazing\nelse\n  p Get on it!",
    #    "output": [Ast(0, If('youAreUsingPug', [Ast(2, Tag('p', {}, 'You are amazing'), [])], [Ast(2, Tag('p', {}, 'Get on it!'), [])]), [])]
    #})
    #tests.append({
    #    "input": "if youAreUsingPug\n  p You are amazing",
    #    "output": [Ast(0, If('youAreUsingPug', [Ast(2, Tag('p', {}, 'You are amazing'), [])], None), [])]
    #})
    tests.append({
        "input": "a(style={color: 'red', background: 'green'})",
        "output": [Ast(0, Tag('a', {'style': "{color: 'red', background: 'green'}"}, None), [])]
    })
    tests.append({
        "input": "doctype html",
        "output": [Ast(0,'<!DOCTYPE html',[])]
    })
    tests.append({
        "input": 'doctype html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN"',
        "output": [Ast(0,'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN"',[])]
    })
    tests.append({
        "input": "include includes/head.pug",
        "output": [Ast(0,Include('includes/head.pug'),[])]
    })
    tests.append({
        "input": "case friends\n when 0\n  p you have no friends\n when 1\n  p you have a friend\n default\n  p you have #{friends} friends",
        "output": [Ast(0,Case('friends', {'0': [Ast(2,Tag('p', {}, 'you have no friends'),[])], '1': [Ast(2,Tag('p', {}, 'you have a friend'),[])], 'default': [Ast(2,Tag('p', {}, 'you have #{friends} friends'),[])]}),[])]
    })
    tests.append({
        "input": "each val in [1, 2, 3]\n  li= val",
        "output": [Ast(0,Each('val', '[1, 2, 3]', [Ast(2,Tag('li', {}, 'val'),[])]),[])]
    })
    tests.append({
        "input": "for (var x = 0; x < 3; x++)\n  li item",
        "output": [Ast(0,For('(var x ', ' 0', ' x < 3', ' x++)', [Ast(2,Tag('li', {}, 'item'),[])]),[])]
    })
    tests.append({
        "input": "p\n  p\n    p Hello",
        "output": [Ast(0,Tag('p', {},None),[Ast(2,Tag('p', {}, None),[Ast(4,Tag('p', {}, 'Hello'),[])])])]
    })
    tests.append({
        "input": "html(lang='en')\n  head\n    title= pageTitle\n  body\n    h1 Pug - node template engine",
        "output": [Ast(0,Tag('html', {'lang': 'en'}, None),[Ast(2,Tag('head', {}, None),[Ast(4,Tag('title', {'title': 'pageTitle'}, None),[])]), Ast(2,Tag('body', {}, None),[Ast(4,Tag('h1', {}, 'Pug - node template engine'),[])])])]
    })
    tests.append({
        "input": """html(lang='en')
  head
    title= pageTitle
  body
    h1 Pug - node template engine
    div
      p You are amazing
    p.
      Pug is a terse and simple templating language with a strong focus on performance and powerful features""",
      "output": [Ast(0,Tag('html', {'lang': 'en'}, None),[Ast(2,Tag('head', {}, None),[Ast(4,Tag('title', {'title': 'pageTitle'}, None),[])]), Ast(2,Tag('body', {}, None),[Ast(4,Tag('h1', {}, 'Pug - node template engine'),[]), Ast(4,Tag('div', {}, None),[Ast(6,Tag('p', {}, 'You are amazing'),[])]), Ast(4,Tag('p', {}, 'Pug is a terse and simple templating language with a strong focus on performance and powerful features'),[])])])]
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
