#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Options
"""

from argparse import ArgumentParser

import shlex
import six


def build_argument_parser():
    """
    Builds the argument parser
    :return: the argument parser
    :rtype: ArgumentParser
    """
    opts = ArgumentParser()
    opts.add_argument(dest='filename', help='Filename or release name to guess', nargs='*')

    naming_opts = opts.add_argument_group("Naming")
    #naming_opts.add_argument('-t', '--type', dest='type', default=None,
    #                         help='The suggested file type: movie, episode. If undefined, type will be guessed.')
    naming_opts.add_argument('-Y', '--date-year-first', action='store_true', dest='date_year_first', default=None,
                             help='If short date is found, consider the first digits as the year.')
    naming_opts.add_argument('-D', '--date-day-first', action='store_true', dest='date_day_first', default=None,
                             help='If short date is found, consider the second digits as the day.')
    naming_opts.add_argument('-L', '--allowed-languages', action='append', dest='allowed_languages',
                             help='Allowed language (can be used multiple times)')

    output_opts = opts.add_argument_group("Output")
    output_opts.add_argument('-v', '--verbose', action='store_true', dest='verbose', default=False,
                             help='Display debug output')
    output_opts.add_argument('-P', '--show-property', dest='show_property', default=None,
                             help='Display the value of a single property (title, series, videoCodec, year, ...)')
    output_opts.add_argument('-u', '--unidentified', dest='unidentified', action='store_true', default=False,
                             help='Display the unidentified parts.')
    output_opts.add_argument('-a', '--advanced', dest='advanced', action='store_true', default=False,
                             help='Display advanced information for filename guesses, as json output')
    output_opts.add_argument('-j', '--json', dest='json', action='store_true', default=False,
                             help='Display information for filename guesses as json output')
    output_opts.add_argument('-y', '--yaml', dest='yaml', action='store_true', default=False,
                             help='Display information for filename guesses as yaml output (like unit-test)')
    output_opts.add_argument('-f', '--input-file', dest='input_file', default=False,
                             help='Read filenames from an input file.')

    information_opts = opts.add_argument_group("Information")
    information_opts.add_argument('-p', '--properties', dest='properties', action='store_true', default=False,
                                  help='Display properties that can be guessed.')
    information_opts.add_argument('-V', '--values', dest='values', action='store_true', default=False,
                                  help='Display property values that can be guessed.')
    information_opts.add_argument('--version', dest='version', action='store_true', default=False,
                                  help='Display the guessit version.')

    return opts


def parse_options(options):
    """
    Parse given option string
    :param options:
    :type options:
    :return:
    :rtype:
    """
    if isinstance(options, six.text_type):
        args = shlex.split(options)
        options = vars(argument_parser.parse_args(args))
    if options is None:
        options = {}
    return options

argument_parser = build_argument_parser()
