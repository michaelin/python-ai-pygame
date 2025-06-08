"""
Game entities module - contains base classes and implementations for game objects.
"""

from abc import ABC, abstractmethod

import pygame

from utils.constants import COLORS


class Entity(ABC):
    """Base class for all game entities."""

    def __init__(self, x: float, y: float, width: float, height: float):
        """Initialize the entity."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.active = True

    @property
    def position(self) -> tuple[float, float]:
        """Get the entity's position."""
        return (self.x, self.y)

    @property
    def rect(self) -> pygame.Rect:
        """Get the entity's bounding rectangle."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update the entity."""
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        """Render the entity."""
        pass

    def move(self, dt: float) -> None:
        """Move the entity based on its velocity."""
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt


class Player(Entity):
    """Player entity."""

    def __init__(self, x: float, y: float):
        """Initialize the player."""
        super().__init__(x, y, 32, 32)
        self.speed = 200.0  # pixels per second
        self.color = COLORS["BLUE"]

    def update(self, dt: float) -> None:
        """Update the player."""
        # Handle input
        keys = pygame.key.get_pressed()
        self.velocity_x = 0.0
        self.velocity_y = 0.0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity_y = self.speed

        # Move the player
        self.move(dt)

        # Keep player on screen
        self.x = max(0, min(self.x, 800 - self.width))  # TODO: Use screen constants
        self.y = max(0, min(self.y, 600 - self.height))

    def render(self, screen: pygame.Surface) -> None:
        """Render the player."""
        pygame.draw.rect(screen, self.color, self.rect)


class Enemy(Entity):
    """Basic enemy entity."""

    def __init__(self, x: float, y: float):
        """Initialize the enemy."""
        super().__init__(x, y, 24, 24)
        self.speed = 100.0
        self.color = COLORS["RED"]

    def update(self, dt: float) -> None:
        """Update the enemy."""
        # Simple AI: move towards center of screen
        center_x, center_y = 400, 300  # TODO: Use screen constants

        dx = center_x - self.x
        dy = center_y - self.y
        distance = (dx**2 + dy**2) ** 0.5

        if distance > 0:
            self.velocity_x = (dx / distance) * self.speed
            self.velocity_y = (dy / distance) * self.speed

        self.move(dt)

    def render(self, screen: pygame.Surface) -> None:
        """Render the enemy."""
        pygame.draw.rect(screen, self.color, self.rect)
