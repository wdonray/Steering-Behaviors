"""MAIN."""

import random

from agent import Agent
from constants import *
from steeringbehavior import SteeringBehavior
from vector import Vector2

random.seed()


def main():
    """Main execution."""

    game = SteeringBehavior("Steering Behaviors")
    # make gameobjects to participate in game
    for _ in range(1):
        game.addtobatch(Agent(Vector2(0.0 + (random.randint(0, SCREEN.get_width())),
                                      0.0 + (random.randint(0, SCREEN.get_height())))))
    # game.addtobatch(Agent(Vector2(200.0, 200.0)))
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    game.run()



if __name__ == "__main__":
    main()
