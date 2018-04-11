import stdio
import sys


# Returns the Watson-Crick complement of the given DNA string.
def wc_complement(dna):
    s = ''  # the wc complement of dna
    for c in dna:
        if c == 'A':
            s += 'T'
        elif c == 'T':
            s += 'A'
        elif c == 'G':
            s += 'C'
        else:
            s += 'G'
    return s


# Test client [DO NOT EDIT]. Reads a DNA string as command-line argument and
# writes its Watson-Crick complement.
def _main():
    dna = sys.argv[1]
    stdio.writeln(wc_complement(dna.upper()))

if __name__ == '__main__':
    _main()
