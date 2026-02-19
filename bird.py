class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0.5
        self.velocity = 0
        self.image = self.load_image()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def load_image(self):
        # Load the bird image here
        pass

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def flap(self):
        self.velocity = -10  # Flap effect

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))