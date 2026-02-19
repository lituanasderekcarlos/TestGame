import pygame
from sprites.bird import Bird
from sprites.pipe import Pipe
from sprites.background import Background
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_SPEED

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.running = True
        self.bird = Bird()
        self.pipes = []
        self.background = Background()
        self.score = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(GAME_SPEED)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()

    def update(self):
        self.bird.update()
        self.update_pipes()
        self.check_collisions()

    def update_pipes(self):
        if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - 200:
            self.pipes.append(Pipe())
        for pipe in self.pipes:
            pipe.update()
            if pipe.off_screen():
                self.pipes.remove(pipe)
                self.score += 1

    def check_collisions(self):
        for pipe in self.pipes:
            if self.bird.collides_with(pipe):
                self.running = False

    def render(self):
        self.background.render(self.screen)
        self.bird.render(self.screen)
        for pipe in self.pipes:
            pipe.render(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()