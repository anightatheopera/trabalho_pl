import ply.lex as lex
import ply.yacc as yacc

# Define the list of token names
tokens = (
    'COMMENT', 'DOCTYPE', 'HYPERLINK', 'ADDRESS', 'AREA', 'ARTICLE', 'ASIDE',
    'AUDIO', 'BOLD', 'BASE', 'BDI', 'BDO', 'BLOCKQUOTE', 'BODY', 'BREAK',
    'BUTTON', 'CANVAS', 'CAPTION', 'CITE', 'CODE', 'COLUMN', 'COLUMNGROUP',
    'DATA', 'DATALIST', 'DESCRIPTION', 'DELETED'
)

# Regular expressions for each token
t_COMMENT = r'//' # This is a comment <!-- [...] -->
t_DOCTYPE = r'doctype' #This is a doctype <!DOCTYPE> 
t_HYPERLINK = r'a\(href=\'//[a-z]*\'\)[a-zA-Z0-9]*' #This is a hyperlink
#t_ADDRESS =
#t_AREA = 
#t_ARTICLE = 
#t_ASIDE =

