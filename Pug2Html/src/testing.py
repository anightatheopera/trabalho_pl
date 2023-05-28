#!/usr/bin/env python3
from lexer import run_lexer_tests
from parsing import run_parser_tests
from compiler import run_compiler_tests

def run_tests():
    print("Lexer tests:\n")
    run_lexer_tests()
    print("\n----------------------------------------\n")
    print("Parser tests:\n")
    run_parser_tests()
    print("\n----------------------------------------\n")
    print("Compiler tests:\n")
    run_compiler_tests()

if __name__ == "__main__":
    run_tests()
