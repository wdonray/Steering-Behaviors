"""Main File"""
import pygame
import random
from boids import Boids

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
DONE = False
CLOCK = pygame.time.Clock()

pygame.mouse.set_cursor(*pygame.cursors.diamond)
pygame.display.set_mode((1280, 720))
SCREEN = pygame.display.get_surface()
BOIDS = []
TARGETED = Boids()
TARGETED.pos = pygame.mouse.get_pos()

for x in range(50):
    BOIDS.append(Boids())
    BOIDS[x].target = TARGETED
    BOIDS[x].pos = (random.randrange(0, SCREEN.get_width() + 1),
                    random.randrange(0, SCREEN.get_height() + 1))

while not DONE:
    CLOCK.tick(60)
    DELTATIME = CLOCK.get_time()
    pygame.display.set_mode((1280, 720))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                DONE = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                TARGETED.pos = pygame.mouse.get_pos()
    for boid in BOIDS:
        boid.seek(DELTATIME)
        pygame.draw.circle(
            SCREEN, YELLOW, ((int(round(boid.pos[0])), int(round(boid.pos[1])))), 5, 0)
    pygame.draw.circle(
        SCREEN, RED, ((int(round(TARGETED.pos[0])), int(round(TARGETED.pos[1])))), 15, 0)
    pygame.display.flip()
pygame.quit()
