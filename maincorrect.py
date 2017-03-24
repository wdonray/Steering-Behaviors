"""MAIN."""

import pygame

from agent import Agent
from steeringbehavior import SteeringBehavior


def main():
    """Main execution."""
    game = SteeringBehavior("Seek")
    game.addtobatch(Agent(pygame.display.get_surface()))
    # make gameobjects to participate in game
    game.run()

if __name__ == "__main__":
    main()
