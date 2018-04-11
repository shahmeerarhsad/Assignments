import stdio
import sys


# Returns the domain type of the given URL.
def domain_type(URL):
    a = URL.split('http://')
    a = a[1].split('/')
    a = a[0].split('.')
    s=''

    if(len(a) > 2):
        for i in range (2,len(a)):
            s = s + str(a[i]) + '.'
        return s[0:len(s)-1]
    else:
        return a[2]


# Test client [DO NOT EDIT]. Reads a URL as command-line argument and writes
# its domain type.
def _main():
    URL = sys.argv[1]
    stdio.writeln(domain_type(URL))

if __name__ == '__main__':
    _main()
