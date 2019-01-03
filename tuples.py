#!/usr/bin/env python3
"""Return min and max of a ints, learning about tuples.

Usage:

    tuple.py -q <QUESTION>
"""


import argparse
parser = argparse.ArgumentParser(description="Get min and max of a tuple.")
parser.add_argument('-q', '--question', nargs='+', help='<Required> A\
 tuple', required=True)

args = parser.parse_args()


def minmax(question=None):
    """Find the min and max of a tuple.

    Args:
        question: A tuple of interest.
    """
    lower, upper = min(question), max(question)  # tuples unpacking
    return lower, upper


def main(question):
    """Print the min and max.

    Args:
        question: The tuple to get the min and max from.
    """
    words = minmax(question)
    print("The lower is ", words[0], "\n",  # zero index from tuple
          "The upper is ", words[1])  # use square bracket to index


if __name__ == '__main__':
    main(question=tuple(args.question))  # args is an entire namespace, need .
