class Background:
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height
        self.x1 = 0
        self.x2 = self.width

    def update(self, speed):
        self.x1 -= speed
        self.x2 -= speed

        if self.x1 <= -self.width:
            self.x1 = self.width
        if self.x2 <= -self.width:
            self.x2 = self.width

    def render(self, screen):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))