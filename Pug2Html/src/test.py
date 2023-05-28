#!/usr/bin/env python3

from lexer import lexer, run_lexer_tests
from parse import parser, run_parser_tests
from compiler import run_compiler_tests

print("Lexer tests:\n")
run_lexer_tests()
print("\n----------------------------------------\n")
print("Parser tests:\n")
run_parser_tests()
print("\n----------------------------------------\n")
print("Compiler tests:\n")
run_compiler_tests()
