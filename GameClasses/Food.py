import random


class Food:
    """
    This class is used to create food objects.
    Food objects are used to feed the snake and make it grow.
    """
    def __init__(self, x, y):
        """
        Constructor
        :param x: x coordinate of the food
        :param y: y coordinate of the food
        """
        self.x = x
        self.y = y

    def update(self, snake):
        """
        This method is used to update the food object.
        :param snake: The snake object
        :return: None
        """
        # check if the snake has eaten the food
        if snake.snake_list[0][0] == self.x and snake.snake_list[0][1] == self.y:
            self.x = 10 * int(30 * random.random())
            self.y = 10 * int(30 * random.random())
            # create new snake part at the current position
            snake.snake_list.append([self.x, self.y])
