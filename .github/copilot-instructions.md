# Copilot Instructions for Python AI Pygame Project

## Project Overview
This is a Python game project using pygame-ce with AI components. The project uses modern Python tooling including uv for dependency management, ruff for linting/formatting, and follows a clean package structure.

## Development Philosophy
- **Small, focused changes**: Break down complex tasks into smaller, manageable pieces
- **Test-driven development**: Write tests for new functionality
- **Clean code principles**: Prioritize readability and maintainability
- **Modern Python practices**: Use type hints, dataclasses, and current idioms

## Code Style and Standards

### Python Style
- Follow PEP 8 guidelines
- Use type hints for all function parameters and return values
- Prefer f-strings for string formatting
- Use descriptive variable and function names
- Keep functions small and focused (max 20-30 lines)
- Use docstrings for all classes and public methods

### Import Organization
- Standard library imports first
- Third-party imports second
- Local imports last
- Use absolute imports within the project
- Group imports logically and sort alphabetically within groups

### Error Handling
- Use specific exception types rather than bare `except:`
- Handle errors close to where they occur
- Log errors appropriately
- Fail fast when possible

## Project Structure Rules

### File Organization
- Keep modules focused on a single responsibility
- Use meaningful file and directory names
- Place related functionality together
- Separate game logic, AI, and utilities into distinct modules

### Dependencies
- Minimize external dependencies
- Use pygame-ce for game functionality
- Prefer standard library solutions when possible
- Document any new dependencies in pyproject.toml

## Testing Guidelines

### Test Strategy
- Write unit tests for all new functions and classes
- Use pytest for all testing
- Mock external dependencies (pygame, file I/O)
- Test edge cases and error conditions
- Aim for high test coverage but focus on critical paths

### Test Structure
- One test file per source module
- Use descriptive test names that explain what is being tested
- Group related tests using classes
- Use fixtures for common test setup

## Game Development Practices

### Performance
- Profile before optimizing
- Use pygame's sprite groups for entity management
- Minimize object creation in game loops
- Cache expensive calculations

### Architecture
- Separate game state from rendering
- Use composition over inheritance for game entities
- Implement clear interfaces between systems
- Keep AI logic separate from game entities

## AI Development Guidelines

### AI Implementation
- Start with simple AI behaviors before complex ones
- Make AI behaviors configurable and tunable
- Separate AI decision-making from movement/action execution
- Test AI behaviors in isolation

### Performance Considerations
- Avoid expensive calculations in AI update loops
- Use spatial partitioning for entity queries
- Implement configurable AI update frequencies
- Profile AI systems regularly

## Tool Usage

### VS Code Integration
- Use the configured debugger for troubleshooting
- Leverage ruff for automatic formatting
- Run tests frequently using the test runner
- Use the integrated terminal for uv commands

### Git Practices
- Make small, focused commits
- Write clear commit messages that include ALL user prompts since the last commit
- Use conventional commit format when possible
- Keep the working directory clean
- When suggesting commits, include the initial prompt that started the changes and ALL subsequent prompts that contributed to the current uncommitted changes

## When Making Changes

### Before Starting
1. Understand the current code structure
2. Identify the smallest possible change
3. Consider what tests need to be added/updated
4. Check for existing similar implementations

### During Development
1. Make one logical change at a time
2. Run tests after each change
3. Use the debugger to understand code flow
4. Keep changes focused and minimal

### After Changes
1. Run the full test suite
2. Check for linting errors
3. Test the game manually
4. Update documentation if needed
5. Commmit the change

## Common Patterns to Follow

### Entity System
- Use composition for entity capabilities
- Keep entities lightweight
- Separate rendering from logic
- Use clear interfaces for entity interactions

### AI Agents
- Implement the Strategy pattern for different AI behaviors
- Keep AI state separate from entity state
- Use dependency injection for AI configuration
- Make AI behaviors easily testable

### Game Loop
- Keep the main loop simple and focused
- Separate input, update, and render phases
- Use delta time for frame-rate independent updates
- Handle errors gracefully without crashing

## Avoid These Patterns

- Large, monolithic functions
- Tight coupling between unrelated systems
- Global state when possible
- Premature optimization
- Complex inheritance hierarchies
- Magic numbers (use constants)
- Bare except clauses
- Mutable default arguments

## Questions to Ask Before Implementing

1. Is this the smallest possible change to achieve the goal?
2. Are there existing patterns in the codebase I should follow?
3. What tests need to be written or updated?
4. Will this change break existing functionality?
5. Is this change necessary or am I over-engineering?

Remember: Simple, working code is better than complex, clever code.
