import pygame
from GameClasses.Snake import Snake
from GameClasses.Food import Food


class Game:
    """
    This is the main game class. It contains the main game loop and all the game logic.
    """
    def __init__(self):
        """
        Constructor
        """
        self.width = 300
        self.height = 300
        self.snake = Snake(150, 150)
        self.food = Food(100, 100)
        self.running = True

    def run(self):
        """
        Main game loop
        :return: None
        """
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # check if a key is pressed : if yes, change the direction of the snake
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = 'up'
                    if event.key == pygame.K_DOWN:
                        self.snake.direction = 'down'
                    if event.key == pygame.K_LEFT:
                        self.snake.direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        self.snake.direction = 'right'
            # set background color : white
            screen.fill((255, 255, 255))
            self.snake.update()
            self.food.update(self.snake)
            # draw the snake : for the each snake part, draw a rectangle
            for x, y in self.snake.snake_list:
                if x < 0 or x > 300 or y < 0 or y > 300:
                    self.running = False
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 10, 10), 0)
            pygame.draw.rect(screen, (255, 0, 0), (self.food.x, self.food.y, 10, 10), 0)
            pygame.display.update()
            # 30 Frames per second
            clock.tick(30)
        pygame.quit()
