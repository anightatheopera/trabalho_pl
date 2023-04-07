import re 

pug = """
input(
  type='checkbox'
  name='agreement'
  checked
)
"""

def attribute_type(attribute):
    # Split the attribute by "(" and take the second element.
    content = attribute.split("(")[1]
    # Split the content by " " and ":" to get the attribute values.
    attribute_values = []
    for attr in content.split():
        if "=" in attr:
            attribute_values.append(attr.split("=")[1].strip("'"))
    
    return attribute_values


def attribute_content(attribute):
    # Split the attribute by "(" and take the second element.
    content = attribute.split("(")[1]
    
    # Split the content by " " and ":" to get the attribute types.
    attribute_types = [attr.split("=")[0].strip() for attr in content.split() if "=" in attr]
    
    return attribute_types


def is_attribute(line):
    # Construct a regular expression that matches a Pug attribute line.
    regex = re.compile(r'^[ \t]*\w+(\([\w\W]*\))?')
    
    # Search for the attribute pattern in the line.
    match = regex.search(line)
    
    if match:
        return True
    else:
        return False
    
def attribute_tag(pug_line):
    pug_line = pug_line.strip()
    if '(' in pug_line:
        tag = pug_line[:pug_line.index('(')]
    else:
        tag = pug_line
    return tag
    
def attribute_content(line):
    # Construct a regular expression that matches the content after the attribute list.
    regex = re.compile(r'\)[ \t]*([^ \t].*)?')
    
    # Search for the content in the line.
    match = regex.search(line)
    
    if match:
        return match.group(1)
    else:
        return None
    
def match_type_value(pug_line):
    attribute_dict = {}
    if '(' in pug_line and ')' in pug_line:
        start_index = pug_line.index('(') + 1
        end_index = pug_line.index(')')
        attributes = pug_line[start_index:end_index].strip()
        attribute_pairs = attributes.split('\n')
        for attr_pair in attribute_pairs:
            attr_parts = attr_pair.strip().split('=')
            if len(attr_parts) > 1:
                attr_type = attr_parts[0].strip()
                attr_value = '='.join(attr_parts[1:]).strip().strip("'\"")
                attribute_dict[attr_type] = attr_value
            else:
                attribute_dict[attr_pair.strip()] = ''
    return attribute_dict
    
print(match_type_value(pug))