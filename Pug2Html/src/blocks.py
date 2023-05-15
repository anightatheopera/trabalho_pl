from dataclasses import dataclass

BLOCK_TAG = "TAG"


class Tag():
    def __init__(self, name: str, attrs, inline_text=None) -> None:
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
    def __init__(self, indent: int, value: str, children) -> None:
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
class Match():
    match: str
    do: object
    _break: bool = False

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Match({repr(self.match)}, {repr(self.do)}, {repr(self._break)})"

    def __eq__(self, other:object):
        if isinstance(other, Match):
            return self.match == other.match and self.do == other.do and self._break == other._break
        return False


@dataclass
class Case():
    var: str
    case: dict(str, Match)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"Case({repr(self.var)}, {repr(self.case)})"

    def __eq__(self, other:object):
        if isinstance(other, Case):
            return self.var == other.var and self.case == other.case
        return False



def push_ast(asts: list, ast: Ast):
    if len(asts) == 0:
        asts.append(ast)
    elif asts[-1].indent == ast.indent:
        asts.append(ast)
    elif asts[-1].indent < ast.indent:
        push_ast(asts[-1].children, ast)
    else:
        assert False, f"Not implemented {asts} {ast}"
