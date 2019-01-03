import sys


def sqrt(x):
    """Compute square roots using hte method of Heron of Alexandria.

    Args
    ----
    x: The number for which the square root is to be computed.

    Returns
    -------
    The square root of x.

    Raises
    ------
    ValueError: If x is negative.

    """
    if x < 0:
        raise ValueError("Cannot compute square root "
                         "of negative numbers {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    """Illustrate function level and exceptions."""
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Programm execution continues normally here.")


if __name__ == "__main__":
    main()
