class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('assets/fonts/your_font.ttf', 48)
        self.title = self.font.render('Flappy Bird', True, (255, 255, 255))
        self.start_text = self.font.render('Press SPACE to Start', True, (255, 255, 255))
        self.background = Background()  # Assuming Background class is implemented

    def display(self):
        self.background.update()  # Update background position
        self.background.render(self.screen)  # Render background
        self.screen.blit(self.title, (self.screen.get_width() // 2 - self.title.get_width() // 2, 100))
        self.screen.blit(self.start_text, (self.screen.get_width() // 2 - self.start_text.get_width() // 2, 300))
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Signal to start the game
        return False  # No input to start the game yet