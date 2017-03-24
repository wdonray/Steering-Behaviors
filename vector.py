"""Vector."""

import math


class Vector2(object):
    """Vector Class."""

    def __init__(self, xpos, ypos):
        """Initialize."""
        self.value = (xpos, ypos)
        self.xpos = self.value[0]
        self.ypos = self.value[1]

    def get_normilized(self, vector):
        """Get_normilized."""
        return vector[0] / self.get_mag(vector), vector[1] / self.get_mag(vector)

    def get_mag(self, vector):
        """Get magnitude."""
        return math.sqrt((vector[0] * vector[0]) + (vector[1] * vector[1]))

    def __add__(self, other):
        """Add vector to vector."""
        return Vector2(self.xpos + other.xpos, self.ypos + other.ypos)

    def __sub__(self, other):
        """Subtract vector from vector."""
        return Vector2(self.xpos - other.xpos, self.ypos - other.ypos)

    def __mul__(self, other):
        """Multiply vector to vector."""
        return Vector2(self.xpos * other, self.ypos * other)

    def get_direction(self):
        """Get direction of vector."""
        v_mag = self.get_mag
        return Vector2(self.xpos / v_mag, self.ypos / v_mag)

    def get_dist(self, vector1, vector2):
        """Get_dist."""
        return (vector2[0] - vector1[0], vector2[1] - vector1[1])
