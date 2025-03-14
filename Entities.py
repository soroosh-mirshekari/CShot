# entities.py
from abc import ABC, abstractmethod
import pygame
from random import randint
# an Instanst
class Entity(ABC):
    @abstractmethod
    def __init__(self, border_thickness, width, height, screen):
        self.__border_thickness = border_thickness
        self.__width = width
        self.__height = height
        self.__screen = screen

    @abstractmethod
    def random_placement(self):
        pass

    # Getter methods for private variables
    def get_border_thickness(self):
        return self.__border_thickness

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_screen(self):
        return self.__screen

class Aim(Entity):
    def __init__(self, border_thickness, width, height, screen, speed, size, color, controls):
        super().__init__(border_thickness, width, height, screen)
        self.__speed = speed
        self.__size = size
        self.__color = color
        self.__controls = controls
        self.__x = randint(border_thickness, width - border_thickness)
        self.__y = randint(border_thickness, height - border_thickness)

    def random_placement(self):
        self.__x = randint(self.get_border_thickness(), self.get_width() - self.get_border_thickness())
        self.__y = randint(self.get_border_thickness(), self.get_height() - self.get_border_thickness())

    def press_key(self, keys):

        # Move aim based on WASD keys
        if keys[self.__controls[0]]:  # Up
            self.__y -= self.__speed
        if keys[self.__controls[1]]:  # Down
            self.__y += self.__speed
        if keys[self.__controls[2]]:  # Left
            self.__x -= self.__speed
        if keys[self.__controls[3]]:  # Right
            self.__x += self.__speed

        # Keep aim within screen bounds
        self.__x = max(self.get_border_thickness(), min(self.__x, self.get_width() - self.get_border_thickness()))
        self.__y = max(self.get_border_thickness(), min(self.__y, self.get_height() - self.get_border_thickness()))

    def draw(self):  # Draw aim
        pygame.draw.circle(self.get_screen(), self.__color, (int(self.__x), int(self.__y)), self.__size)

        # Update the display
        pygame.display.flip()

    # Getter methods for private variables
    def get_speed(self):
        return self.__speed

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def get_controls(self):
        return self.__controls

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y