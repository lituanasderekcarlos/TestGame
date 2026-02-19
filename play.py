class Play:
    def __init__(self, game):
        self.game = game
        self.bird = None  # Initialize the bird object
        self.pipes = []  # List to hold pipe objects
        self.background = None  # Initialize the background object
        self.score = 0  # Initialize the score
        self.game_over = False  # Flag to check if the game is over

    def initialize(self):
        # Initialize game objects like bird, pipes, and background
        from sprites.bird import Bird
        from sprites.pipe import Pipe
        from sprites.background import Background

        self.bird = Bird()
        self.background = Background()
        self.pipes = [Pipe() for _ in range(3)]  # Create initial pipes

    def update(self):
        # Update game state
        if not self.game_over:
            self.bird.update()
            for pipe in self.pipes:
                pipe.update()
                if self.check_collision(pipe):
                    self.game_over = True
            self.background.update()

    def render(self, screen):
        # Render game objects on the screen
        self.background.render(screen)
        self.bird.render(screen)
        for pipe in self.pipes:
            pipe.render(screen)

    def check_collision(self, pipe):
        # Check for collision between bird and pipe
        return self.bird.rect.colliderect(pipe.rect)

    def reset(self):
        # Reset the game state for a new game
        self.initialize()
        self.score = 0
        self.game_over = False