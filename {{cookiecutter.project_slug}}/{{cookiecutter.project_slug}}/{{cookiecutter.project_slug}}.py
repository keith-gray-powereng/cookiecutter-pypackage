# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import sys


def main():
    parser = ArgumentParser(
        description='{{ cookiecutter.project_short_description }}'
    )

    # Build the command line argument parser here

    args = parser.parse_args()


if __name__ == '__main__':
    sys.exit(main())
