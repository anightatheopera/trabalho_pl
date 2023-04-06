import ply.lex as lex
import ply.yacc as yacc

# Define the list of token names
tokens = (
    'COMMENT', 'DOCTYPE', 'HYPERLINK', 'ADDRESS', 'AREA', 'ARTICLE', 'ASIDE',
    'AUDIO', 'BOLD', 'BASE', 'BDI', 'BDO', 'BLOCKQUOTE', 'BODY', 'BREAK',
    'BUTTON', 'CANVAS', 'CAPTION', 'CITE', 'CODE', 'COLUMN', 'COLUMNGROUP',
    'DATA', 'DATALIST', 'DESCRIPTION', 'DELETED', 'DETAILS', 'DFN', 'DIALOG',
    'DIV', 'DT', 'EM', 'EMBED', 'FIELDSET', 'FIGCAPTION', 'FIGURE', 'FOOTER',
    'FORM', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'HEAD', 'HEADER', 'HR', 'HTML',
    'I', 'IFRAME', 'IMG', 'INPUT', 'INS', 'KBD', 'LABEL', 'LEGEND', 'LI',
    'LINK', 'MAIN', 'MAP', 'MARK', 'META', 'METER', 'NAV', 'NOSCRIPT', 'OBJECT',
    'OL', 'OPTGROUP', 'OPTION', 'OUTPUT', 'P', 'PARAM', 'PICTURE', 'PRE', 'PROGRESS',
    'Q', 'RP', 'RT', 'RUBY', 'S', 'SAMP', 'SCRIPT', 'SECTION', 'SELECT',
    'SMALL', 'SOURCE', 'SPAN', 'STRONG', 'STYLE', 'SUB', 'SUMMARY', 'SUP',
    'SVG', 'TABLE', 'TBODY', 'TD', 'TEMPLATE', 'TEXTAREA', 'TFOOT', 'TH',
    'THEAD', 'TIME', 'TITLE', 'TR', 'TRACK', 'U', 'UL', 'VAR', 'VIDEO', 'WBR'
)

# Regular expressions for each token
t_COMMENT = r'//' # This is a comment <!-- [...] -->
t_DOCTYPE = r'doctype' #This is a doctype <!DOCTYPE> 
t_HYPERLINK = r'a\(href=\'//[a-z]*\'\)[a-zA-Z0-9]*' #This is a hyperlink
t_ADDRESS = r'address' #This is an address
t_AREA = r'area' #This is an area
t_ARTICLE = r'article' #This is an article
t_ASIDE = r'aside' #This is an aside
t_AUDIO = r'audio' #This is an audio
t_BOLD = r'b' #This is bold
t_BASE = r'base' #This is a base
t_BDI = r'bdi' #This is a bdi
t_BDO = r'bdo' #This is a bdo
t_BLOCKQUOTE = r'blockquote' #This is a blockquote
t_BODY = r'body' #This is a body
t_BREAK = r'br' #This is a break
t_BUTTON = r'button' #This is a button
t_CANVAS = r'canvas' #This is a canvas

