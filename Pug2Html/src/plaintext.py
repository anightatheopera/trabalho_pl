pug ="""
p.
  Using regular tags can help keep your lines short,
  but interpolated tags may be easier to #[em visualize]
  whether the tags and text are whitespace-separated."""

def plain_text(line):
    if line.lstrip().startswith('p'):
        return line[2:].lstrip()
    else:
        return line

def plain_text_piped(text):
    lines = text.strip().split('\n')
    text_lines = []
    for line in lines:
        if not line.lstrip().startswith('|'):
            continue
        text_lines.append(line.strip()[1:])
    return ''.join(text_lines)

# returns the tag name that is presented in block form
def tag_block(text):
    lines = text.split('\n')
    for line in lines:
        if line.strip() != "":
            contents = line.split('.')[0].strip()
            return contents
    return ""  # No non-empty line found with a dot

def block_in_a_tag(text):
    words = text.split()
    for word in words:
        if word.endswith('.'):
            index = text.find(word)
            return text[index + len(word):].lstrip()
    return ""  

print(block_in_a_tag(pug))