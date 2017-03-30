"""Vector."""

import math


class Vector2(object):
    """Vector Class."""

    def __init__(self, xpos, ypos):
        """Initialize."""
        self.value = (xpos, ypos)
        self._xpos = self.value[0]
        self._ypos = self.value[1]

    def setx(self, value):
        """Set X."""
        self._xpos = value
        self.value = (value, self._ypos)

    def getx(self):
        """Return X."""
        return self.value[0]

    def sety(self, value):
        """Set Y."""
        self._ypos = value
        self.value = (self._xpos, value)

    def gety(self):
        """Return Y."""
        return self.value[1]

    xpos = property(getx, setx)
    ypos = property(gety, sety)

    def __str__(self):
        """Override string."""
        return "Position: " + str(self.xpos) + ", " + str(self.ypos)

    def __getitem__(self, key):
        """Override index."""
        return self.value[key]

    @property
    def magnitude(self):
        """Magnitude."""
        return self.get_mag()

    def get_mag(self):
        """Get magnitude."""
        sqrmag = self.xpos * self.xpos + self.ypos * self.ypos
        return math.sqrt(sqrmag)

    def __add__(self, other):
        """Add vector to vector."""
        return Vector2(self.xpos + other.xpos, self.ypos + other.ypos)

    def __sub__(self, other):
        """Subtract vector from vector."""
        return Vector2(self.xpos - other.xpos, self.ypos - other.ypos)

    def __mul__(self, other):
        """Multiply vector to vector."""
        return Vector2(self.xpos * other, self.ypos * other)

    @property
    def direction(self):
        """Direction."""
        return self.get_direction()

    def get_direction(self):
        """Get direction of vector."""
        v_mag = self.magnitude
        if v_mag == 0:
            return Vector2(0, 0)
        return Vector2(self.xpos / v_mag, self.ypos / v_mag)

    def get_dist(self, vector1, vector2):
        """Get_dist."""
        return (vector2.xpos - vector1.xpos, vector2.ypos - vector1.ypos)


if __name__ == '__main__':
    testv = Vector2(-25, -25)

    print testv * 20
