from dataclasses import dataclass

BLOCK_TAG = "TAG"


class Tag():
    def __init__(self, name, attrs, inline_text=None) -> None:
        self.name = name
        self.attrs = attrs
        self.inline_text = inline_text

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Tag({repr(self.name)}, {repr(self.attrs)}, {repr(self.inline_text)})"

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name and self.attrs == other.attrs and self.inline_text == self.inline_text
        return False


class Ast():
    def __init__(self, indent: int, value, children) -> None:
        self.indent = indent
        self.value = value
        self.children = children

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Ast({repr(self.indent)},{repr(self.value)},{repr(self.children)})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Ast):
            return self.indent == other.indent and self.value == other.value and self.children == other.children
        return False

@dataclass
class Case():
    var: str
    case: dict[str, object]

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Case({repr(self.var)}, {repr(self.case)})"

    def __eq__(self, other:object):
        if isinstance(other, Case):
            return self.var == other.var and self.case == other.case
        return False

@dataclass
class For():
    var: str
    init_call: str
    condition: str
    increment: str
    todo: object

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"For({repr(self.var)}, {repr(self.init_call)}, {repr(self.condition)}, {repr(self.increment)}, {repr(self.todo)})"

    def __eq__(self, other:object):
        if isinstance(other, For):
            return self.var == other.var and self.init_call == other.init_call and self.condition == other.condition and self.increment == other.increment and self.todo == other.todo
        return False

@dataclass
class If():
    condition: str
    run: object
    else_: object

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"If({repr(self.condition)}, {repr(self.run)})"

    def __eq__(self, other:object):
        if isinstance(other, If):
            return self.condition == other.condition and self.run == other.run
        return False

@dataclass
class Include():
    path: str

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Include({repr(self.path)})"

    def __eq__(self, other:object):
        if isinstance(other, Include):
            return self.path == other.path
        return False

@dataclass
class Each():
    var: str
    in_: str
    run: object

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Each({repr(self.var)}, {repr(self.in_)}, {repr(self.run)})"

    def __eq__(self, other:object):
        if isinstance(other, Each):
            return self.var == other.var and self.in_ == other.in_ and self.run == other.run
        return False

def push_ast(asts: list, ast: Ast):
    if len(asts) == 0:
        asts.append(ast)
    elif asts[-1].indent == ast.indent:
        asts.append(ast)
    elif asts[-1].indent < ast.indent:
        push_ast(asts[-1].children, ast)
    else:
        assert False, f"Not implemented {asts}  <-  {ast}"
