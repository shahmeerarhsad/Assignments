import stdio
import sys


# Returns the sum S(n) = 1 + 2 + ... + n, computed iteratively.

def sum_iter(n):
    sumiter = 0
    for i in range(1, n + 1):
        sumiter = sumiter + i
    return sumiter


# Returns the sum S(n) = 1 + 2 + ... + n, computed recursively.

def sum_rec(n):
    if n == 1:
        return 1
    if n > 1:
        return n + sum_rec(n - 1)


def _main():

    n = int(sys.argv[1])
    stdio.writeln(sum_iter(n))
    stdio.writeln(sum_rec(n))


if __name__ == '__main__':
    _main()
