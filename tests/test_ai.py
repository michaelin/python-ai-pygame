"""
Tests for AI agents.
"""

from ai.agents import ChasingAI, SimpleAI
from game.entities import Entity


class MockEntity(Entity):
    """Mock entity for testing."""

    def update(self, dt):
        pass

    def render(self, screen):
        pass


class TestSimpleAI:
    """Test the SimpleAI agent."""

    def test_simple_ai_initialization(self):
        """Test SimpleAI is properly initialized."""
        entity = MockEntity(10, 20, 5, 5)
        ai = SimpleAI(entity)

        assert ai.entity == entity
        assert ai.active is True
        assert ai.direction_change_timer == 0.0
        assert ai.direction_change_interval == 2.0
        assert ai.speed == 50.0

    def test_simple_ai_update_no_direction_change(self):
        """Test SimpleAI update without direction change."""
        entity = MockEntity(10, 20, 5, 5)
        ai = SimpleAI(entity)

        # Should not change direction yet
        ai.update(1.0, {})  # 1 second, less than 2 second interval
        assert ai.direction_change_timer == 1.0

    def test_simple_ai_update_with_direction_change(self):
        """Test SimpleAI update with direction change."""
        entity = MockEntity(10, 20, 5, 5)
        ai = SimpleAI(entity)

        # Force direction change
        ai.update(2.5, {})  # 2.5 seconds, more than 2 second interval

        # Timer should reset
        assert ai.direction_change_timer == 0.0
        # Velocity should be set (non-zero)
        assert entity.velocity_x != 0 or entity.velocity_y != 0


class TestChasingAI:
    """Test the ChasingAI agent."""

    def test_chasing_ai_initialization(self):
        """Test ChasingAI is properly initialized."""
        entity = MockEntity(10, 20, 5, 5)
        ai = ChasingAI(entity, speed=150.0)

        assert ai.entity == entity
        assert ai.active is True
        assert ai.speed == 150.0
        assert ai.target is None

    def test_chasing_ai_set_target(self):
        """Test setting a target for ChasingAI."""
        entity = MockEntity(10, 20, 5, 5)
        target = MockEntity(50, 60, 5, 5)
        ai = ChasingAI(entity)

        ai.set_target(target)
        assert ai.target == target

    def test_chasing_ai_update_no_target(self):
        """Test ChasingAI update with no target."""
        entity = MockEntity(10, 20, 5, 5)
        ai = ChasingAI(entity)

        ai.update(0.1, {})
        # Should not change velocity without target
        assert entity.velocity_x == 0
        assert entity.velocity_y == 0

    def test_chasing_ai_update_with_target(self):
        """Test ChasingAI update with a target."""
        entity = MockEntity(0, 0, 5, 5)
        target = MockEntity(100, 0, 5, 5)  # Target to the right
        ai = ChasingAI(entity, speed=100.0)
        ai.set_target(target)

        ai.update(0.1, {})

        # Should move towards target (positive x direction)
        assert entity.velocity_x > 0
        assert entity.velocity_y == 0

    def test_chasing_ai_update_same_position(self):
        """Test ChasingAI when entity and target are at same position."""
        entity = MockEntity(50, 50, 5, 5)
        target = MockEntity(50, 50, 5, 5)  # Same position
        ai = ChasingAI(entity)
        ai.set_target(target)

        ai.update(0.1, {})

        # Should not move when at same position
        assert entity.velocity_x == 0
        assert entity.velocity_y == 0
