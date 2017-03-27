"""Steering Behaviors."""

import random

import pygame

from vector import Vector2 as Vec2

from vector import *

random.seed()


class Agent(object):
    """Agent_list."""

    def __init__(self, position):
        """Initialize."""
        self.pos = position
        self.velocity = Vec2(1, 0)
        self.acceleration = Vec2(1, 0)
        self.targetpos = Vec2(0, 0)
        self.force = Vec2(1, 0)
        self.mass = 1
        self.direction = Vec2(1, 0)

    def set_target(self, target):
        """Set Target."""
        self.targetpos = Vec2(target[0], target[1])

    def addforce(self, force):
        """Add a force."""
        self.force += force

    def seek(self, target):
        """Seek Behavior."""
        max_velocity = 20
        displacement = target - self.pos
        force = displacement.direction * max_velocity
        seekforce = force - self.velocity
        return seekforce

    def draw(self, screen):
        """Draw the gameobject."""
        posx = int(self.pos[0])
        posy = int(self.pos[1])

        pygame.draw.circle(screen, (125, 125, 255), (posx, posy), 25, 0)

    def update(self, deltatime):
        """Update gameobject logic."""
        # self.seek(deltatime)
        force = self.seek(self.targetpos)
        self.addforce(force * 5)
        self.force = self.force * deltatime
        self.acceleration = self.force * (1 / self.mass)
        self.velocity = self.velocity + self.force * deltatime
        self.direction = self.velocity.direction
        if self.velocity.magnitude > 20:
            self.velocity = self.velocity * (1 / 20)
        self.pos = self.pos + self.velocity
        print self.pos
