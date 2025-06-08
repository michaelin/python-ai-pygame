"""
Main entry point for the pygame game.
"""

import sys

import pygame

from game.engine import GameEngine


def main():
    """Main function to run the game."""
    # Initialize pygame
    pygame.init()

    try:
        # Create and run the game engine
        engine = GameEngine()
        engine.run()
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        pygame.quit()
        sys.exit(0)


if __name__ == "__main__":
    main()
