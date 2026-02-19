# Flappy Bird Game

This is a simple 2D Flappy Bird game implemented in Python using Pygame. The objective of the game is to navigate a bird through a series of pipes without hitting them.

## Project Structure

```
flappy-bird-py
├── src
│   ├── main.py          # Entry point of the game
│   ├── game.py          # Main game logic
│   ├── settings.py      # Configuration settings
│   ├── sprites          # Contains sprite classes
│   │   ├── bird.py      # Bird character
│   │   ├── pipe.py      # Pipe obstacles
│   │   └── background.py # Background handling
│   ├── scenes           # Game scenes
│   │   ├── menu.py      # Main menu
│   │   ├── play.py      # Gameplay scene
│   │   └── game_over.py  # Game over screen
│   ├── utils            # Utility functions
│   │   └── helpers.py    # Helper functions
│   └── assets           # Game assets
│       ├── fonts        # Font files
│       └── sounds       # Sound files
├── tests                # Unit tests
│   └── test_game.py     # Tests for game logic
├── requirements.txt     # Project dependencies
├── pyproject.toml       # Project configuration
├── .gitignore           # Files to ignore in version control
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flappy-bird-py.git
   ```
2. Navigate to the project directory:
   ```
   cd flappy-bird-py
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the game, run the following command:
```
python src/main.py
```

## Controls

- Press the spacebar to make the bird jump.
- Avoid hitting the pipes.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.