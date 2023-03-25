"""
Annotation tool specific argument usage and parsing
"""

import sys
import logging
import textwrap
import getopt


def usage():
    """
    Tool specific usage
    :return: None, just print usage and exit
    """
    logging.error("Missing Required Parameters!")
    print(textwrap.dedent('''
            DESCRIPTION:
            Annotate genomic variants. Supports various formats as input and output.

            EXAMPLE USAGE:
            python genovariant.py annotate -i input.vcf.gz -o output.vcf.gz -c annotations.cfg
            OPTIONS:
            -i,--input           Input variants file (required)
            -o,--output          Output file containing annotated variants (required)
            -f,--format_out      Output format {vcf, tab, json}. Default: vcf
            -c,--config          Config in json format containing annotation info.
            -h,--help            Help message
            '''))
    sys.exit(2)


def parse_args(args):
    """
    Parse tool specific args
    :param args: list of arguments
    :return: dict of parsed args
    """
    try:
        opts, args = getopt.getopt(args[2:], "hi:o:f:c:",
                                   ["help", "input=", "output=", "format=", "config="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
        # Default Params
    extra_annotations = list()
    params = {'input_file': None, 'output_file': None}
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-i", "--input"):
            params['input_file'] = a
        elif o in ("-o", "--output"):
            params['output_file'] = a
        elif o in ("-f", "--format"):
            params['format'] = a
        elif o in ("-c", "--config"):
            params['config_file'] = a
        else:
            usage()
    # required parameters
    if not params['input_file'] or not params['output_file']:
        usage()

    return params
