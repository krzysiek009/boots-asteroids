import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(25, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        left_velocity = self.velocity.rotate(angle)
        right_velocity = self.velocity.rotate(-angle)

        left = Asteroid(self.position[0], self.position[1], radius)
        right = Asteroid(self.position[0], self.position[1], radius)

        left.velocity = left_velocity * 1.2
        right.velocity = right_velocity * 1.2
