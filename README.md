# Python AI Pygame Project

A Python game project built with pygame-ce, featuring AI components and modern Python tooling.

## Setup

1. Install uv (if not already installed):
   ```bash
   pip install uv
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   uv pip sync requirements.txt
   ```

3. Install development dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```

## Development

### Running the Game
```bash
uv run python src/main.py
```

### Code Quality
- **Linting and Formatting**: `uv run ruff check . && uv run ruff format .`
- **Type Checking**: (Add mypy if needed)
- **Testing**: `uv run pytest`

### Project Structure
```
src/
├── main.py          # Entry point
├── game/            # Game logic
│   ├── __init__.py
│   ├── engine.py    # Game engine
│   ├── entities.py  # Game entities
│   └── scenes.py    # Game scenes
├── ai/              # AI components
│   ├── __init__.py
│   └── agents.py    # AI agents
└── utils/           # Utilities
    ├── __init__.py
    └── constants.py  # Game constants

tests/               # Test files
assets/              # Game assets (images, sounds, etc.)
```

## Requirements

- Python 3.11+
- pygame-ce 2.5.0+
- uv for dependency management

## Contributing

1. Run tests: `uv run pytest`
2. Check code quality: `uv run ruff check . && uv run ruff format .`
3. Ensure all tests pass before committing
