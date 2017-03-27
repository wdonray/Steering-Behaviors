"""Vector."""

import math


class Vector2(object):
    """Vector Class."""

    def __init__(self, xpos, ypos):
        """Initialize."""
        self.value = (xpos, ypos)
        self.xpos = self.value[0]
        self.ypos = self.value[1]

    def __str__(self):
        return "Position: " + str(self.xpos) + ", " + str(self.ypos)

    def __getitem__(self, key):
        '''override index'''
        return self.value[key]

    @property
    def magnitude(self):
        '''magnitude'''
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
        '''aaa'''
        return self.get_direction()

    def get_direction(self):
        """Get direction of vector."""
        v_mag = self.magnitude
        return Vector2(self.xpos / v_mag, self.ypos / v_mag)

    def get_dist(self, vector1, vector2):
        """Get_dist."""
        return (vector2[0] - vector1[0], vector2[1] - vector1[1])

if __name__ == '__main__':
    testv = Vector2(-25, -25)

    print testv * 20