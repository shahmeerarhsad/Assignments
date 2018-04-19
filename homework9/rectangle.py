import stdio
import sys
from interval import Interval


class Rectangle:
    """
    Represents a rectangle as two (x and y) intervals.
    """

    def __init__(self, xint, yint):
        """
        Constructs a new rectangle given the x and y intervals.
        """

        self._xint = xint
        self._yint = yint

    def area(self):
        """
        Returns the area of self.
        """
        area = (self._xint.rbound() - self._xint.lbound()) \
            * (self._yint.rbound() - self._yint.lbound())
        return area

    def perimeter(self):
        """
        Returns the perimeter of self.
        """
        perimeter = 2*((self._xint.rbound() - self._xint.lbound())
                       + (self._yint.rbound() - self._yint.lbound()))
        return perimeter

    def contains(self, x, y):
        """
        Returns True if self contains the point (x, y) and False otherwise.
        """
        if x > self._xint.lbound() and x < self._xint.rbound() and \
                y > self._yint.lbound() and y < self._yint.rbound():
            return True
        else:
            return False

    def intersects(self, other):
        """
        Returns True if self intersects other and False othewise.
        """

        if other._xint.lbound() > self._xint.rbound() or \
                other._yint.lbound() > self._yint.rbound() \
                or self._xint.lbound() > other._xint.rbound() \
                or self._yint.lbound() > other._yint.rbound():
            return False
        else:
            return True

    def __str__(self):
        """
        Returns a string representation of self.
        """

        return '%s x %s' % (self._xint, self._yint)


# Test client [DO NOT EDIT]. Reads a floats x and y from the command line and
# writes to standard output: all of the rectangles from standard input
# (each defined by two pairs of floats) that contain (x, y); and all pairs
# of rectangles from standard input that intersect one another.
def _main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    rectangles = []
    while not stdio.isEmpty():
        lbound1 = stdio.readFloat()
        rbound1 = stdio.readFloat()
        lbound2 = stdio.readFloat()
        rbound2 = stdio.readFloat()
        rectangles += [Rectangle(Interval(lbound1, rbound1),
                                 Interval(lbound2, rbound2))]
    for i in range(len(rectangles)):
        stdio.writef('Area(%s) = %f\n', rectangles[i], rectangles[i].area())
        stdio.writef('Perimeter(%s) = %f\n', rectangles[i],
                     rectangles[i].perimeter())
        if rectangles[i].contains(x, y):
            stdio.writef('%s contains (%f, %f)\n', rectangles[i], x, y)
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].intersects(rectangles[j]):
                stdio.writef('%s intersects %s\n',
                             rectangles[i], rectangles[j])


if __name__ == '__main__':
    _main()
