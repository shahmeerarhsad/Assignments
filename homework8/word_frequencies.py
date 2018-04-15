import operator
import stdio
import sys


# Returns a list containing the keys of the dictionary st in reverse order
# of the values of the dictionary.
def keys(st):
    a = sorted(st.items(), key=operator.itemgetter(1), reverse=True)
    return [v[0] for v in a]


# Returns a dictionary whose keys are the words from the given list of words
# and values are the corresponding frequencies.
def count_word_frequencies(words):
    n = len(words)
    d = {}
    for i in range(n):
        if words[i] not in d:
            d[words[i]] = 0
        d[words[i]] += 1
    return d


# Writes (in reverse order of values) the key-value pairs of the dictionary
# st to standard output, one per line, and with a ' -> ' between a key and
# the corresponding value.
def write_word_frequencies(st):
    reverse_st = keys(st)
    for i in range(len(reverse_st)):
        stdio.writef('%s -> %s\n', reverse_st[i], st[reverse_st[i]])


# Test client [DO NOT EDIT]. Reads words from standard input and writes
# the words along with their frequencies, in reverse order of frequencies.
def _main():
    words = stdio.readAllStrings()
    write_word_frequencies(count_word_frequencies(words))


if __name__ == '__main__':
    _main()
