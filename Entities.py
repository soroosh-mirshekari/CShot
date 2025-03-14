# entities.py
from abc import ABC, abstractmethod
import pygame
from random import randint

# an Instanst
class Entity(ABC):
    @abstractmethod
    def __init__(self, border_thickness, width, height, screen):
        self._border_thickness = border_thickness
        self._width = width
        self._height = height
        self._screen = screen

    @abstractmethod
    def random_placement(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Aim(Entity):

    def __init__(self, border_thickness, width, height, screen, speed, size, color, controls):
        super().__init__(border_thickness, width, height, screen)
        self.__speed = speed
        self.__size = size
        self.__color = color
        self.__controls = controls
        self.__x = randint(border_thickness, width - border_thickness)
        self.__y = randint(border_thickness, height - border_thickness)
        self.__shots_xy = []

    def random_placement(self):
        self.__x = randint(self._border_thickness, self._width - self._border_thickness)
        self.__y = randint(self._border_thickness, self._height - self._border_thickness)
        self.__rect = pygame.Rect(self.__x - self.__size, self.__y + self.__size, self.__size * 2, self.__size * 2) # Create a rect for the aim

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
        self.__x = max(self._border_thickness, min(self.__x, self._width - self._border_thickness))
        self.__y = max(self._border_thickness, min(self.__y, self._height - self._border_thickness))

        self.__rect.center = (self.__x, self.__y) #update the rect

    def draw(self):  # Draw aim
        pygame.draw.circle(self._screen, self.__color, (int(self.__x), int(self.__y)), self.__size)

        for shot_x, shot_y in self.__shots_xy: # draw shots 
            pygame.draw.circle(self._screen, self.__color, (shot_x, shot_y), self.__size)

    def shot(self):# add x, y axis 
        self.__shots_xy.append((self.__x, self.__y))
    
    def check_collision(self, target):
        return self.__rect.colliderect(target.rect)

class Target(Entity):
    def __init__(self, border_thickness, width, height, screen):
        super().__init__(border_thickness, width, height, screen)
        self.rect = None

    def random_placement(self):
        self.__x = randint(self._border_thickness*2, self._width - 5*self._border_thickness)
        self.__y = randint(self._border_thickness*2, self._height - 5*self._border_thickness)

    def draw(self):
        target_image = pygame.image.load("target_icon.png").convert_alpha()  # Load target image
        target_image = pygame.transform.scale(target_image, (40, 40)) #resizes the image

        # create a rect 
        self.rect = target_image.get_rect()
        self.rect.x = self.__x
        self.rect.y = self.__y
        # draw
        self._screen.blit(target_image, self.rect)
