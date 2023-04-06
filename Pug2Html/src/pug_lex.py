from ply.lex import lex

class PugLexer(object):
    tokens = ((),)
    

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)