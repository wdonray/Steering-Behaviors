"""Steering Behaviors."""

import random

import pygame

from vector import Vector2 as Vec2

random.seed()


class Agent(object):
    """Agent_list."""

    def __init__(self, position):
        """Initialize."""
        self.pos = position
        self.velocity = Vec2(1, 0)
        self.max_velocity = 20
        self.acceleration = Vec2(1, 0)
        self.target = None
        self.force = Vec2(1, 0)
        self.mass = 1
        # self.bounds = posbounds

    def set_target(self, target):
        """Set Target."""
        self.target = target

    # def seek(self, scaler):
    #     """Seek Behavior."""
    #     dist = self.Vec_.get_dist(self.pos, self.target.pos)
    #     direction = self.Vec_.get_normilized(dist)
    #     self._addforce((direction[0] * self.Vec_.get_mag(dist) * 150,
    #                     direction[1] * self.Vec_.get_mag(dist) * 150))
    #     #self._updatepos()
    #     self._updatevelocity(scaler)
    #     self._updateacceleration(scaler)

    # def flee(self, scaler):
    #     """Flee Behavior."""
    #     dist = self.Vec_.get_dist(self.pos, self.target.pos)
    #     direction = self.Vec_.get_normilized(dist)
    #     vec = self._addforce((direction[0] * self.Vec_.get_mag(dist) * -250,
    #                           direction[1] * self.Vec_.get_mag(dist) * -250))
    #     #self._updatepos()
    #     self._updatevelocity(scaler)
    #     self._updateacceleration(scaler)
    #     return vec

    def wander(self, scaler):
        """Wander Behavior."""
        # jitter = random.choice()
        # radius =
        # distance =
        # self._updatepos()
       # self._updatevelocity(scaler)
       # self._updateacceleration(scaler)

    def pursue(self):
        """Pursue Behavior."""
        pass

    def evade(self):
        """Evade Behavior."""
        pass

    def arrival(self):
        """Arrival Behavior."""
        pass

    def addforce(self, force):
        """Add a force."""
        self.force += force

    # def _updateacceleration(self, time):
    #     self.acceleration = (self.force[0] * time,
    #                          self.force[1] * time)

    # def _updatevelocity(self, time):
    #     """update_velocity."""
    #     self.velocity = ((self.velocity[0] + self.acceleration[0]) * time,
    #                      (self.velocity[1] + self.acceleration[1]) * time)

    #     if self.Vec_.get_mag(self.velocity) > self.max_velocity:
    #         self.velocity = (self.Vec_.get_normilized(self.velocity)[0] *
    #                          self.max_velocity,
    #                          self.Vec_.get_normilized(self.velocity)[1] *
    #                          self.max_velocity)

    # def _boundaryforce(self):
    #     """update_pos."""
    #     self.pos = (self.pos[0] + self.velocity[0],
    #                 self.pos[1] + self.velocity[1])
    #     if self.pos[0] < 10:
    #         self.pos = (10, self.pos[1])
    #     if self.pos[1] < 10:
    #         self.pos = (self.pos[0], 10)
    #     if self.pos[0] > self.bounds[0] - 10:
    #         self.pos = (self.bounds[0] - 10, self.pos[1])
    #     if self.pos[1] > self.bounds[1] - 10:
    #         self.pos = (self.pos[0], self.bounds[1] - 10)

    # def _addforce(self, force):
    #     """add_force."""
    #     self.force = (force[0],
    #                          force[1])

    def draw(self, screen):
        """Draw the gameobject."""
        posx = int(self.pos[0])
        posy = int(self.pos[1])

        pygame.draw.circle(screen, (125, 125, 255), (posx, posy), 25)

    def update(self, deltatime):
        """Update gameobject logic."""
        # self.seek(deltatime)
        self.acceleration = self.force 
        self.velocity = (self.velocity + self.acceleration) * deltatime
        self.pos = (self.pos + self.velocity) * deltatime
       # print self.pos
