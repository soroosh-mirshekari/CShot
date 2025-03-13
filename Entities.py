from abc import ABC, abstractmethod
from random import randint
import pygame

# an Instanst
class Entity(ABC): 
    @abstractmethod
    def __init__(self, BORDER_THICKNESS, WIDTH, HEIGHT, screen,):
        self._BORDER_THICKNESS = BORDER_THICKNESS
        self._WIDTH = WIDTH
        self._HEIGHT = HEIGHT
        self._screen = screen

    def random_placement(self):
        pass

class Aim(Entity):
    def __init__(self, BORDER_THICKNESS, WIDTH, HEIGHT, screen,aim_speed, aim_size, AIM_COLOR, key):
        super().__init__(BORDER_THICKNESS, WIDTH, HEIGHT, screen)
        self.__aim_speed = aim_speed
        self.__aim_size = aim_size
        self.__color = AIM_COLOR
        self.__key = key
        


    def random_placement(self):
        self.__x_axis = randint(self._BORDER_THICKNESS,self._WIDTH-self._BORDER_THICKNESS)
        self.__y_axis = randint(self._BORDER_THICKNESS,self._HEIGHT-self._BORDER_THICKNESS)
        pygame.draw.circle(self._screen, self.__color, (self.__x_axis, self.__y_axis), self.__aim_size)
        # aim_speed = self.__aim_speed
        return 

    def press_key(self, keys, DARK_BG = (30, 30, 30), LIGHT_BORDER = (200, 200, 200)):
        
        # Move aim based on WASD keys
        if keys[self.__key[0]]:
            self.__y_axis -= self.__aim_speed
        elif keys[self.__key[1]]:
            self.__y_axis += self.__aim_speed
        elif keys[self.__key[2]]:
            self.__x_axis -= self.__aim_speed
        elif keys[self.__key[3]]:
            self.__x_axis += self.__aim_speed

        # Keep aim within screen bounds
        self.__x_axis = max(self.__aim_size + self._BORDER_THICKNESS, min(self.__x_axis, self._WIDTH - self.__aim_size  - self._BORDER_THICKNESS))
        self.__y_axis = max(self.__aim_size + self._BORDER_THICKNESS, min(self.__y_axis, self._HEIGHT - self.__aim_size  - self._BORDER_THICKNESS))

        # Clear the screen
        self._screen.fill(DARK_BG)
        pygame.draw.rect(self._screen, LIGHT_BORDER, (0, 0, self._WIDTH, self._HEIGHT), self._BORDER_THICKNESS)
        
        # Draw aim
        pygame.draw.circle(self._screen, self.__color, (self.__x_axis, self.__y_axis),self.__aim_size)
        
        # Update the display
        pygame.display.flip()