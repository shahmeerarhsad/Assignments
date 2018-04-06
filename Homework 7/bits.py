import stdio
import sys


# Return the number of zeros in s, computed recursively.


def zeros(s):
    zero = "0"
    return ((zero == s[0]) + zeros(s[1:])) if s else 0


# Return the number of ones in s, computed recursively.


def ones(s):
    one = "1"
    return ((one == s[0]) + ones(s[1:])) if s else 0


# Test client [DO NOT EDIT]. Reads a string s from command line and writes the
# the number of zeros and ones in s, both computed recursively.


def _main():
    s = sys.argv[1]
    stdio.writef('zeros = %d, ones = %d, total = %d\n',
                 zeros(s), ones(s), len(s))


if __name__ == '__main__':
    _main()
