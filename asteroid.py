import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)
      self.rotation = 0
      self.rotation_speed = 0.1
   
   def draw(self, screen):
      # Draw the asteroid as a circle
      pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, 2)
   
   def update(self, dt):
      self.position += self.velocity * dt