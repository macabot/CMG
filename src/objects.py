"""By Michael Cabot, Steven Laan, Richard Rozeboom"""

import pygame
from random import randint

# Own imports
import utils

class GameObject(object):
    """Abstract superclass for all objects in the game."""
    world = None
	def __init__(self, pos=(0, 0), frames=None):
			super(Sprite, self).__init__()
			self.image = frames[0][0]
			self.rect = self.image.get_rect()
			self.pos = pos
			

    def update(self):
        """Executes the main logic of the object. This method is called every 
        timestep."""
        raise NotImplementedError()
		

    def _get_pos(self):
        """Check the current position of the sprite on the map."""

        return (self.rect.midbottom[0]-12)/24, (self.rect.midbottom[1]-16)/16

    def _set_pos(self, pos):
        """Set the position and depth of the sprite on the map."""

        self.rect.midbottom = pos[0]*24+12, pos[1]*16+16
        self.depth = self.rect.midbottom[1]

    pos = property(_get_pos, _set_pos)

    def move(self, dx, dy):
        """Change the position of the sprite on screen."""

        self.rect.move_ip(dx, dy)
        self.depth = self.rect.midbottom[1]        

class Person(GameObject):
    """Class for one person."""

    def __init__(self, x, y, color = None, radius = 8):
        GameObject.__init__(self)
        self.pos = utils.Point(x, y)
        self.goal = None
        if color != None:
            self.color = color
        else:
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.radius = radius
        
    def __repr__(self):
        return self.pos.__repr__()
        
    def __str__(self):
        return self.__repr__()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, tuple(self.pos), self.radius, 0)

    def step(self):
        pass


class Player(Person):
    """Player object."""

    def __init__(self, x, y):
        Person.__init__(self, x, y, (255, 0, 0))
        
    def step(self):
        # Logic here!
        pass


class Cop(Person):
    """Cop object."""

    def __init__(self, x, y):
        Person.__init__(self, x, y, (0, 0, 255))
        
    def step(self):
        # Logic here!
        pass
