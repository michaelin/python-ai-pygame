"""
Test configuration for pytest.
"""

import pygame
import pytest


@pytest.fixture(scope="session", autouse=True)
def pygame_init():
    """Initialize pygame for all tests."""
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def mock_screen():
    """Create a mock pygame screen for testing."""
    return pygame.Surface((800, 600))
