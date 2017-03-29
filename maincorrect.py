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

    for i in range(1):
        game.addtobatch(Agent(Vector2(0.0 + (random.randint(0, SCREEN.get_width())),
                                      0.0 + (random.randint(0, SCREEN.get_height())))))
    # game.addtobatch(Agent(Vector2(200.0, 200.0)))
    # make gameobjects to participate in game
    game.run()


if __name__ == "__main__":
    main()
