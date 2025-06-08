"""
Tests for game entities.
"""

import pygame
import pytest

from game.entities import Enemy, Entity, Player


class TestEntity:
    """Test the base Entity class."""

    def test_entity_initialization(self):
        """Test entity is properly initialized."""

        class TestEntity(Entity):
            def update(self, dt):
                pass

            def render(self, screen):
                pass

        entity = TestEntity(10, 20, 30, 40)
        assert entity.x == 10
        assert entity.y == 20
        assert entity.width == 30
        assert entity.height == 40
        assert entity.velocity_x == 0.0
        assert entity.velocity_y == 0.0
        assert entity.active is True

    def test_entity_position_property(self):
        """Test entity position property."""

        class TestEntity(Entity):
            def update(self, dt):
                pass

            def render(self, screen):
                pass

        entity = TestEntity(15, 25, 10, 10)
        assert entity.position == (15, 25)

    def test_entity_rect_property(self):
        """Test entity rect property."""

        class TestEntity(Entity):
            def update(self, dt):
                pass

            def render(self, screen):
                pass

        entity = TestEntity(10, 20, 30, 40)
        rect = entity.rect
        assert rect.x == 10
        assert rect.y == 20
        assert rect.width == 30
        assert rect.height == 40

    def test_entity_move(self):
        """Test entity movement."""

        class TestEntity(Entity):
            def update(self, dt):
                pass

            def render(self, screen):
                pass

        entity = TestEntity(0, 0, 10, 10)
        entity.velocity_x = 100
        entity.velocity_y = 50
        entity.move(0.1)  # 0.1 seconds

        assert entity.x == 10  # 100 * 0.1
        assert entity.y == 5  # 50 * 0.1


class TestPlayer:
    """Test the Player entity."""

    def test_player_initialization(self):
        """Test player is properly initialized."""
        player = Player(50, 60)
        assert player.x == 50
        assert player.y == 60
        assert player.width == 32
        assert player.height == 32
        assert player.speed == 200.0

    def test_player_update_no_input(self):
        """Test player update with no input."""
        player = Player(100, 100)

        # Mock no keys pressed - return False for all key checks
        def mock_get_pressed():
            # Create a mock that returns False for any key access
            class MockKeys:
                def __getitem__(self, key):
                    return False

            return MockKeys()

        with pytest.MonkeyPatch().context() as m:
            m.setattr(pygame.key, "get_pressed", mock_get_pressed)
            player.update(0.1)

        assert player.velocity_x == 0.0
        assert player.velocity_y == 0.0

    def test_player_render(self, mock_screen):
        """Test player rendering."""
        player = Player(100, 100)
        # Should not raise any exceptions
        player.render(mock_screen)


class TestEnemy:
    """Test the Enemy entity."""

    def test_enemy_initialization(self):
        """Test enemy is properly initialized."""
        enemy = Enemy(75, 85)
        assert enemy.x == 75
        assert enemy.y == 85
        assert enemy.width == 24
        assert enemy.height == 24
        assert enemy.speed == 100.0

    def test_enemy_update(self):
        """Test enemy update behavior."""
        enemy = Enemy(0, 0)
        enemy.update(0.1)

        # Enemy should move towards center (400, 300)
        assert enemy.velocity_x > 0  # Moving right towards center
        assert enemy.velocity_y > 0  # Moving down towards center

    def test_enemy_render(self, mock_screen):
        """Test enemy rendering."""
        enemy = Enemy(200, 200)
        # Should not raise any exceptions
        enemy.render(mock_screen)
