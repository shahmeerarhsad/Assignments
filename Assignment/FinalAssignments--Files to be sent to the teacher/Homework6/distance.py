import stdio
import sys
from math import sqrt
# Return the Euclidean distance between x and y, calculated as as the square
# root of the sums of the squares of the differences between corresponding
# entries. You may assume that x and y have the same length.


def distance(x, y):
        if len(x) != len(y):
            raise Exception('Data sets must be the same dimension')
        dimension = len(x)
        sum = 0
        for dim in range(0, dimension):
            sum += (x[dim] - y[dim]) ** 2

        return sqrt(sum)

# Test client [DO NOT EDIT]. Reads an integer n as command-line argument, and
# then calculates and prints the Euclidean distance between two n-dimensional
# vectors read from standard input.


def _main():
    n = int(sys.argv[1])
    x = [stdio.readFloat() for i in range(n)]
    y = [stdio.readFloat() for i in range(n)]
    stdio.writeln(distance(x, y))


if __name__ == '__main__':
    _main()
