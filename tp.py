import ply.lex as lex

class PugLexer:
    def __init__(self):
        self.lexer = lex.lex(module=self)
    
    # List of token names.   This is always required
    tokens = (
        'COMMENT',
        'PIPE',
        'TEXT',
        'SCRIPT',
        'STYLE',
        'TAG',
        'CLASS',
        'ID',
        'ATTRIBUTE',
        'EQUALS',
        'STRING',
        'BOOLEAN',
        'NUMBER',
        'NULL',
        'UNDEFINED',
        'INCLUDE',
        'EXTENDS',
        'BLOCK',
        'MIXIN',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'MODULUS',
        'ASSIGN',
        'LPAREN',
        'RPAREN',
        'LBRACE',
        'RBRACE',
        'LBRACKET',
        'RBRACKET',
        'DOT',
        'COLON',
        'COMMA',
        'OR',
        'AND',
        'NOT',
        'EQ',
        'NEQ',
        'LT',
        'LTE',
        'GT',
        'GTE',
        'IF',
        'ELSE',
        'UNLESS',
        'CASE',
        'WHEN',
        'DEFAULT',
        'EACH',
        'FOR',
        'IN', 
        'ATTR_OPEN',
        'ATTR_CLOSE',
        'TRUE',
        'FALSE',
        'NULL_LITERAL',
        'UNDEFINED_LITERAL',
        'BLOCK_OPEN',
        'BLOCK_CLOSE',
        'MIXIN_CALL',
        'EXTEND',
        'YIELD',
        'SLASH',
        'NEWLINE'
    )
         
    
    # Regular expression rules for tokens
    t_COMMENT = r'\/\/.*'
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
        r'\/\/.*'
        pass
        # No return value. Token discarded
         
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
    
    # Define a rule https://prod.liveshare.vsengsaas.visualstudio.com/join?8EDBA06EC0CBAC6A744F37588212A175C1F1(self, t):
        r'\]'
        return t
     
    # Define a rule to match dot
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
    
     
     
        