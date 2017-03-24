"""MAIN."""

import pygame

from agent import Agent
from steeringbehavior import SteeringBehavior
from vector import Vector2


def main():
    """Main execution."""
    game = SteeringBehavior("Seek")
    agent = Agent(Vector2(250, 250))
    agent.addforce(Vector2(1, 0))
    game.addtobatch(agent)
    # for iterator in range(1):
    #     game.addtobatch(Agent((pygame.display.get_surface().get_width(
    #     ), pygame.display.get_surface().get_height())))
    # make gameobjects to participate in game
    game.run()


if __name__ == "__main__":
    main()
