"""
Game engine module - handles the main game loop and core functionality.
"""

from typing import Optional

import pygame

from utils.constants import COLORS, FPS, SCREEN_HEIGHT, SCREEN_WIDTH


class GameEngine:
    """Main game engine that handles the game loop and core systems."""

    def __init__(self):
        """Initialize the game engine."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Python AI Pygame Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0.0

    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self, dt: float) -> None:
        """Update game state."""
        # TODO: Update game entities and AI systems
        pass

    def render(self) -> None:
        """Render the game."""
        # Clear screen with background color
        self.screen.fill(COLORS["BLACK"])

        # Draw a simple placeholder
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        pygame.draw.circle(self.screen, COLORS["WHITE"], (center_x, center_y), 50)

        # Update display
        pygame.display.flip()

    def run(self) -> None:
        """Main game loop."""
        print("Starting game engine...")

        while self.running:
            # Calculate delta time
            self.dt = self.clock.tick(FPS) / 1000.0

            # Handle events
            self.handle_events()

            # Update game state
            self.update(self.dt)

            # Render
            self.render()

        print("Game engine stopped.")
