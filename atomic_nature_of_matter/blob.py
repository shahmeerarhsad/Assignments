import math
class Blob:
    """
    Represents a blob.
    """

    def __init__(self):
        """
        Constructs an empty blob.
        """

        self._P = 0 # number of pixels
        self._x = 0.0  # x-coordinate of center of mass
        self._y = 0.0  # y-coordinate of center of mass

    def add(self, i, j):
        """
        Adds pixel (i, j) to this blob.
        """
        self._x += i
        self._y += j
        self._P += 1


    def mass(self):
        """
        Returns the number of pixels added to this blob, ie, its mass.
        """
        return self._P


    def distanceTo(self, other):
        """
        Returns the Euclidean distance between the center of mass of this blob
        and the center of mass of other blob.
        """
        doublecx = self._x * 1.0/ self._P * 1.0
        doublecy = self._y * 1.0/ self._P * 1.0
        otherdoublecx = other._x * 1.0/ other._P * 1.0
        otherdoublecy = other._y * 1.0/ other._P * 1.0
        return math.sqrt(math.pow((otherdoublecx - doublecx), 2) + math.pow(otherdoublecy - doublecy, 2))


    def __str__(self):
        """
        Returns a string representation of this blob.
        """

        return '%d (%.4f, %.4f)' % (self._P, self._x*1.0/self._P*1.0, self._y*1.0/self._P*1.0)


def _main():
    b = Blob()
    b.add(4, 3)
    b.add(3, 3)
    b.add(3, 6)
    t = Blob()
    t.add(8, 4)
    t.add(0, 3)
    t.add(23, 2)
    print(b)
    print(t)
    print(b.distanceTo(t))


if __name__ == '__main__':
    _main()