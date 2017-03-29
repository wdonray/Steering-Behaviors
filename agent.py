"""Steering Behaviors."""

import random

import pygame

from gametemplate import *
from constants import *
from vector import Vector2 as Vec2
from vector import *

random.seed()

# pylint: disable=E1121
# pylint: disable=E1101


class Agent(object):
    """Agent_list."""

    def __init__(self, position):
        """Initialize."""
        self.pos = position
        self.velocity = Vec2(0, 0)
        self.acceleration = Vec2(0, 0)
        self.targetpos = Vec2(0, 0)
        self.force = Vec2(0, 0)
        self.mass = 1
        self.direction = self.velocity.direction
        self.surface = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, (125, 125, 255), (10, 10), 10, 0)
        self.font = pygame.font.SysFont('mono', 12)


    def set_target(self, target):
        """Set Target."""
        self.targetpos = Vec2(target[0], target[1])

    def addforce(self, force):
        """Add a force."""
        self.force += force

    def seek(self, target):
        """Seek Behavior."""
        max_velocity = 200
        displacement = target - self.pos
        force = displacement.direction * max_velocity
        seekforce = force - self.velocity
        return seekforce

    def flee(self, target):
        """Flee Behavior."""
        max_velocity = 200
        displacement = target - self.pos
        force = displacement.direction * max_velocity * -1
        fleeforce = force - self.velocity
        return fleeforce

    def wander(self, radius, dist, jitter, strength):
        """Wander Behavior."""
        pass

    def draw(self, screen):
        """Draw the gameobject."""
        textpos = "Pos: <{0:.5} {1:.5}>".format(
            self.pos.xpos, self.pos.ypos)
        surface = self.font.render(textpos, True, (0, 0, 0))
        screen.blit(surface, (self.pos.xpos, self.pos.ypos + 25))
        screen.blit(self.surface, (self.pos.xpos, self.pos.ypos))

    def updateseek(self, deltatime):
        """Update gameobject logic."""
        self.acceleration = self.force + self.seek(self.targetpos)
        self.velocity = self.velocity + self.acceleration * deltatime
        self.direction = self.velocity.direction
        self.pos = self.pos + self.velocity * deltatime

    def updateflee(self, deltatime):
        """Update gameobject logic."""
        self.acceleration = self.force + self.flee(self.targetpos)
        self.velocity = self.velocity + self.acceleration * deltatime
        self.direction = self.velocity.direction
        self.pos = self.pos + self.velocity * deltatime
