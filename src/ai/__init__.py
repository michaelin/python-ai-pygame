"""
AI agents module - contains AI implementations for game entities.
"""

import random
from abc import ABC, abstractmethod

import pygame

from game.entities import Entity


class AIAgent(ABC):
    """Base class for AI agents."""

    def __init__(self, entity: Entity):
        """Initialize the AI agent."""
        self.entity = entity
        self.active = True

    @abstractmethod
    def update(self, dt: float, game_state: dict) -> None:
        """Update the AI agent."""
        pass


class SimpleAI(AIAgent):
    """Simple AI that moves randomly."""

    def __init__(self, entity: Entity):
        """Initialize the simple AI."""
        super().__init__(entity)
        self.direction_change_timer = 0.0
        self.direction_change_interval = 2.0  # Change direction every 2 seconds
        self.speed = 50.0

    def update(self, dt: float, game_state: dict) -> None:
        """Update the simple AI."""
        self.direction_change_timer += dt

        if self.direction_change_timer >= self.direction_change_interval:
            # Choose a new random direction
            angle = random.uniform(0, 2 * 3.14159)  # Random angle in radians
            self.entity.velocity_x = (
                self.speed * pygame.math.Vector2(1, 0).rotate_rad(angle).x
            )
            self.entity.velocity_y = (
                self.speed * pygame.math.Vector2(1, 0).rotate_rad(angle).y
            )
            self.direction_change_timer = 0.0


class ChasingAI(AIAgent):
    """AI that chases a target entity."""

    def __init__(self, entity: Entity, speed: float = 100.0):
        """Initialize the chasing AI."""
        super().__init__(entity)
        self.speed = speed
        self.target: Entity | None = None

    def set_target(self, target: Entity) -> None:
        """Set the target entity to chase."""
        self.target = target

    def update(self, dt: float, game_state: dict) -> None:
        """Update the chasing AI."""
        if not self.target:
            return

        # Calculate direction to target
        dx = self.target.x - self.entity.x
        dy = self.target.y - self.entity.y
        distance = (dx**2 + dy**2) ** 0.5

        if distance > 0:
            # Normalize and apply speed
            self.entity.velocity_x = (dx / distance) * self.speed
            self.entity.velocity_y = (dy / distance) * self.speed
        else:
            self.entity.velocity_x = 0
            self.entity.velocity_y = 0


class FlockingAI(AIAgent):
    """AI that implements basic flocking behavior (separation, alignment, cohesion)."""

    def __init__(self, entity: Entity, speed: float = 80.0):
        """Initialize the flocking AI."""
        super().__init__(entity)
        self.speed = speed
        self.neighbors: list[Entity] = []
        self.neighbor_radius = 100.0
        self.separation_weight = 1.5
        self.alignment_weight = 1.0
        self.cohesion_weight = 1.0

    def find_neighbors(self, entities: list[Entity]) -> None:
        """Find neighboring entities within the flocking radius."""
        self.neighbors = []
        for other in entities:
            if other != self.entity:
                dx = other.x - self.entity.x
                dy = other.y - self.entity.y
                distance = (dx**2 + dy**2) ** 0.5
                if distance < self.neighbor_radius:
                    self.neighbors.append(other)

    def separation(self) -> tuple[float, float]:
        """Calculate separation force to avoid crowding neighbors."""
        if not self.neighbors:
            return (0.0, 0.0)

        force_x, force_y = 0.0, 0.0
        for neighbor in self.neighbors:
            dx = self.entity.x - neighbor.x
            dy = self.entity.y - neighbor.y
            distance = (dx**2 + dy**2) ** 0.5
            if distance > 0:
                force_x += dx / distance
                force_y += dy / distance

        return (force_x, force_y)

    def alignment(self) -> tuple[float, float]:
        """Calculate alignment force to match neighbors' velocity."""
        if not self.neighbors:
            return (0.0, 0.0)

        avg_vel_x = sum(n.velocity_x for n in self.neighbors) / len(self.neighbors)
        avg_vel_y = sum(n.velocity_y for n in self.neighbors) / len(self.neighbors)

        return (avg_vel_x, avg_vel_y)

    def cohesion(self) -> tuple[float, float]:
        """Calculate cohesion force to move toward neighbors' center."""
        if not self.neighbors:
            return (0.0, 0.0)

        center_x = sum(n.x for n in self.neighbors) / len(self.neighbors)
        center_y = sum(n.y for n in self.neighbors) / len(self.neighbors)

        dx = center_x - self.entity.x
        dy = center_y - self.entity.y

        return (dx, dy)

    def update(self, dt: float, game_state: dict) -> None:
        """Update the flocking AI."""
        # Get all entities from game state
        entities = game_state.get("entities", [])
        self.find_neighbors(entities)

        # Calculate forces
        sep_x, sep_y = self.separation()
        align_x, align_y = self.alignment()
        coh_x, coh_y = self.cohesion()

        # Combine forces
        total_x = (
            sep_x * self.separation_weight
            + align_x * self.alignment_weight
            + coh_x * self.cohesion_weight
        )
        total_y = (
            sep_y * self.separation_weight
            + align_y * self.alignment_weight
            + coh_y * self.cohesion_weight
        )

        # Normalize and apply speed
        magnitude = (total_x**2 + total_y**2) ** 0.5
        if magnitude > 0:
            self.entity.velocity_x = (total_x / magnitude) * self.speed
            self.entity.velocity_y = (total_y / magnitude) * self.speed
