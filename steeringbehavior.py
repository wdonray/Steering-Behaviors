"""SteeringBehavior."""

import random

import pygame

from constants import *
from gametemplate import GameTemplate


class SteeringBehavior(GameTemplate):
    """Seeking Behavior."""

    def __init__(self, name):
        """Initialize."""
        super(SteeringBehavior, self).__init__()
        self.name = name
        self.gameobjects = []
        random.seed()

    def addtobatch(self, gameobject):
        """Add gameobjects to this game."""
        self.gameobjects.append(gameobject)
        for i in self.gameobjects:
            i.set_target((random.randint(0, SCREEN.get_width() - 10),
                          random.randint(0, SCREEN.get_height() - 10)))

    def update(self):
        """Update this games logic."""
        if not super(SteeringBehavior, self).update():
            return False
        if self.get_state() == "running":
            for i in self.gameobjects:
                i.set_target(
                    (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                i.update(self.deltatime)
        return True

    def draw(self):
        """Draw all gameobjects added to this game."""
        for i in self.gameobjects:
            i.draw(self.surface)
        super(SteeringBehavior, self).draw()

    def run(self):
        """Runnning."""
        if super(SteeringBehavior, self).startup():
            while self.update():
                self.draw()
        super(SteeringBehavior, self).shutdown()


if __name__ == '__main__':
    import maincorrect as Main
    Main.main()
