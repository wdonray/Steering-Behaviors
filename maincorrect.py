"""MAIN."""

import pygame

from agent import Agent
from steeringbehavior import SteeringBehavior
from vector import Vector2


def main():
    """Main execution."""
    game = SteeringBehavior("Seek")
    for i in range(1):
        game.addtobatch(Agent(Vector2(200 + (i * i), 200 + (i * i))))
    # make gameobjects to participate in game
    game.run()

if __name__ == "__main__":
    main()
