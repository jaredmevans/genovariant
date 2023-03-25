"""
Main module and entry point for GenoVariant package.
The GenoVariant package contains a suite of easy to use tools for annotating, filtering, and storing genomic variants.

@author: Jared Evans https://github.com/jaredmevans
"""

import sys
import logging
import textwrap
import getopt
from annotate.args import parse_args as parse_annotate
from annotate.annotate import run_annotation as run_annotate
from __init__ import package
from __init__ import version


def usage():
    """
    print general argument usage info
    :return: None, just print usage info and exit
    """
    logging.error("Missing Required Parameters!")
    print(textwrap.dedent('''
            DESCRIPTION:
            The GenoVariant package contains a suite of easy to use tools for annotating, 
            filtering, and storing genomic variants.

            EXAMPLE USAGE:
            python genovariant.py [TOOL] [OPTIONS]
            TOOL:
            annotate          Annotate variants 
            OPTIONS:
            -v,--version      Display version and exit
            -h,--help         Help message. Add tool name to get tool specific help.
            '''))
    sys.exit(2)


def parse_args(args):
    """
    Parse commandline arguments
    :param args: arguments
    :return: dict of parsed args
    """
    tool_arg_parse = {"annotate": parse_annotate}
    tool = None
    params = {}
    if len(args) > 1:
        # get requested tool
        if args[1] in tool_arg_parse:
            tool = args[1]
    else:
        usage()

    # Parse args based on requested tool
    if tool in tool_arg_parse:
        params = tool_arg_parse[tool](args)
    else:
        try:
            opts, args = getopt.getopt(args[1:], "hv", ["help", "version"])
        except getopt.GetoptError as err:
            logging.error(str(err))
            usage()
            sys.exit(2)
        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
            elif o in ("-v", "--version"):
                print(package + " version " + str(version))
                sys.exit(2)
            else:
                # no arguments given
                usage()
    params['tool'] = tool
    return params


def main():
    # set default logging
    logging.basicConfig(format='%(levelname)s\t%(asctime)s - %(message)s', level=logging.INFO)

    # parse arguments
    params = parse_args(sys.argv)

    logging.info(package + " v" + str(version) + " " + str(params['tool']) + " Started")

    # run requested tool
    tools = {"annotate": run_annotate}
    if params['tool'] in tools:
        tools[params['tool']](params)
    else:
        logging.error("Tool Not Recognized: " + str(params['tool']))

    logging.info(package + " v" + str(version) + " " + str(params['tool']) + " Finished")


if __name__ == '__main__':
    sys.exit(main())
