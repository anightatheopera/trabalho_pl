#!/usr/bin/env python3

import argparse as arguments

import lexer, parsing
import compiler
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


BANNER = f"""{bcolors.OKGREEN}


         _               _                _                _       _  
        /\ \            /\ \             /\ \             / /\    / /\\
       /  \ \          /  \ \           /  \ \           / / /   / / /
      / /\ \ \        / /\ \ \         / /\ \ \         / /_/   / / / 
     / / /\ \_\      / / /\ \ \       / / /\ \ \       / /\ \__/ / /  
    / / /_/ / /     / / /  \ \_\     / / /  \ \_\     / /\ \___\/ /   
   / / /__\/ /     / / /   / / /    / / /   / / /    / / /\/___/ /    
  / / /_____/     / / /   / / /    / / /   / / /    / / /   / / /     
 / / /           / / /___/ / /    / / /___/ / /    / / /   / / /      
/ / /           / / /____\/ /    / / /____\/ /    / / /   / / /       
\/_/            \/_________/     \/_________/     \/_/    \/_/        
                                                                      
{bcolors.ENDC}"""


pug_code: str = None
html_code: str = None
output = None

def print_help():
    print(BANNER)
    print("Pooh compiler")
    print("Usage: pooh [input file] [output file]")
    print("Options:")
    print("  -h, --help         Show this help message and exit")
    print("  --test             Run tests")
    print("  --stdout           Output to stdout")

def main(args):
    if args.file == "null":
        if args.test:
            from testing import run_tests
            run_tests()
        else:
            print_help()
    else:
        if args.output == "null":
            if args.stdout:
                output = sys.stdout
            else:
                output = open(args.file.replace(".pug",".html"),"w")
        else:
            output = open(args.output,"w")

        with open(args.file,"r") as f:
            pug_code = f.readlines()
            pug_code = [line.rstrip() for line in pug_code]
            pug_code = "\n".join(pug_code)
            html_code = compiler.compile_pug(pug_code)
            output.write(html_code)


if __name__ == "__main__":
    parsing = arguments.ArgumentParser(prog='pooh',description=f"Pooh compiler")
    parsing.add_argument("file",nargs='?',default="null",metavar="input file", type=str, help="Pug file to compile")
    parsing.add_argument("output",default="null",nargs='?',metavar="output file", type=str, help="Output file, defaults to [input_file.html]")
    parsing.add_argument("-stdout", action="store_true", help="Output to stdout")
    parsing.add_argument("--test", action="store_true", help="Run tests")
    args = parsing.parse_args()
    main(args)
