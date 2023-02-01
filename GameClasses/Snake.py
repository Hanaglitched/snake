

class Snake:
    """
    This is used to create snake objects.
    Snake objects are used to move around the screen and eat food.
    """
    def __init__(self, x, y):
        """
        Constructor
        :param x: x coordinate of the snake
        :param y: y coordinate of the snake
        """
        self.x = x
        self.y = y
        self.snake_list = [[x, y]]
        self.direction = 'right'
        self.update_counter = 0

    def update(self):
        """
        This method is used to update the snake object.
        :return: None
        """
        if self.update_counter % 10 == 0:
            x, y = self.snake_list[0]
            if self.direction == 'right':
                x += 10
            elif self.direction == 'left':
                x -= 10
            elif self.direction == 'up':
                y -= 10
            elif self.direction == 'down':
                y += 10
            self.snake_list.insert(0, [x, y])
            self.snake_list.pop()
        self.update_counter += 1
