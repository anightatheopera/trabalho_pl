import re

# Example usage:
html = '<!--[if IE 8]> html(lang="en" class="lt-ie9") <![endif]--> <!--[if gt IE 8]><!--> html(lang="en") <!--<![endif]-->'

# Regular expression for matching the start of a comment
start_comment_regex = re.compile(r"<!--\[if\s.*?\]>")

# Regular expression for matching the end of a comment
end_comment_regex = re.compile(r"<\!\[endif\]-->\s*")

# Iterate over each match in the input string
for match in re.finditer(start_comment_regex, html):
    # Print the start index of the match
    print(match.group(0))
    
    # Search for the end of the comment starting from the end of the start tag
    end_match = re.search(end_comment_regex, html[match.end():])
    
    # If the end of the comment is found, print the end index of the match and extract the comment content
    if end_match:
        comment_start = match.start()
        comment_end = match.end() + end_match.end()
        
        # Extract the comment content by removing the opening comment tag and condition
        comment_content = start_comment_regex.sub('', html[match.end():comment_end])
        
        # Remove any whitespace at the beginning and end of the comment content
        comment_content = comment_content.strip()
        comment_content = comment_content.strip('<![endif]-->')
        
        print(comment_content)
        print(end_match.group(0))
    else:
        print("End of comment not found.")