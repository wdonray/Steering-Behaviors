"""Main Game File."""

import math
import random

# from gameobject import GameObject
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
        self.fps = 30
        self.playtime = 0.0
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        self.gamestates = {}
        self.gamestates["init"] = ["seek", "flee", "wander", "dance", "quit"]
        self.gamestates["seek"] = ["flee", "wander", "dance", "quit"]
        self.gamestates["flee"] = ["seek", "wander", "dance", "quit"]
        self.gamestates["wander"] = ["flee", "seek", "dance", "quit"]
        self.gamestates["dance"] = ["flee", "seek", "quit"]
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
        self.set_state("wander")
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
                if key_pressed[pygame.K_F1]:
                    self.set_state("seek")
                if key_pressed[pygame.K_F2]:
                    self.set_state("flee")
                if key_pressed[pygame.K_F3]:
                    self.set_state("wander")
                if key_pressed[pygame.K_F10]:
                    self.set_state("dance")
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
        self.draw_text("FPS:{}{}TIME:{:6.5}{}STATE: {:4.6}".format(
            int(math.floor(self.clock.get_fps())),
            " --- ", self.playtime, " --- ",
            self.get_state()))

        pygame.display.flip()
        self.surface.blit(self.background, (0, 0))

        if self.get_state() == "dance":
            self.background.fill((random.randrange(0, 255), random.randrange(0, 255),
                                  random.randrange(0, 255)))
            self.surface.blit(self.background, (random.randint(0, SCREEN.get_width()),
                                                random.randint(0, SCREEN.get_height())))

    def shutdown(self):
        """Shutdown the game properly."""
        pygame.quit()
