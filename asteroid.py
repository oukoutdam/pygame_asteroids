import pygame as pg

import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pg.draw.circle(screen,(255,255,255), center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        split_angle = random.uniform(20, 50)
        left_split_velocity , right_split_velocity = self.velocity.rotate(-split_angle), self.velocity.rotate(split_angle)
        left_split_velocity, right_split_velocity = left_split_velocity * 1.2, right_split_velocity * 1.2
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_1.velocity = left_split_velocity
        split_2 = Asteroid(self.position.x, self.position.y, split_radius)
        split_2.velocity = right_split_velocity
