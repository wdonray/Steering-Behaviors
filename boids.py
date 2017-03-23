"""Steering Behaviors"""

import random
import vector as Vec

random.seed()


class Boids(object):
    """boids_list"""

    def __init__(self):
        self.pos = (0, 0)
        self.velocity = (0, 0)
        self.max_velocity = 20
        self.acceleration = (0, 0)
        self.target = None
        self.forceapplied = (0, 0)

    def seek(self, scaler):
        """Seek Behavior"""
        dist = Vec.get_dist(self.pos, self.target.pos)
        direction = Vec.get_normilized(dist)
        self._addforce((direction[0] * Vec.get_mag(dist) * 150,
                        direction[1] * Vec.get_mag(dist) * 150))
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)

    def flee(self, scaler):
        """Flee Behavior"""
        dist = Vec.get_dist(self.pos, self.target.pos)
        direction = Vec.get_normilized(dist)
        self._addforce((direction[0] * Vec.get_mag(dist) * -150,
                        direction[1] * Vec.get_mag(dist) * -150))
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)

    def wander(self, scaler):
        """Wander Behavior"""
        #jitter = random.choice()
        # radius =
        # distance =
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)

    def pursue(self):
        """Pursue Behavior"""
        pass

    def evade(self):
        """Evade Behavior"""
        pass

    def arrival(self):
        """Arrival Behavior"""
        pass

    def _updateacceleration(self, time):
        self.acceleration = (self.forceapplied[0] * time,
                             self.forceapplied[1] * time)

    def _updatevelocity(self, time):
        """update_velocity"""
        self.velocity = ((self.velocity[0] + self.acceleration[0]) * time,
                         (self.velocity[1] + self.acceleration[1]) * time)

        if Vec.get_mag(self.velocity) > self.max_velocity:
            self.velocity = (Vec.get_normilized(self.velocity)[0] *
                             self.max_velocity,
                             Vec.get_normilized(self.velocity)[1] *
                             self.max_velocity)

    def _updatepos(self):
        """update_pos"""
        self.pos = (self.pos[0] + self.velocity[0],
                    self.pos[1] + self.velocity[1])
        if self.pos[0] < 5:
            self.pos[0] = (5, self.pos[1])
        if self.pos[1] < 5:
            self.pos[1] = (self.pos[0], 5)

    def _addforce(self, forceapplied):
        """add_force"""
        self.forceapplied = (forceapplied[0],
                             forceapplied[1])
