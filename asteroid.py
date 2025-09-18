import pygame # pyright: ignore[reportMissingImports]
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        deg = random.uniform(20, 50)

        rot1 = self.velocity.rotate(deg)
        rot2 = self.velocity.rotate(-deg)

        rad = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, rad)
        ast2 = Asteroid(self.position.x, self.position.y, rad)
        ast1.velocity = rot1 * 1.2
        ast2.velocity = rot2 * 1.2
        
