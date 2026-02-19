class GameOver:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font('assets/fonts/font.ttf', 48)
        self.game_over_surface = self.font.render('Game Over', True, (255, 0, 0))
        self.score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.restart_surface = self.font.render('Press R to Restart', True, (255, 255, 255))

    def display(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_over_surface, (self.screen.get_width() // 2 - self.game_over_surface.get_width() // 2, 100))
        self.screen.blit(self.score_surface, (self.screen.get_width() // 2 - self.score_surface.get_width() // 2, 200))
        self.screen.blit(self.restart_surface, (self.screen.get_width() // 2 - self.restart_surface.get_width() // 2, 300))
        pygame.display.flip()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return True
        return False