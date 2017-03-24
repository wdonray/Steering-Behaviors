"""Main Game File."""

# from gameobject import GameObject
import pygame
from constants import *


class GameTemplate(object):
    """Pygame object."""

    def __init__(self):
        """Init."""
        self.name = ""
        pygame.display.init()
        pygame.font.init()
        self.screen = SCREEN
        pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.fps = 1
        self.playtime = 0.0
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        self.gamestates = {}
        self.gamestates["init"] = ["running"]
        self.gamestates["running"] = ["quit"]
        self.gamestates["quit"] = []
        self.currentstate = "init"
        self.events = pygame.event.get()
        self.deltatime = 0.0

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

    gamestate = property(get_state, set_state)

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
        self.deltatime = millisec / 1000
        self.playtime += self.deltatime
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_m]:
                    self.gamestate = "menu"
                if key_pressed[pygame.K_r]:
                    self.gamestate = "running"
                if key_pressed[pygame.K_ESCAPE]:
                    self.set_state("quit")
                if event.type == pygame.QUIT:
                    self.set_state("quit")
        return True

    def draw(self):
        """Base draw."""
        pygame.display.flip()

    def shutdown(self):
        """Shutdown the game properly."""
        pygame.quit()
