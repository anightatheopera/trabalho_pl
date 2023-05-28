#!/usr/bin/env python3

import argparse as arguments

from compiler import compile_pug 
import sys

def main(args):
    try:
        output = None
        if args.stdout:
            output = sys.stdout
        else:
            if args.output == "null":
                output = open(args.file.replace(".pug",".html"),"w")
            else:
                output = open(args.output,"w")
        if args.file:
            with open(args.file,"r") as f:
                pug_code = f.read()
                html_code = compile_pug(pug_code)
                output.write(html_code)

    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    parser = arguments.ArgumentParser(prog='pooh',description="Pooh compiler")
    parser.add_argument("file", type=str, help="Pug file to compile")
    parser.add_argument("output",default="null",nargs='?', type=str, help="Output file, defaults to [input_file.html]")
    parser.add_argument("-stdout", action="store_true", help="Output to stdout")
    args = parser.parse_args()
    main(args)
