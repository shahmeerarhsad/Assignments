"""
markov_model.py

A data type that represents a Markov model of order k from a given text string.
"""

import stdio
import sys
import random


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Creates a Markov model of order k from given text. Assumes that text
        has length at least k.
        """

        self._k = k
        self._st = {}
        circ_text = text + text[:2]
        for i in range(len(circ_text) - k):
            x = circ_text[i:i+k]
            y = circ_text[i+k]
            self._st.setdefault(circ_text[i:i + k], {}).setdefault(circ_text[i+k], 0)
            self._st[x][y] += 1
    

    def order(self):
        """
        Returns order k of Markov model.
        """

        return self._k
    

    def kgram_freq(self, kgram):
        """
        Returns number of occurrences of kgram in text. Raises an error if
        kgram is not of length k.
        """
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if kgram in self._st:
            return sum(self._st[kgram].values())
        else:
            return 0

    def char_freq(self, kgram, c):
        """
        Returns number of times character c follows kgram. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if bool(c in self._st[kgram]):
            return self._st[kgram][c]
        else:
            return 0

    def rand(self, kgram):
        """
        Returns a random character following kgram. Raises an error if kgram
        is not of length k or if kgram is unknown.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)

        return random.choice(self._st[kgram].keys())

    def gen(self, kgram, T):
        """
        Generates and returns a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k characters of the
        generated string is the argument kgram. Assumes that T is at least k.
        """

        text = kgram
        for i in range(T - self._k):
            text += self.rand(kgram)
            kgram = text[-self._k:]
        return text


def _main():
    """
    Test client [DO NOT EDIT].
    """
    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
