__file__ = 'pug2html_main'
__config__ = '.config'

VERSION:str = '0.0.1'
DESCRIPTION:str = 'Pug2Html - Convert Pug to Html'

from argparse import ArgumentParser, Namespace



def main(args: Namespace) -> None:
    pass

if __name__ == '__main__':

    parser:ArgumentParser = ArgumentParser()
    parser.add_argument('input',action='store', help='input directory [pug_files/index.pug]')
    parser.add_argument('output',action='store', help='output directory [html_files/index.html]')
    parser.add_argument('-v', '--version', action='version', version=f'{DESCRIPTION} Ver.{VERSION}')
    main(parser.parse_args())