"""Steering Behaviors."""

import math
import random

import pygame

from constants import *
from vector import Vector2 as Vec2

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
        self.wander_angle = 45.0
        self.heading = Vec2(0, 0)
        self.max_velocity = 100
        self.direction = self.velocity.direction
        self.surface = pygame.Surface((45, 25), pygame.SRCALPHA)
        pygame.draw.lines(self.surface, random.choice((BLACK, BLUE, PINK, MAROON, GREEN)),
                          True, [(1, 1), (15, 25), (25, 1)], 2)
        pygame.draw.circle(self.surface, RED, (25, 3), 3)
        self.font = pygame.font.SysFont('mono', 12)
        self.wanderforce = None

    def set_target(self, target):
        """Set Target."""
        self.targetpos = Vec2(target[0], target[1])

    def seek(self, target):
        """Seek Behavior."""
        displacement = target - self.pos
        force = displacement.direction * self.max_velocity
        seekforce = force - self.velocity
        return seekforce

    def flee(self, target):
        """Flee Behavior."""
        displacement = target - self.pos
        force = displacement.direction * self.max_velocity * -1
        fleeforce = force - self.velocity
        return fleeforce

    def wander(self, distance, radius):
        """Wander Behavior."""
        center_circle = self.velocity.get_direction()
        center_circle = center_circle * distance

        displacement = self.velocity.get_direction()
        displacement = Vec2(0, 1) * radius
        self.wander_angle += (random.random() * 1.0) - (1.0 * .5)
        displacement.xpos = math.cos(
            self.wander_angle) * displacement.get_mag()
        displacement.ypos = math.sin(
            self.wander_angle) * displacement.get_mag()
        self.wanderforce = center_circle + displacement
        return self.wanderforce

    def draw(self, screen):
        """Draw the gameobject."""
        middle = Vec2(self.pos.xpos + self.surface.get_width() / 2,
                      self.pos.ypos + self.surface.get_height() / 2)

        lineseek = Vec2(middle.xpos + self.velocity.direction.xpos * self.velocity.get_mag(),
                        middle.ypos + self.velocity.direction.ypos * self.velocity.get_mag())
        lineflee = Vec2(middle.xpos + self.velocity.direction.xpos * self.velocity.get_mag() * -1,
                        middle.ypos + self.velocity.direction.ypos * self.velocity.get_mag() * -1)
        linewander = Vec2(middle.xpos + self.wanderforce.xpos / 6,
                          middle.ypos + self.wanderforce.ypos / 6)

        pygame.draw.line(screen, RED, middle.value, lineflee.value, 2)
        pygame.draw.line(screen, BLUE, middle.value, lineseek.value, 2)
        pygame.draw.line(screen, PINK, middle.value, linewander.value, 2)

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

        howpos = "Steering Behavior created by Donray"
        surfaceh = self.font.render(howpos, True, (0, 0, 0))
        screen.blit(surfaceh, (screen.get_width() / 2 + 10, 30))

        rotate = pygame.transform.rotate(
            self.surface, -180 * math.atan2(self.heading[1], self.heading[0]) /
            math.pi)
        self.heading = Vec2.get_direction(self.velocity)

        screen.blit(rotate, (self.pos.xpos, self.pos.ypos))

    def update(self, deltatime):
        """Update agent logic."""
        self.force = self.seek(
            self.targetpos) * 25 + self.flee(self.targetpos) + self.wander(400, 400)
        if (self.pos.xpos >= SCREEN.get_width() or
                (self.pos.ypos >= SCREEN.get_height())):
            self.pos.xpos = SCREEN.get_width() / 2
            self.pos.ypos = SCREEN.get_height() / 2

        elif self.pos.xpos <= 0 or self.pos.ypos <= 0:
            self.pos.xpos = SCREEN.get_width() / 2
            self.pos.ypos = SCREEN.get_height() / 2

        self.acceleration = self.force
        self.velocity += self.acceleration * deltatime

        if self.velocity.get_mag() > self.max_velocity:
            self.velocity = self.velocity.direction * self.max_velocity

        self.direction = self.velocity.direction
        self.pos += self.velocity * deltatime


if __name__ == '__main__':
    import maincorrect as Main
    Main.main()
