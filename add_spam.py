#!/usr/bin/env python3
"""Add spam to a menu.

Usage:

    add_spam.py --menu <MENU>
"""


import argparse
parser = argparse.ArgumentParser(description="Add spam to your menu.")
parser.add_argument('-m', '--menu', nargs='+', help='<Required> the menu as a\
 list that you want to add spam to', required=True)

args = parser.parse_args()


def add_spam(menu=None):
    """Print each word from a menu plus spam.

    Args:
        menu: The base menu.
    """
    if menu is None:  # kinda redundant as we require menu
        menu = []  # this avoids spamming! [spam, spam, spam etc.]
    menu.append('spam')
    return menu


def main(menu):
    """Print the modified menu.

    Args:
        menu: The menu to add spam to.
    """
    words = add_spam(menu)
    print(words)


if __name__ == '__main__':
    try:  # argparse treats the options we give it as strings
        main(menu=args.menu)  # args is an entire namespace, we require menu
    except IndexError:
        main(menu=None)  # if there is no command line input we default
