import ply.lex as lex

class PugLexer(object):
    tokens = ((),)
    
    # Build the lexer
    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Define the list of token names
    tokens = (
        'COMMENT','PUG_COMMENT','SPECIALCOMMENT','DOCTYPE','HYPERLINK','ADDRESS','AREA','ARTICLE','ASIDE',
        'AUDIO','BOLD','BASE','BDI','BDO','BLOCKQUOTE','BODY','BREAK',
        'BUTTON','CANVAS','CAPTION','CITE','CODE','COL','COLGROUP',
        'DATA','DATALIST','DESCRIPTION','DEL','DETAILS','DFN','DIALOG',
        'DIV','DT','EM','EMBED','FIELDSET','FIGCAPTION','FIGURE','FOOTER',
        'FORM','H1','H2','H3','H4','H5','H6','HEAD','HEADER','HR','HTML',
        'I','IFRAME','IMG','INPUT','INS','KBD', 'KEYGEN','LABEL','LEGEND','LI',
        'LINK','MAIN','MENU','MENUITEM','MAP','MARK','META','METER','NAV','NOSCRIPT','OBJECT',
        'OL','OPTGROUP','OPTION','OUTPUT','P','PARAM','PICTURE','PRE','PROGRESS',
        'Q','RP','RT','RUBY','S','SAMP','SCRIPT','SECTION','SELECT',
        'SMALL','SOURCE','SPAN','STRONG','STYLE','SUB','SUMMARY','SUP',
        'SVG','TABLE','TBODY','TD','TEMPLATE','TEXTAREA','TFOOT','TH',
        'THEAD','TIME','TITLE','TR','TRACK','U','UL','VAR','VIDEO','WBR',
        'PIPE','TEXT','SCRIPT','STYLE','TAG','CLASS','ID','ATTRIBUTE','EQUALS',
        'STRING','BOOLEAN','NUMBER','NULL','UNDEFINED','INCLUDE','EXTENDS','BLOCK',
        'MIXIN','PLUS','MINUS','TIMES','DIVIDE','MODULUS','ASSIGN','LPAREN','RPAREN',
        'LBRACE','RBRACE','LBRACKET','RBRACKET','DOT','COLON','COMMA','OR','AND','NOT',
        'EQ','NEQ','LT','LTE','GT','GTE','IF','ELSE','UNLESS','CASE','WHEN','DEFAULT',
        'EACH','FOR','IN','ATTR_OPEN','ATTR_CLOSE','TRUE','FALSE','NULL_LITERAL',
        'UNDEFINED_LITERAL','BLOCK_OPEN','BLOCK_CLOSE','MIXIN_CALL','EXTEND','YIELD','SLASH','NEWLINE'
    )

    # Regular expressions for each token
    t_DOCTYPE = r'doctype' #This is a doctype <!DOCTYPE> 
    t_HYPERLINK = r'a' #This is a hyperlink
    t_ADDRESS = r'address' #This is an address tag
    t_AREA = r'area' #This is an area tag
    t_ARTICLE = r'article' #This is an article tag
    t_ASIDE = r'aside' #This is an aside tag
    t_AUDIO = r'audio' #This is an audio tag
    t_BOLD = r'b' #This is bold tag
    t_BASE = r'base' #This is a base
    t_BDI = r'bdi' #This is a bdi
    t_BDO = r'bdo' #This is a bdo
    t_BLOCKQUOTE = r'blockquote' #This is a blockquote
    t_BODY = r'body' #This is a body
    t_BREAK = r'br' #This is a break
    t_BUTTON = r'button' #This is a button
    t_CANVAS = r'canvas' #This is a canvas
    t_CAPTION = r'caption' #This is a caption
    t_CITE = r'cite' #This is a cite
    t_CODE = r'code' #This is a code
    t_COL = r'col' #This is a column
    t_COLGROUP = r'colgroup' #This is a column group
    t_DATA = r'data' #This is a data
    t_DATALIST = r'datalist' #This is a datalist
    t_DESCRIPTION = r'description' #This is a description
    t_DEL = r'del' #This is a deleted
    t_DETAILS = r'details' #This is a details
    t_DFN = r'dfn' #This is a dfn
    t_DIALOG = r'dialog' #This is a dialog
    t_DIV = r'div' #This is a div
    t_DT = r'dt' #This is a dt
    t_EM = r'em' #This is an em
    t_EMBED = r'embed' #This is an embed
    t_FIELDSET = r'fieldset' #This is a fieldset
    t_FIGCAPTION = r'figcaption' #This is a figcaption
    t_FIGURE = r'figure' #This is a figure
    t_FOOTER = r'footer' #This is a footer
    t_FORM = r'form' #This is a form
    t_H1 = r'h1' #This is a h1
    t_H2 = r'h2' #This is a h2
    t_H3 = r'h3' #This is a h3
    t_H4 = r'h4' #This is a h4
    t_H5 = r'h5' #This is a h5
    t_H6 = r'h6' #This is a h6
    t_HEAD = r'head' #This is a head
    t_HEADER = r'header' #This is a header
    t_HR = r'hr' #This is a hr
    t_HTML = r'html' #This is a html
    t_I = r'i' #This is an i
    t_IFRAME = r'iframe' #This is an iframe
    t_IMG = r'img' #This is an img
    t_INPUT = r'input' #This is an input
    t_INS = r'ins' #This is an ins
    t_KBD = r'kbd' #This is a kbd
    t_KEYGEN = r'keygen' #This is a keygen
    t_LABEL = r'label' #This is a label
    t_LEGEND = r'legend' #This is a legend
    t_LI = r'li' #This is a li
    t_LINK = r'link' #This is a link
    t_MAIN = r'main' #This is a main
    t_MENU = r'menu' #This is a menu
    t_MENUITEM = r'menuitem' #This is a menuitem
    t_MAP = r'map' #This is a map
    t_MARK = r'mark' #This is a mark
    t_META = r'meta' #This is a meta
    t_METER = r'meter' #This is a meter
    t_NAV = r'nav' #This is a nav
    t_NOSCRIPT = r'noscript' #This is a noscript
    t_OBJECT = r'object' #This is an object
    t_OL = r'ol' #This is an ol
    t_OPTGROUP = r'optgroup' #This is an optgroup
    t_OPTION = r'option' #This is an option
    t_OUTPUT = r'output' #This is an output
    t_P = r'p' #This is a p
    t_PARAM = r'param' #This is a param
    t_PICTURE = r'picture' #This is a picture
    t_PRE = r'pre' #This is a pre
    t_PROGRESS = r'progress' #This is a progress
    t_Q = r'q' #This is a q
    t_RP = r'rp' #This is an rp
    t_RT = r'rt' #This is an rt
    t_RUBY = r'ruby' #This is a ruby
    t_S = r's' #This is an s
    t_SAMP = r'samp' #This is a samp
    t_SCRIPT = r'script' #This is a script
    t_SECTION = r'section' #This is a section
    t_SELECT = r'select' #This is a select
    t_SMALL = r'small' #This is a small
    t_SOURCE = r'source' #This is a source
    t_SPAN = r'span' #This is a span
    t_STRONG = r'strong' #This is a strong
    t_STYLE = r'style' #This is a style
    t_SUB = r'sub' #This is a sub
    t_SUMMARY = r'summary' #This is a summary
    t_SUP = r'sup' #This is a sup
    t_SVG = r'svg' #This is a svg
    t_TABLE = r'table' #This is a table 
    t_TBODY = r'tbody' #This is a tbody
    t_TD = r'td' #This is a td
    t_TEMPLATE = r'template' #This is a template
    t_TEXTAREA = r'textarea' #This is a textarea
    t_TFOOT = r'tfoot' #This is a tfoot
    t_TH = r'th' #This is a th
    t_THEAD = r'thead' #This is a thead
    t_TIME = r'time' #This is a time
    t_TITLE = r'title' #This is a title
    t_TR = r'tr' #This is a tr
    t_TRACK = r'track' #This is a track
    t_U = r'u' #This is a u
    t_UL = r'ul' #This is a ul
    t_VAR = r'var' #This is a var
    t_VIDEO = r'video' #This is a video
    t_WBR = r'wbr' #This is a wbr
    t_PIPE = r'\|'
    t_TEXT = r'[^\n\r|]+'
    t_SCRIPT = r'script'
    t_STYLE = r'style'
    t_TAG = r'[a-zA-Z][\w-]*'
    t_CLASS = r'\.[a-zA-Z][\w-]*'
    t_ID = r'#[a-zA-Z][\w-]*'
    t_ATTRIBUTE = r'[a-zA-Z][\w-]*\s*=\s*'
    t_EQUALS = r'='
    t_STRING = r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''
    t_BOOLEAN = r'true|false'
    t_NUMBER = r'\d+(\.\d+)?'
    t_NULL = r'null'
    t_UNDEFINED = r'undefined'
    t_INCLUDE = r'include'
    t_EXTENDS = r'extends'
    t_BLOCK = r'block'
    t_MIXIN = r'mixin'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MODULUS = r'%'
    t_ASSIGN = r':'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_DOT = r'\.'
    t_COLON = r':'
    t_COMMA = r','
    t_OR = r'\|\|'
    t_AND = r'&&'
    t_NOT = r'!'
    t_EQ = r'=='
    t_NEQ = r'!='
    t_LT = r'<'
    t_LTE = r'<='
    t_GT = r'>'
    t_GTE = r'>='
    t_IF = r'if'
    t_ELSE = r'else'
    t_UNLESS = r'unless'
    t_CASE = r'case'
    t_WHEN = r'when'
    t_DEFAULT = r'default'
    t_EACH = r'each'
    t_FOR = r'for'
    t_IN = r'in'
    t_ATTR_OPEN = r'\('
    t_ATTR_CLOSE = r'\)'
    t_TRUE = r'true'
    t_FALSE = r'false'
    t_NULL_LITERAL = r'null'
    t_UNDEFINED_LITERAL = r'undefined'
    t_BLOCK_OPEN = r'block'
    t_BLOCK_CLOSE = r'block'
    t_MIXIN_CALL = r'+[a-zA-Z][\w-]*'
    t_EXTEND = r'extend'
    t_YIELD = r'yield'
    t_SLASH = r'/'
    t_NEWLINE = r'[\n\r]+'
    

    # Define a rule to match comments
    def t_COMMENT(self, t):
        r'\/\/(.*)'
        t.value = t.value[2:]
        return t


    # Define a rule to match pug comments
    def t_PUG_COMMENT(self, t):
        r'\/\/-.*'
        pass

    def t_SPECIALCOMMENT(self, t):
        r'<\!--.*-->'
        # 
    
    def t_DOCTYPE(self, t):
        r'doctype.*'
        t.value = t.value[8:]
        return t
    
    def t_HYPERLINK(self, t):
        r'a.*'
        t.value = t.value[2:]
        return t
    
    def t_ADDRESS (self, t):
        r'address.*'
        t.value = t.value[8:]
        return t
    
    def t_AREA (self, t):
        r'area.*'
        t.value = t.value[5:]
        return t
    
    def t_ARTICLE (self, t):
        r'article.*'
        t.value = t.value[8:]
        return t
    
    def t_ASIDE (self, t):
        r'aside.*'
        t.value = t.value[6:]
        return t
    
    def t_AUDIO (self, t):
        r'audio.*'
        t.value = t.value[6:]
        return t
    
    def t_BOLD (self, t):
        r'b.*'
        t.value = t.value[2:]
        return t
    
    def t_BASE (self, t):
        r'base.*'
        t.value = t.value[5:]
        return t
    
    def t_BDI (self, t):
        r'bdi.*'
        t.value = t.value[4:]
        return t
    
    def t_BDO (self, t):
        r'bdo.*'
        t.value = t.value[4:]
        return t
    
    def t_BLOCKQUOTE (self, t):
        r'blockquote.*'
        t.value = t.value[11:]
        return t
    
    def t_BODY(self, t):
        r'body.*'
        t.value = t.value[5:]
        return t
    
    def t_BR (self, t):
        r'br.*'
        t.value = t.value[3:]
        return t
    
    def t_BUTTON (self, t):
        r'button.*'
        t.value = t.value[7:]
        return t
    
    def t_CANVAS (self, t):
        r'canvas.*'
        t.value = t.value[7:]
        return t
     
    def t_CAPTION (self, t):
        r'caption.*'
        t.value = t.value[8:]
        return t
    
    def t_CITE (self, t):
        r'cite.*'
        t.value = t.value[5:]
        return t
    
    def t_CODE (self, t):
        r'code.*'
        t.value = t.value[5:]
        return t
    
    def t_COL (self, t):
        r'col.*'
        t.value = t.value[4:]
        return t
    
    def t_COLGROUP (self, t):
        r'colgroup.*'
        t.value = t.value[9:]
        return t
    
    def t_DATA (self, t):
        r'data.*'
        t.value = t.value[5:]
        return t
    
    def t_DATALIST (self, t):
        r'datalist.*'
        t.value = t.value[9:]
        return t
    
    def t_DD (self, t):
        r'dd.*'
        t.value = t.value[3:]
        return t
    
    def t_DEL (self, t):
        r'del.*'
        t.value = t.value[4:]
        return t 
    
    def t_DETAILS (self, t):
        r'details.*'
        t.value = t.value[8:]
        return t
    
    def t_DFN (self, t):
        r'dfn.*'
        t.value = t.value[4:]
        return t
    
    def t_DIALOG (self, t):
        r'dialog.*'
        t.value = t.value[7:]
        return t
    
    def t_DIV (self, t):
        r'div.*'
        t.value = t.value[4:]
        return t
    
    def t_DL (self, t):
        r'dl.*'
        t.value = t.value[3:]
        return t       
    
    def t_DT (self, t):
        r'dt.*'
        t.value = t.value[3:]
        return t
    
    def t_EM (self, t):
        r'em.*'
        t.value = t.value[3:]
        return t
    
    def t_EMBED (self, t):
        r'embed.*'
        t.value = t.value[6:]
        return t
    
    def t_FIELDSET (self, t):
        r'fieldset.*'
        t.value = t.value[9:]
        return t
    
    def t_FIGCAPTION (self, t):
        r'figcaption.*'
        t.value = t.value[12:]
        return t
    
    def t_FIGURE (self, t):
        r'figure.*'
        t.value = t.value[7:]
        return t
    
    def t_FOOTER (self, t):
        r'footer.*'
        t.value = t.value[7:]
        return t
    
    def t_FORM (self, t):
        r'form.*'
        t.value = t.value[5:]
        return t
    
    def t_FRAME (self, t):
        r'frame.*'
        t.value = t.value[6:]
        return t
    
    def t_FRAMESET (self, t):
        r'frameset.*'
        t.value = t.value[9:]
        return t
    
    def t_H1 (self, t):
        r'h1.*'
        t.value = t.value[3:]
        return t
    
    def t_H2 (self, t):
        r'h2.*'
        t.value = t.value[3:]
        return t
    
    def t_H3 (self, t):
        r'h3.*'
        t.value = t.value[3:]
        return t
    
    def t_H4 (self, t):
        r'h4.*'
        t.value = t.value[3:]
        return t
    
    def t_H5 (self, t):
        r'h5.*'
        t.value = t.value[3:]
        return t 
    
    def t_H6 (self, t):
        r'h6.*'
        t.value = t.value[3:]
        return t
    
    def t_HEAD (self, t):
        r'head.*'
        t.value = t.value[5:]
        return t
    
    def t_HEADER (self, t):
        r'header.*'
        t.value = t.value[7:]
        return t
    
    def t_HGROUP (self, t):
        r'hgroup.*'
        t.value = t.value[7:]
        return t
    
    def t_HR (self, t):
        r'hr.*'
        t.value = t.value[3:]
        return t
    
    def t_HTML (self, t):
        r'html.*'
        t.value = t.value[5:]
        return t
    
    def t_I (self, t):
        r'i.*'
        t.value = t.value[2:]
        return t
    
    def t_IFRAME (self, t):
        r'iframe.*'
        t.value = t.value[7:]
        return t
    
    def t_IMG (self, t):
        r'img.*'
        t.value = t.value[4:]
        return t
    
    def t_INPUT (self, t):
        r'input.*'
        t.value = t.value[6:]
        return t
    
    def t_INS (self, t):
        r'ins.*'
        t.value = t.value[4:]
        return t
    
    def t_KBD (self, t):
        r'kbd.*'
        t.value = t.value[4:]
        return t
    
    def t_KEYGEN (self, t):
        r'keygen.*'
        t.value = t.value[7:]
        return t
    
    def t_LABEL (self, t):
        r'label.*'
        t.value = t.value[6:]
        return t
    
    def t_LEGEND (self, t):
        r'legend.*'
        t.value = t.value[7:]
        return t
    
    def t_LI (self, t):
        r'li.*'
        t.value = t.value[3:]
        return t
    
    def t_LINK (self, t):
        r'link.*'
        t.value = t.value[5:]
        return t
    
    def t_MAIN (self, t):
        r'main.*'
        t.value = t.value[5:]
        return t
    
    def t_MAP (self, t):
        r'map.*'
        t.value = t.value[4:]
        return t
    
    def t_MARK (self, t):
        r'mark.*'
        t.value = t.value[5:]
        return t
    
    def t_MENU (self, t):
        r'menu.*'
        t.value = t.value[5:]
        return t
    
    def t_MENUITEM (self, t):
        r'menuitem.*'
        t.value = t.value[9:]
        return t
    
    def t_META (self, t):
        r'meta.*'
        t.value = t.value[5:]
        return t
    
    def t_METER (self, t):
        r'meter.*'
        t.value = t.value[6:]
        return t
    
    def t_NAV (self, t):
        r'nav.*'
        t.value = t.value[4:]
        return t
    
    def t_NOSCRIPT (self, t):
        r'noscript.*'
        t.value = t.value[9:]
        return t
    
    def t_OBJECT (self, t):
        r'object.*'
        t.value = t.value[7:]
        return t
    
    def t_OL (self, t):
        r'ol.*'
        t.value = t.value[3:]
        return t
    
    def t_OPTGROUP (self, t):
        r'optgroup.*'
        t.value = t.value[9:]
        return t
    
    def t_OPTION (self, t):
        r'option.*'
        t.value = t.value[7:]
        return t
    
    def t_OUTPUT (self, t):
        r'output.*'
        t.value = t.value[7:]
        return t
    
    def t_P (self, t):
        r'p.*'
        t.value = t.value[2:]
        return t
    
    def t_PARAM (self, t):
        r'param.*'
        t.value = t.value[6:]
        return t
    
    def t_PRE (self, t):
        r'pre.*'
        t.value = t.value[4:]
        return t
    
    def t_PROGRESS (self, t):
        r'progress.*'
        t.value = t.value[9:]
        return t
    
    def t_Q (self, t):
        r'q.*'
        t.value = t.value[2:]
        return t
    
    def t_RP (self, t):
        r'rp.*'
        t.value = t.value[3:]
        return t
    
    def t_RT (self, t):
        r'rt.*'
        t.value = t.value[3:]
        return t
    
    def t_RUBY (self, t):
        r'ruby.*'
        t.value = t.value[5:]
        return t
    
    def t_S (self, t):
        r's.*'
        t.value = t.value[2:]
        return t
    
    def t_SAMP (self, t):
        r'samp.*'
        t.value = t.value[5:]
        return t
    
    def t_SCRIPT (self, t):
        r'script.*'
        t.value = t.value[7:]
        return t
    
    def t_SECTION (self, t):
        r'section.*'
        t.value = t.value[8:]
        return t
    
    def t_SELECT (self, t):
        r'select.*'
        t.value = t.value[7:]
        return t
    
    def t_SMALL (self, t):
        r'small.*'
        t.value = t.value[6:]
        return t
    
    def t_SOURCE (self, t):
        r'source.*'
        t.value = t.value[7:]
        return t
    
    def t_SPAN (self, t):
        r'span.*'
        t.value = t.value[5:]
        return t
    
    def t_STRONG (self, t):
        r'strong.*'
        t.value = t.value[7:]
        return t
    
    def t_STYLE (self, t):
        r'style.*'
        t.value = t.value[6:]
        return t
    
    def t_SUB (self, t):
        r'sub.*'
        t.value = t.value[4:]
        return t
    
    def t_SUMMARY (self, t):
        r'summary.*'
        t.value = t.value[8:]
        return t
    
    def t_SUP (self, t):
        r'sup.*'
        t.value = t.value[4:]
        return t
    
    def t_TABLE (self, t):
        r'table.*'
        t.value = t.value[6:]
        return t
    
    def t_TBODY (self, t):
        r'tbody.*'
        t.value = t.value[6:]
        return t
    
    def t_TD (self, t):
        r'td.*'
        t.value = t.value[3:]
        return t
    
    def t_TEXTAREA (self, t):
        r'textarea.*'
        t.value = t.value[9:]
        return t
    
    def t_TFOOT (self, t):
        r'tfoot.*'
        t.value = t.value[6:]
        return t
    
    def t_TH (self, t):
        r'th.*'
        t.value = t.value[3:]
        return t 
    
    def t_THEAD (self, t):
        r'thead.*'
        t.value = t.value[6:]
        return t
    
    def t_TIME (self, t):
        r'time.*'
        t.value = t.value[5:]
        return t
    
    def t_TITLE (self, t):
        r'title.*'
        t.value = t.value[6:]
        return t
    
    def t_TR (self, t):
        r'tr.*'
        t.value = t.value[3:]
        return t
    
    def t_TRACK (self, t):
        r'track.*'
        t.value = t.value[6:]
        return t
    
    def t_TT (self, t):
        r'tt.*'
        t.value = t.value[3:]
        return t
    
    def t_U (self, t):
        r'u.*'
        t.value = t.value[2:]
        return t
    
    def t_UL (self, t):
        r'ul.*'
        t.value = t.value[3:]
        return t
    
    def t_VAR (self, t):
        r'var.*'
        t.value = t.value[4:]
        return t
    
    def t_VIDEO (self, t):
        r'video.*'
        t.value = t.value[6:]
        return t
    
    def t_WBR (self, t):
        r'wbr.*'
        t.value = t.value[4:]
        return t

   # Define a rule to match pipes
    def t_PIPE(self, t):
        r'\|'
        return t
    
    # Define a rule to match text
    def t_TEXT(self, t):
        r'[^\n\r|]+'
        return t
    
    # Define a rule to match script
    def t_SCRIPT(self, t):
        r'script'
        return t
    
    # Define a rule to match style
    def t_STYLE(self, t):
        r'style'
        return t
    
     # Define a rule to match tag names
    def t_TAG(self, t):
        r'[a-z0-9_-]+'
        return t
    
    # Define a rule to match class names
    def t_CLASS(self, t):
        r'\.[a-z0-9_-]+'
        t.value = t.value[1:]
        return t
    
    # Define a rule to match IDs
    def t_ID(self, t):
        r'#[a-z0-9_-]+'
        t.value = t.value[1:]
        return t
    
    # Define a rule to match attributes
    def t_ATTRIBUTE(self, t):
        r'[a-z0-9_-]+\s*=\s*'
        t.value = t.value[:-3]
        return t
    
    # Define a rule to match equals
    def t_EQUALS(self, t):
        r'='
        return t
    
    # Define a rule to match strings
    def t_STRING(self, t):
        r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''
        t.value = t.value[1:-1]
        return t
    
    # Define a rule to match booleans
    def t_BOOLEAN(self, t):
        r'true|false'
        return t
    
    # Define a rule to match numbers
    def t_NUMBER(self, t):
        r'\d+(\.\d+)?'
        return t
    
    # Define a rule to match null
    def t_NULL(self, t):
        r'null'
        return t
    
    # Define a rule to match undefined
    def t_UNDEFINED(self, t):
        r'undefined'
        return t
    
    # Define a rule to match include
    def t_INCLUDE(self, t):
        r'include'
        return t
    
    # Define a rule to match extends
    def t_EXTENDS(self, t):
        r'extends'
        return t
     
    # Define a rule to match block
    def t_BLOCK(self, t):
        r'block'
        return t
    
    # Define a rule to match mixin
    def t_MIXIN(self, t):
        r'mixin'
        return t
    
    # Define a rule to match plus
    def t_PLUS(self, t):
        r'\+'
        return t
    
    # Define a rule to match minus
    def t_MINUS(self, t):
        r'-'
        return t
    
    # Define a rule to match times
    def t_TIMES(self, t):
        r'\*'
        return t
    
    # Define a rule to match divide
    def t_DIVIDE(self, t):
        r'/'
        return t
    
    # Define a rule to match modulus
    def t_MODULUS(self, t):
        r'%'
        return t
    
    # Define a rule to match assign
    def t_ASSIGN(self, t):
        r':'
        return t
    
    # Define a rule to match left parenthesis
    def t_LPAREN(self, t):
        r'\('
        return t
    
    # Define a rule to match right parenthesis
    def t_RPAREN(self, t):
        r'\)'
        return t
    
    # Define a rule to match left brace
    def t_LBRACE(self, t):
        r'\{'
        return t
    
    # Define a rule to match right brace
    def t_RBRACE(self, t):
        r'\}'
        return t
    
    # Define a rule to match left bracket
    def t_LBRACKET(self, t):
        r'\['
        return t
    
    # Define a rule to match right bracket
    def t_RBRACKET(self, t):
        r'\]'
        return t
     
    # Define a rule to match DOT
    def t_DOT(self, t):
        r'\.'
        return t
    
    # Define a rule to match colon
    def t_COLON(self, t):
        r':'
        return t
    
    # Define a rule to match comma
    def t_COMMA(self, t):
        r','
        return t
     
    # Define a rule to match or
    def t_OR(self, t):
        r'\|\|'
        return t
    
    # Define a rule to match and
    def t_AND(self, t):
        r'&&'
        return t
    
    # Define a rule to match not
    def t_NOT(self, t):
        r'!'
        return t
    
    # Define a rule to match not equals
    def t_NOT_EQUALS(self, t):
        r'!='
        return t
    
    # Define a rule to match equals
    def t_EQUALS(self, t):
        r'=='
        return t
    
    # Define a rule to match greater than
    def t_GT(self, t):
        r'>'
        return t
    
    # Define a rule to match less than
    def t_LT(self, t):
        r'<'
        return t
    
    # Define a rule to match greater than or equal to
    def t_GTE(self, t):
        r'>='
        return t
    
    # Define a rule to match less than or equal to
    def t_LTE(self, t):
        r'<='
        return t
    
    # Define a rule to match if
    def t_IF(self, t):
        r'if'
        return t
    
    # Define a rule to match else
    def t_ELSE(self, t):
        r'else'
        return t
    
    # Define a rule to match else if
    def t_ELSEIF(self, t):
        r'else\s+if'
        return t
    
    # Define a rule to match for
    def t_FOR(self, t):
        r'for'
        return t
     
    # Define a rule to match while
    def t_WHILE(self, t):
        r'while'
        return t
    
    # Define a rule to match each
    def t_EACH(self, t):
        r'each'
        return t
    
    # Define a rule to match in
    def t_IN(self, t):
        r'in'
        return t
    
    # Define a rule to match return
    def t_RETURN(self, t):
        r'return'
        return t
    
    # Define a rule to match break
    def t_BREAK(self, t):
        r'break'
        return t
    
    # Define a rule to match continue
    def t_CONTINUE(self, t):
        r'continue'
        return t
    
    # Define a rule to match yield
    def t_YIELD(self, t):
        r'yield'
        return t
    
    # Define a rule to match case
    def t_CASE(self, t):
        r'case'
        return t
    
    # Define a rule to match when
    def t_WHEN(self, t):
        r'when'
        return t
    
    # Define a rule to match default
    def t_DEFAULT(self, t):
        r'default'
        return t
    
    # Define a rule to match switch
    def t_SWITCH(self, t):
        r'switch'
        return t
    
    # Define a rule to match try
    def t_TRY(self, t):
        r'try'
        return t
    
    # Define a rule to match catch
    def t_CATCH(self, t):
        r'catch'
        return t
    
    # Define a rule to match finally
    def t_FINALLY(self, t):
        r'finally'
        return t
    
    # Define a rule to match throw
    def t_THROW(self, t):
        r'throw'
        return t
    
    # Define a rule to match new
    def t_NEW(self, t):
        r'new'
        return t
    
    # Define a rule to match delete
    def t_DELETE(self, t):
        r'delete'
        return t
    
    # Define a rule to match typeof
    def t_TYPEOF(self, t):
        r'typeof'
        return t
    
    # Define a rule to match instanceof
    def t_INSTANCEOF(self, t):
        r'instanceof'
        return t
    
    # Define a rule to match void
    def t_VOID(self, t):
        r'void'
        return t
    
    # Define a rule to match this
    def t_THIS(self, t):
        r'this'
        return t
    
    # Define a rule to match super
    def t_SUPER(self, t):
        r'super'
        return t
    
    # Define a rule to match class
    def t_CLASS(self, t):
        r'class'
        return t
    
    # Define a rule to match extends
    def t_EXTENDS(self, t):
        r'extends'
        return t
    
    # Define a rule to match implements
    def t_IMPLEMENTS(self, t):
        r'implements'
        return t
    
    # Define a rule to match interface
    def t_INTERFACE(self, t):
        r'interface'
        return t
    
    # Define a rule to match package
    def t_PACKAGE(self, t):
        r'package'
        return t
    
    # Define a rule to match import
    def t_IMPORT(self, t):
        r'import'
        return t
    
    # Define a rule to match public
    def t_PUBLIC(self, t):
        r'public'
        return t
    
    # Define a rule to match private
    def t_PRIVATE(self, t):
        r'private'
        return t
    
    # Define a rule to match protected
    def t_PROTECTED(self, t):
        r'protected'
        return t
    
    # Define a rule to match static
    def t_STATIC(self, t):
        r'static'
        return t
    
    # Define a rule to match const
    def t_CONST(self, t):
        r'const'
        return t
    
    # Define a rule to match let
    def t_LET(self, t):
        r'let'
        return t
    
    # Define a rule to match var
    def t_VAR(self, t):
        r'var'
        return t
    
    # Define a rule to match function
    def t_FUNCTION(self, t):
        r'function'
        return t
    
    # Define a rule to match async
    def t_ASYNC(self, t):
        r'async'
        return t
    
    # Define a rule to match await
    def t_AWAIT(self, t):
        r'await'
        return t
    
    # Define a rule to match get
    def t_GET(self, t):
        r'get'
        return t
    
    # Define a rule to match set
    def t_SET(self, t):
        r'set'
        return t
    
    # Define a rule to match true
    def t_TRUE(self, t):
        r'true'
        return t
    
    # Define a rule to match false
    def t_FALSE(self, t):
        r'false'
        return t
    
    # Define a rule to match null
    def t_NULL(self, t):
        r'null'
        return t
    
    # Define a rule to match undefined
    def t_UNDEFINED(self, t):
        r'undefined'
        return t
    
    # Define a rule to match NaN
    def t_NAN(self, t):
        r'NaN'
        return t
    
    # Define a rule to match Infinity
    def t_INFINITY(self, t):
        r'Infinity'
        return t

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)


