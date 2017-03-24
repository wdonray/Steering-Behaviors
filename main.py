"""Main File"""
import random

import pygame

from boids import Boids
from drawablenode import DrawableNode
from graph import Graph, Node

pygame.init()
random.seed()

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
the_screen = pygame.display.set_mode((1280, 720))
SEARCH_SPACE = Graph([ROWS, COLS])

pygame.mouse.set_cursor(*pygame.cursors.diamond)

BOXES = []

COUNT = 0
mouse_listeners = []
for i in range(ROWS):  # Creates Rows and Cols and adds a node and a id to each
    for j in range(COLS):
        node = SEARCH_SPACE.get_node([i, j])
        n = DrawableNode(node, COUNT)
        BOXES.append(n)
        mouse_listeners.append(n.printpos)
        COUNT += 1

pygame.font.init()

FONT = pygame.font.Font(None, 45)


def main_menu():
    """main_menu"""
    CLOCK.tick(60)
    pygame.display.set_mode((WIDTH, HEIGHT))
    main_done = False

    selected = BOXES[0]

    while not main_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_UP] and selected.identification > 0:
                    selected = BOXES[selected.identification - 1]
                if (pygame.key.get_pressed()[pygame.K_DOWN] and
                        selected.identification < ROWS * COLS - 1):
                    selected = BOXES[selected.identification + 1]
                if (pygame.key.get_pressed()[pygame.K_RETURN] and
                        BOXES[selected.identification] is BOXES[0]):
                    test_seek()
                elif (pygame.key.get_pressed()[pygame.K_RETURN] and
                      BOXES[selected.identification] is BOXES[1]):
                    test_flee()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    main_done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                for callback in mouse_listeners:
                    cb = callback(pygame.mouse.get_pos())
                    selected = cb
                    if cb:
                        if (event.button == 1 and
                                BOXES[selected.identification] is BOXES[0]):
                            selected = cb
                            test_seek()
                        elif (event.button == 1 and
                              BOXES[selected.identification] is BOXES[1]):
                            selected = cb
                            test_flee()

        the_screen.fill(BLACK)

        pygame.draw.rect(the_screen, PINK, [selected.xpos, selected.ypos,
                                            selected.width + 5, selected.height + 5])

        for things in BOXES:
            things.draw(the_screen, FONT)

        pygame.display.flip()
    pygame.quit()


def test_seek():
    """Testing Seek"""
    seek_done = False
    pygame.display.set_mode((1080, 720))
    boids_list = []
    targeted = Boids((the_screen.get_width(), the_screen.get_height()))

    for itera in range(10):
        boids_list.append(
            Boids((the_screen.get_width(), the_screen.get_height())))
        boids_list[itera].target = targeted
        boids_list[itera].pos = (random.randrange(0, the_screen.get_width() + 1),
                                 random.randrange(0, the_screen.get_height() + 1))

    while not seek_done:
        CLOCK.tick(60)
        delta_time = float(CLOCK.get_time()) / float(2500)
        pygame.display.set_mode((1280, 720))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                seek_done = True
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    seek_done = True
                if pygame.key.get_pressed()[pygame.K_p]:
                    pygame.display.set_mode((WIDTH, HEIGHT))
                    main_menu()
        for boid in boids_list:
            boid.seek(delta_time)
            pygame.draw.rect(
                the_screen, (0, random.randrange(0, 255), random.randrange(0, 255)), [
                    int(round(boid.pos[0])), int(round(boid.pos[1])), 20, 20])
            pygame.draw.line(the_screen, WHITE, ((int(round(boid.pos[0]))),
                                                 (int(round(boid.pos[1])))),
                             ((int(round(targeted.pos[0]))), (int(round(targeted.pos[1])))), 2)
        pygame.draw.circle(
            the_screen, RED, (int(round(targeted.pos[0])), int(
                round(targeted.pos[1]))),
            5, 0)
        targeted.pos = pygame.mouse.get_pos()
        pygame.display.flip()
    pygame.quit()


def test_flee():
    """Testing Flee"""
    flee_done = False
    pygame.display.set_mode((1280, 720))
    boids_list = []
    targeted = Boids((the_screen.get_width(), the_screen.get_height()))

    for itera in range(10):
        boids_list.append(
            Boids((the_screen.get_width(), the_screen.get_height())))
        boids_list[itera].target = targeted
        boids_list[itera].pos = (random.randrange(0, the_screen.get_width() + 1),
                                 random.randrange(0, the_screen.get_height() + 1))

    while not flee_done:
        CLOCK.tick(60)
        delta_time = float(CLOCK.get_time()) / float(2500)
        pygame.display.set_mode((1280, 720))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flee_done = True
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    flee_done = True
                if pygame.key.get_pressed()[pygame.K_p]:
                    pygame.display.set_mode((WIDTH, HEIGHT))
                    main_menu()
        for boid in boids_list:
            boid.flee(delta_time)
            pygame.draw.rect(
                the_screen, YELLOW, [int(round(boid.pos[0])), int(round(boid.pos[1])), 20, 20])
            pygame.draw.line(the_screen, WHITE, ((int(round(boid.pos[0]))),
                                                 (int(round(boid.pos[1])))),
                             ((int(round(targeted.pos[0]))), (int(round(targeted.pos[1])))), 2)
        pygame.draw.circle(
            the_screen, RED, (int(round(targeted.pos[0])), int(
                round(targeted.pos[1]))),
            5, 0)
        targeted.pos = pygame.mouse.get_pos()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main_menu()
