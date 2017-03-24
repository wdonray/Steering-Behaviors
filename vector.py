"""Vector."""

import math


def get_normilized(vector):
    """Get_normilized."""
    return vector[0] / get_mag(vector), vector[1] / get_mag(vector)


def get_mag(vector):
    """Get magnitude."""
    return math.sqrt((vector[0] * vector[0]) + (vector[1] * vector[1]))


def get_dist(vector1, vector2):
    """Get_dist."""
    return (vector2[0] - vector1[0], vector2[1] - vector1[1])
