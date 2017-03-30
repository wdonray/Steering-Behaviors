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
        self.heading = Vec2(0, 0)
        self.direction = self.velocity.direction
        self.surface = pygame.Surface((45, 25), pygame.SRCALPHA)
        #pygame.draw.circle(self.surface, (125, 125, 255), (10, 10), 10, 0)
        pygame.draw.lines(self.surface, random.choice((BLACK, BLUE, PINK, MAROON, GREEN)),
                          True, [(1, 1), (15, 25), (25, 1)], 2)
        pygame.draw.circle(self.surface, RED, (25, 3), 3)
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
        textpos = "Pos: <{:0.5}{}{:1.5}>".format(
            self.pos.xpos, ", ", self.pos.ypos)
        surfacep = self.font.render(textpos, True, (0, 0, 0))
        screen.blit(surfacep, (self.pos.xpos - 50, self.pos.ypos + 50))

        targetpos = "TargetPos: <{0:.5} {1:.5}>".format(
            str(self.targetpos.xpos), str(self.targetpos.ypos))
        surfacet = self.font.render(targetpos, True, (0, 0, 0))
        screen.blit(surfacet, (self.pos.xpos - 50, self.pos.ypos + 60))

        velpos = "Velocity: <{0:.5} {1:.5}>".format(
            str(self.velocity.xpos), str(self.velocity.ypos))
        surfacev = self.font.render(velpos, True, (0, 0, 0))
        screen.blit(surfacev, (self.pos.xpos - 50, self.pos.ypos + 70))

        rotate = pygame.transform.rotate(
            self.surface, -180 * math.atan2(self.heading[1], self.heading[0]) / math.pi)
        self.heading = Vec2.get_direction(self.velocity)

        screen.blit(rotate, (self.pos.xpos, self.pos.ypos))

    def updateseek(self, deltatime):
        """Update gameobject logic."""
        self.acceleration = self.force + self.seek(self.targetpos)
        self.velocity = self.velocity + self.acceleration * deltatime
        self.direction = self.velocity.direction
        self.pos = self.pos + self.velocity * deltatime
        # if (int(self.pos.xpos) == self.targetpos.xpos and
        # int(self.pos.ypos) == self.targetpos.ypos):

    def updateflee(self, deltatime):
        """Update gameobject logic."""
        self.acceleration = self.force + self.flee(self.targetpos)
        self.velocity = self.velocity + self.acceleration * deltatime
        self.direction = self.velocity.direction
        self.pos = self.pos + self.velocity * deltatime
