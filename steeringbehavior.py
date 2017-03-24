"""SteeringBehavior."""

import pygame

import constants
from agent import Agent
from gametemplate import GameTemplate
from vector import Vector2 as Vec


class SteeringBehavior(GameTemplate):
    """Seeking Behavior."""

    def __init__(self, name):
        """Initialize."""
        super(SteeringBehavior, self).__init__()
        self.name = name
        self.gameobjects = []
        self.targeted = Agent((pygame.display.get_surface().get_width(),
                               pygame.display.get_surface().get_height()))

    def addtobatch(self, gameobject):
        """Add gameobjects to this game."""
        self.gameobjects.append(gameobject)
        #gameobject.set_target(self.targeted)

    def update(self):
        """Update this games logic."""
        if not super(SteeringBehavior, self).update():
            return False
        for i in self.gameobjects:
            i.update(self.deltatime)
        # self.targeted = pygame.mouse.get_pos()
        # for i in self.gameobjects:
        #     if type(i) == Agent:
        #         i.seek(self.deltatime)
        #         print i.velocity
        return True

    def draw(self):
        """Draw all gameobjects added to this game."""
        for i in self.gameobjects:
            i.draw(self.screen)
        super(SteeringBehavior, self).draw()

    def run(self):
        """Runnning."""
        if super(SteeringBehavior, self).startup():
            while self.update():
                self.draw()
        super(SteeringBehavior, self).shutdown()
