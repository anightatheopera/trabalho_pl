import sys
from parse import build_parser
from blocks import Ast, Tag
import re


def compile_open_tag(tag: Tag):
    attrs_str = ""
    for attr in tag.attrs:
        attrs_str += f' {attr}="{tag.attrs[attr]}"'
    return f"<{tag.name}{attrs_str}>"


def compile_close_tag(tag: Tag):
    return f"</{tag.name}>"


re_interpolated_tag = re.compile(r"#\[\w+ [^\]]*\]")

def compile_literal(parser, literal: str):
    ret = literal
    for key in parser.variables:
        ret = ret.replace("#{" + key + "}", parser.variables[key])
    
    
    while True:
        match_object = re_interpolated_tag.search(ret)
        if match_object == None:
            break
        begin = match_object.start()
        end = match_object.end()
        interpolation = ret[begin+2:end-1]
        spc = interpolation.find(" ")
        tag = interpolation[:spc]
        text = interpolation[spc+1:]
        ret = ret[:begin] + f"<{tag}>{text}</{tag}>" + ret[end:]
        
    return ret  
    

def compile_ast(parser, ast: Ast):
    if isinstance(ast.value, Tag) and ast.children == []:
        inline_str = ast.value.inline_text if ast.value.inline_text != None else ""
        return f"{compile_open_tag(ast.value)}{compile_literal(parser,inline_str)}{compile_close_tag(ast.value)}"

    elif isinstance(ast.value, Tag):
        ret = ""
        sub_indent = ast.children[0].indent
        for child in ast.children:
            for line in compile_ast(parser,child).split("\n"):
                ret += f"{' ' * sub_indent}{compile_literal(parser,line)}\n"

        return f"{compile_open_tag(ast.value)}\n{ret}{compile_close_tag(ast.value)}"

    elif isinstance(ast.value, str) and ast.children == []:
        return ast.value

    else:
        assert False, f"Not implemented: {repr(ast)}"


def compile(input: str):
    parser = build_parser()
    result = parser.parse(input)
    if result == None:
        return ""
    ret = ""
    for ast in result:
        ret += f"{compile_ast(parser,ast)}\n"
    return ret


def run_compiler_tests():
    tests = []
    tests.append({
        "input": "div",
        "output": '<div></div>\n'
    })
    tests.append({
        "input": "div\ndiv",
        "output": '<div></div>\n<div></div>\n'
    })
    tests.append({
        "input": "div\n p",
        "output": '<div>\n <p></p>\n</div>\n'
    })
    tests.append({
        "input": "div#hello(x='1')",
        "output": '<div id="hello" x="1"></div>\n'
    })
    tests.append({
        "input": "div#hello foo bar",
        "output": '<div id="hello">foo bar</div>\n'
    })
    tests.append({
        "input": "foo\n| bar",
        "output": '<foo></foo>\nbar\n'
    })
    tests.append({
        "input": "div\n.\n  is lit\n  more lit",
        "output": '<div></div>\nis lit\nmore lit\n'
    })
    tests.append({
        "input": "div\n foobar text\n script.\n  is lit\n  more lit",
        "output": '<div>\n <foobar>text</foobar>\n <script>is lit\n more lit</script>\n</div>\n'
    })
    tests.append({
        "input": "div1\n div2\n  div3\n div4\ndiv5\ndiv6\n div7",
        "output": '<div1>\n <div2>\n   <div3></div3>\n </div2>\n <div4></div4>\n</div1>\n<div5></div5>\n<div6>\n <div7></div7>\n</div6>\n'
    })
    tests.append({
        "input": "input(\n  type='checkbox'\n  name='agreement' virg='bar'\n)",
        "output": '<input type="checkbox" name="agreement" virg="bar"></input>\n'
    })
    tests.append({
        "input": "- var msg = \"not my inside voice\";\np This is #{msg}",
        "output": "<p>This is not my inside voice</p>\n"
    })
    tests.append({
        "input": "// hello",
        "output": "<!--  hello -->\n"
    })
    tests.append({
        "input": "- var title = 3;\n p #{title}",
        "output": "<p>3</p>\n"
    })
    tests.append({
        "input": "p Suddenly there is a #[strong strongly worded phrase] that cannot be #[strong strongly worded phrase]",
        "output": '<p>Suddenly there is a <strong>strongly worded phrase</strong> that cannot be <strong>strongly worded phrase</strong></p>\n'
    })
    for test in tests:
        output = compile(test["input"])
        if output != test["output"]:
            print(f"Failed test {repr(test['input'])}")
            print(f"Expected: {repr(test['output'])}")
            print(f"Obtained: {repr(output)}")
            sys.exit(1)
        else:
            print(f"Passed test {repr(test['input'])}")
