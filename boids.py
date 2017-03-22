"""Steering Behaviors"""

import vector as Vec


class Boids(object):
    """Boids"""

    def __init__(self):
        self.pos = (0, 0)
        self.velocity = (0, 0)
        self.max_velocity = 500
        self.acceleration = (0, 0)
        self.target = None

    def seek(self, scaler):
        """Seek Behavior"""
        dist = Vec.get_dist(self.pos, self.target.pos)
        direction = Vec.get_normilized(dist)
        self._addorce((direction[0] * Vec.get_mag(dist) * scaler,
                       direction[1] * Vec.get_mag(dist) * scaler))
        self._updatepos()
        self._updatevelocity()

    def flee(self):
        """Flee Behavior"""
        pass

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

    def _updatevelocity(self):
        """update_velocity"""
        self.velocity = (self.velocity[0] + self.acceleration[0],
                         self.velocity[1] + self.acceleration[1])

        if Vec.get_mag(self.velocity) > self.max_velocity:
            self.velocity = Vec.get_normilized(
                self.velocity) * self.max_velocity

    def _updatepos(self):
        """update_pos"""
        self.pos = (self.pos[0] + self.velocity[0],
                    self.pos[1] + self.velocity[1])

    def _addorce(self, appliedforce):
        self.acceleration = (self.acceleration[0] + appliedforce[0],
                              self.acceleration[1] + appliedforce[1])
