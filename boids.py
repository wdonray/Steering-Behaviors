"""Steering Behaviors"""

import vector as Vec


class Boids(object):
    """Boids"""

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
        self._addforce((direction[0] * Vec.get_mag(dist) * 500,
                        direction[1] * Vec.get_mag(dist) * 500))
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)

    def flee(self, scaler):
        """Flee Behavior"""
        dist = Vec.get_dist(self.pos, self.target.pos)
        direction = Vec.get_normilized(dist)
        self._addforce((direction[0] * Vec.get_mag(dist) * -100,
                        direction[1] * Vec.get_mag(dist) * -100))
        self._updatepos()
        self._updatevelocity(scaler)
        self._updateacceleration(scaler)

    def wander(self):
        """Wander Behavior"""
        pass

    def pursue(self):
        """Pursue Behavior"""
        pass

    def evade(self):
        """Evade Behavior"""
        pass

    def arrival(self):
        """Arrival Behavior"""
        pass

    def _updateacceleration(self, deltatime):
        self.acceleration = (self.forceapplied[0] * deltatime,
                             self.forceapplied[1] * deltatime)

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

    def _addforce(self, forceapplied):
        """add_force"""
        self.forceapplied = (forceapplied[0],
                             forceapplied[1])
