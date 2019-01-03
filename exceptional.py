"""A module for demonstrating exceptions"""

import sys
from math import log

def convert(s):
    """Convert to integer."""
    x = -1
    try:
        x = int(s)
        # print("Conversion succeeded! x =", x)
    except (ValueError, TypeError):  # can accept tuple of types
        # print("Conversion failed!")
        pass  # syntactically permissable, semantically empty
    return x


def convert2(s):
    """Convert to integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
              file=sys.stderr)  # C like behaviour
        return -1  # unpythonic, negative error code, better to raise error


def convert3(s):
    """Convert to integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
              file=sys.stderr)  # C like behaviour
        raise


def string_log(s):
    """Convert to integer and log."""
    v = convert(s)
    return log(v)
