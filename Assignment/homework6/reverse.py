import stdio
import sys


# Reverse the one-dimensional list a in place, ie, without creating a new list.
def reverse(a):
    # Iterate over half of the list a. Exchange element at i in a with the
    # element at len(a) - i - 1.
    for i in range(0, int(len(a) / 2)):
        if a[i] != a[len(a) - i - 1]:
            temp = a[i]
            a[i] = a[len(a) - i - 1]
            a[len(a) - i - 1] = temp

    return a

# Test client [DO NOT EDIT]. Reads strings from standard input into a list,
# reverses the list, and prints the reversed list.


def _main():
    a = stdio.readAllStrings()
    reverse(a)
    for v in a[:-1]:
        stdio.writef('%s ', v)
    stdio.writeln(a[-1])


if __name__ == '__main__':
    _main()
