"""All constants for game."""
import pygame

from graph import Graph

PINK = (255, 153, 255)
MAROON = (128, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ROWS = 1
COLS = 3
PAD = (5, 5)
WIDTH = 210
HEIGHT = 620
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 600))
SEARCH_SPACE = Graph([ROWS, COLS])
