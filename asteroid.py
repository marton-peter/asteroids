import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):  
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        random_dir_1 = self.velocity.rotate(random_angle)
        random_dir_2 = self.velocity.rotate(-random_angle)
        child_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_1.velocity = self.velocity.rotate(random_angle) * 1.2
        child_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_2.velocity = self.velocity.rotate(-random_angle) * 1.2