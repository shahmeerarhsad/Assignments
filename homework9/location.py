import math
import stdio
import sys


class Location:
    """
    Represents a location on Earth.
    """

    def __init__(self, lat, lon):
        """
        Constructs a new location given its latitude and longitude values.
        """

        self._lat = lat
        self._lon = lon

    def distanceTo(self, other):
        """
        Returns the great-circle distance between self and other.
        """
        x1 = math.radians(self._lat)
        y1 = math.radians(self._lon)
        x2 = math.radians(other._lat)
        y2 = math.radians(other._lon)
        d = math.acos(math.sin(x1)*math.sin(x2) +
                      math.cos(x1)*math.cos(x2)*math.cos(y1 - y2))
        d = math.degrees(d)
        return d*111

    def __str__(self):
        """
        Returns a string representation of self.
        """
        return '(%s, %s)' % (self._lat, self._lon)


# Test client [DO NOT EDIT]. Reads floats lat1, lon1, lat2, lon2 from command
# representing two locations on Earth, constructs two Location objects from
# them, and writes them along with the great-circle distance between the two.
def _main():
    lat1, lon1, lat2, lon2 = map(float, sys.argv[1:])
    loc1 = Location(lat1, lon1)
    loc2 = Location(lat2, lon2)
    stdio.writeln('loc1 = ' + str(loc1))
    stdio.writeln('loc2 = ' + str(loc2))
    stdio.writeln('d(loc1, loc2) = ' + str(loc1.distanceTo(loc2)))


if __name__ == '__main__':
    _main()
