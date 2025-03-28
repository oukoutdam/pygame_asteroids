import pygame as pg

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pg.draw.circle(screen, (255,255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
