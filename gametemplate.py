"""Main Game File."""

import math
import random

import pygame

from constants import *

random.seed()
# pylint: disable=E1121
# pylint: disable=E1101


class GameTemplate(object):
    """Pygame object."""

    def __init__(self):
        """Init."""
        self.name = ""
        pygame.display.init()
        pygame.font.init()
        self.surface = SCREEN
        self.background = pygame.Surface(self.surface.get_size()).convert()
        self.background.fill((255, 255, 255))
        self.clock = CLOCK
        self.fps = 60
        self.playtime = 0.0
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        self.gamestates = {}
        self.gamestates["init"] = ["running"]
        self.gamestates["running"] = ["quit"]
        self.gamestates["quit"] = []
        self.currentstate = "init"
        self.events = pygame.event.get()
        self.deltatime = 0.0
        self.font = pygame.font.SysFont('mono', 20)

    def set_state(self, value):
        """Set state."""
        if value in self.gamestates[self.currentstate]:
            print "Valid Transition", self.currentstate, " -> ", value
            self.currentstate = value
        else:
            print "Invalid Transition ", self.currentstate, " -> ", value

    def get_state(self):
        """Get currentstate."""
        return self.currentstate

    def startup(self):
        """Do startup routines."""
        pygame.display.set_caption(self.name)
        self.set_state("running")
        return True

    def update(self):
        """Input and time."""
        if self.get_state() == "quit":
            return False
        millisec = self.clock.tick(self.fps)
        self.deltatime = millisec / 1000.0
        self.playtime += self.deltatime
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_ESCAPE]:
                    self.set_state("quit")
            if event.type == pygame.QUIT:
                self.set_state("quit")
        return True

    def draw_text(self, text):
        """Center text in window."""
        surface = self.font.render(text, True, (0, 0, 0))
        SCREEN.blit(surface, (surface.get_width() / 2 + 60, 10))

    def draw(self):
        """Base draw."""
        self.draw_text("FPS:{}{}TIME:{:6.5}{}STATE: {:4.7}".format(
            int(math.floor(self.clock.get_fps())),
            " --- ", self.playtime, " --- ",
            self.get_state()))

        pygame.display.flip()
        self.surface.blit(self.background, (0, 0))

    def shutdown(self):
        """Shutdown the game properly."""
        pygame.quit()


if __name__ == '__main__':
    import maincorrect as Main
    Main.main()
