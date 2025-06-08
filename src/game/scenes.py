"""
Game scenes module - contains different game states and scenes.
"""

from abc import ABC, abstractmethod

import pygame

from game.entities import Enemy, Player


class Scene(ABC):
    """Base class for all game scenes."""

    def __init__(self):
        """Initialize the scene."""
        self.active = True

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle a pygame event."""
        pass

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update the scene."""
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        """Render the scene."""
        pass


class GameScene(Scene):
    """Main gameplay scene."""

    def __init__(self):
        """Initialize the game scene."""
        super().__init__()
        self.player = Player(100, 100)
        self.enemies = [
            Enemy(500, 200),
            Enemy(300, 400),
        ]

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle pygame events for the game scene."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space pressed in game scene!")

    def update(self, dt: float) -> None:
        """Update the game scene."""
        # Update player
        self.player.update(dt)

        # Update enemies
        for enemy in self.enemies:
            enemy.update(dt)

    def render(self, screen: pygame.Surface) -> None:
        """Render the game scene."""
        # Render player
        self.player.render(screen)

        # Render enemies
        for enemy in self.enemies:
            enemy.render(screen)


class MenuScene(Scene):
    """Main menu scene."""

    def __init__(self):
        """Initialize the menu scene."""
        super().__init__()
        self.font = pygame.font.Font(None, 74)
        self.title_text = self.font.render("Python AI Game", True, (255, 255, 255))

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle pygame events for the menu scene."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Enter pressed - start game!")

    def update(self, dt: float) -> None:
        """Update the menu scene."""
        pass

    def render(self, screen: pygame.Surface) -> None:
        """Render the menu scene."""
        # Center the title
        screen_rect = screen.get_rect()
        title_rect = self.title_text.get_rect(center=screen_rect.center)
        screen.blit(self.title_text, title_rect)
