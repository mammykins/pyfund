"""Generators in python can model data streams which can be composed into a pipeline.
They include the yield keyword"""


def lucas():
    """Similar to the Fibonacci but different starting numbers."""
    yield 2
    a = 2  # initialise a and b, holds previous value as it proceeds
    b = 1
    while True:  # runs forever! or until comp runs out of memory
        yield b
        a, b = a, a + b  # updated a and b using neat tuple unpacking


def main():
    for x in lucas():
        print(x)


if __name__ == '__main__':  # our module is being executed as a program
    main()
