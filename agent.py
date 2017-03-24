"""Steering Behaviors."""

import random
from vector import Vector2 as Vec

random.seed()


class Agent(object):
    """Agent_list."""

    def __init__(self, posbounds):
        """Initialize."""
        self.pos = (0, 0)
        self.velocity = (0, 0)
        self.max_velocity = 20
        self.acceleration = (0, 0)
        self.target = None
        self.forceapplied = (0, 0)
        self.bounds = posbounds
        self.Vec_ = Vec(0, 0)

    def seek(self, scaler):
        """Seek Behavior."""
        dist = self.Vec_.get_dist(self.pos, self.target.pos)
        direction = self.Vec_.get_normilized(dist)
        vec = self._addforce((direction[0] * self.Vec_.get_mag(dist) * 150,
                              direction[1] * self.Vec_.get_mag(dist) * 150))
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)
        return vec

    def flee(self, scaler):
        """Flee Behavior."""
        dist = self.Vec_.get_dist(self.pos, self.target.pos)
        direction = self.Vec_.get_normilized(dist)
        vec = self._addforce((direction[0] * self.Vec_.get_mag(dist) * -250,
                              direction[1] * self.Vec_.get_mag(dist) * -250))
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)
        return vec

    def wander(self, scaler):
        """Wander Behavior."""
        #jitter = random.choice()
        # radius =
        # distance =
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)

    def pursue(self):
        """Pursue Behavior."""
        pass

    def evade(self):
        """Evade Behavior."""
        pass

    def arrival(self):
        """Arrival Behavior."""
        pass

    def _updateacceleration(self, time):
        self.acceleration = (self.forceapplied[0] * time,
                             self.forceapplied[1] * time)

    def _updatevelocity(self, time):
        """update_velocity."""
        self.velocity = ((self.velocity[0] + self.acceleration[0]) * time,
                         (self.velocity[1] + self.acceleration[1]) * time)

        if self.Vec_.get_mag(self.velocity) > self.max_velocity:
            self.velocity = (self.Vec_.get_normilized(self.velocity)[0] *
                             self.max_velocity,
                             self.Vec_.get_normilized(self.velocity)[1] *
                             self.max_velocity)

    def _updatepos(self):
        """update_pos."""
        self.pos = (self.pos[0] + self.velocity[0],
                    self.pos[1] + self.velocity[1])
        if self.pos[0] < 10:
            self.pos = (10, self.pos[1])
        if self.pos[1] < 10:
            self.pos = (self.pos[0], 10)
        if self.pos[0] > self.bounds[0] - 10:
            self.pos = (self.bounds[0] - 10, self.pos[1])
        if self.pos[1] > self.bounds[1] - 10:
            self.pos = (self.pos[0], self.bounds[1] - 10)

    def _addforce(self, forceapplied):
        """add_force."""
        self.forceapplied = (forceapplied[0],
                             forceapplied[1])
