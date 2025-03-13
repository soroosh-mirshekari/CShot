# entities.py
from abc import ABC, abstractmethod
import pygame
from random import randint

# an Instanst
class Entity(ABC):
    @abstractmethod
    def __init__(self, border_thickness, width, height, screen):
        self.border_thickness = border_thickness
        self.width = width
        self.height = height
        self.screen = screen

    @abstractmethod
    def random_placement(self):
        pass

class Aim(Entity):
    def __init__(self, border_thickness, width, height, screen, speed, size, color, controls):
        super().__init__(border_thickness, width, height, screen)
        self.speed = speed
        self.size = size
        self.color = color
        self.controls = controls
        self.x = randint(border_thickness, width - border_thickness)
        self.y = randint(border_thickness, height - border_thickness)

    def random_placement(self):
        self.x = randint(self.border_thickness, self.width - self.border_thickness)
        self.y = randint(self.border_thickness, self.height - self.border_thickness)

    def press_key(self, keys):

        # Move aim based on WASD keys
        if keys[self.controls[0]]:  # Up
            self.y -= self.speed
        if keys[self.controls[1]]:  # Down
            self.y += self.speed
        if keys[self.controls[2]]:  # Left
            self.x -= self.speed
        if keys[self.controls[3]]:  # Right
            self.x += self.speed

        # Keep aim within screen bounds
        self.x = max(self.border_thickness, min(self.x, self.width - self.border_thickness))
        self.y = max(self.border_thickness, min(self.y, self.height - self.border_thickness))

    

    def draw(self):  # Draw aim
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.size)

        # Update the display
        pygame.display.flip()