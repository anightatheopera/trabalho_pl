
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DOT IDENTIFIER NEWLINE NONWHITESPACE PIPE SPACE START_LEFT_ANGLE_BRACKET WHITESPACEstart : inline\n             | literal\n             | pipedliteral : START_LEFT_ANGLE_BRACKET contenttag : IDENTIFIERws : SPACE\n          | WHITESPACEwss : wswss : wss wsword : IDENTIFIER\n            | NONWHITESPACEcontent : wordcontent : content wss\n               | content wordinline : tag ws contentinline : ws inlinepiped : PIPE contentpiped : PIPE wss contentpiped : piped NEWLINE PIPE contentblock_tag : tag DOT NEWLINE wss contentblock_tag : tag NEWLINE wss content NEWLINE wss content'
    
_lr_action_items = {'START_LEFT_ANGLE_BRACKET':([0,],[7,]),'PIPE':([0,12,],[8,22,]),'IDENTIFIER':([0,6,7,8,10,11,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,],[9,9,17,17,-6,-7,17,17,-12,-10,-11,17,17,-8,17,17,-13,-14,17,-9,17,]),'SPACE':([0,5,6,8,9,10,11,15,16,17,18,19,20,21,23,24,25,26,27,28,],[10,10,10,10,-5,-6,-7,10,-12,-10,-11,10,10,-8,10,10,-14,10,-9,10,]),'WHITESPACE':([0,5,6,8,9,10,11,15,16,17,18,19,20,21,23,24,25,26,27,28,],[11,11,11,11,-5,-6,-7,11,-12,-10,-11,11,11,-8,11,11,-14,11,-9,11,]),'$end':([1,2,3,4,10,11,14,15,16,17,18,19,21,23,24,25,26,27,28,],[0,-1,-2,-3,-6,-7,-16,-4,-12,-10,-11,-17,-8,-15,-13,-14,-18,-9,-19,]),'NEWLINE':([4,10,11,16,17,18,19,21,24,25,26,27,28,],[12,-6,-7,-12,-10,-11,-17,-8,-13,-14,-18,-9,-19,]),'NONWHITESPACE':([7,8,10,11,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,],[18,18,-6,-7,18,18,-12,-10,-11,18,18,-8,18,18,-13,-14,18,-9,18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'inline':([0,6,],[2,14,]),'literal':([0,],[3,]),'piped':([0,],[4,]),'tag':([0,6,],[5,5,]),'ws':([0,5,6,8,15,19,20,23,24,26,28,],[6,13,6,21,21,21,27,21,27,21,21,]),'content':([7,8,13,20,22,],[15,19,23,26,28,]),'word':([7,8,13,15,19,20,22,23,26,28,],[16,16,16,25,25,16,16,25,25,25,]),'wss':([8,15,19,23,26,28,],[20,24,24,24,24,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> inline','start',1,'p_start','lexer.py',46),
  ('start -> literal','start',1,'p_start','lexer.py',47),
  ('start -> piped','start',1,'p_start','lexer.py',48),
  ('literal -> START_LEFT_ANGLE_BRACKET content','literal',2,'p_literal_term','lexer.py',56),
  ('tag -> IDENTIFIER','tag',1,'p_identifier_term','lexer.py',64),
  ('ws -> SPACE','ws',1,'p_ws_term','lexer.py',73),
  ('ws -> WHITESPACE','ws',1,'p_ws_term','lexer.py',74),
  ('wss -> ws','wss',1,'p_wss_term','lexer.py',78),
  ('wss -> wss ws','wss',2,'p_wss_ws','lexer.py',82),
  ('word -> IDENTIFIER','word',1,'p_word_ident','lexer.py',90),
  ('word -> NONWHITESPACE','word',1,'p_word_ident','lexer.py',91),
  ('content -> word','content',1,'p_content_term','lexer.py',101),
  ('content -> content wss','content',2,'p_content_cont','lexer.py',105),
  ('content -> content word','content',2,'p_content_cont','lexer.py',106),
  ('inline -> tag ws content','inline',3,'p_inline_term','lexer.py',115),
  ('inline -> ws inline','inline',2,'p_inline_ident','lexer.py',119),
  ('piped -> PIPE content','piped',2,'p_piped_term','lexer.py',128),
  ('piped -> PIPE wss content','piped',3,'p_piped_wss','lexer.py',132),
  ('piped -> piped NEWLINE PIPE content','piped',4,'p_piped_pipe','lexer.py',136),
  ('block_tag -> tag DOT NEWLINE wss content','block_tag',5,'p_block_tag_term','lexer.py',146),
  ('block_tag -> tag NEWLINE wss content NEWLINE wss content','block_tag',7,'p_block_tag_term2','lexer.py',150),
]
