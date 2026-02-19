class Pipe:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.passed = False

    def update(self, speed):
        self.x -= speed

    def draw(self, surface):
        # Assuming a pipe image is loaded in the game
        surface.blit(pipe_image, (self.x, self.y))
        surface.blit(pipe_image, (self.x, self.y + self.height + gap))

    def collide(self, bird_rect):
        pipe_rect_top = pygame.Rect(self.x, self.y, self.width, self.height)
        pipe_rect_bottom = pygame.Rect(self.x, self.y + self.height + gap, self.width, height - self.height - gap)
        return bird_rect.colliderect(pipe_rect_top) or bird_rect.colliderect(pipe_rect_bottom)