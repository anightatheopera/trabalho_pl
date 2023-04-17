
BLOCK_TAG = "TAG"


class Tag():
    def __init__(self, name: str, indent: int, attrs, children) -> None:
        self.name = name
        self.indent = indent
        self.attrs = attrs
        self.children = children

    def __str__(self) -> str:
        ret = f"Tag('{self.name}', {self.indent}, {self.attrs}, ["
        if len(self.children) > 0:
            ret += repr(self.children[0]) if isinstance(self.children[0], str) else str(self.children[0])
            for child in self.children[1:]:
                ret += f", {repr(child) if isinstance(child, str) else str(child)}"
        ret += "])"
        return ret

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name and self.indent == other.indent and self.attrs == other.attrs and self.children == other.children
        return False


class Literal():
    def __init__(self, value: str, indent: int) -> None:
        self.value = value
        self.indent = indent

    def __str__(self) -> str:
        return f"Literal({repr(self.value)}, {self.indent})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Literal):
            return self.value == other.value and self.indent == other.indent
        return False
