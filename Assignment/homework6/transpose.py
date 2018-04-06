import stdarray
import stdio
from numpy import matrix
import sys


# Return a new 2D list representing the transpose of the matrix represented
# by the given 2D list a. Note that the a need not have the same number of
# rows and columns.
def transpose(a):
    # Get the dimensions of matrix a.
    m = len(a)
    n = len(a[0])

    # Create an n-by-m matrix c with all elements initialized to 0.0.
    c = [0.0] * n
    for i in range(n):
        c[i] = [0.0] * m

    # Fill in the elements of c such that c[i][j] = a[j][i].
    for i in range(n):
        for j in range(m):
            c[i][j] = a[j][i]

    # Return c.
    return c

# Test client [DO NOT EDIT]. Reads an m-by-n matrix from standard input and
# prints its transpose.


def _main():

    a = stdarray.readFloat2D()
    c = transpose(a)
    for row in c:
        for v in row[:-1]:
            stdio.write(str(v) + ' ')
        stdio.writeln(row[-1])


if __name__ == '__main__':
    _main()
