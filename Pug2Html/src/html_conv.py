from parse import parse_pug
from blocks import Ast, Tag
from lexer import build_lexer


def pug_to_html(pug_code):
    # Build lexer
    lexer = build_lexer()

    # Tokenize Pug code
    lexer.input(pug_code)
    tokens = list(lexer)

    # Parse Pug code
    parsed = parse_pug(pug_code)

    # Generate HTML code
    def generate_html(node):
        if isinstance(node, Ast):
            pass
        elif isinstance(node, Tag):
            attributes = " ".join(f'{k}="{v}"' for k, v in node.attrs.items())
            start_tag = f"<{node.name} {attributes}>" if attributes else f"<{node.name}>"
            children = "".join(generate_html(child) for child in node.children)
            end_tag = f"</{node.name}>"
            return f"{start_tag}{children}{end_tag}"
        else:
            raise ValueError(f"Invalid node type: {type(node)}")

    try:
        return generate_html(parsed)
    except Exception as e:
        print(f"Error generating HTML: {e}")
        print(f"Parsed tree: {parsed}")
        raise

pug_code = "div\ndiv"

html_code = pug_to_html(pug_code)

print(html_code)

