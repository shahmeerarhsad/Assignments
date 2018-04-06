import stdio
import sys


# Returns a to the power b, computed recursively.
def power(a, b):
    if b == 0:
        return 1
    else:
        if b % 2 == 0:
            return (a**2)**(b/2)
        else:
            if b % 2 != 0:
                return a * (a ** (b - 1))

# Test client [DO NOT EDIT]. Reads integers a and b from command line and
# writes the value of a to the power b, computed recursively.


def _main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    stdio.writeln(power(a, b))


if __name__ == '__main__':
    _main()
