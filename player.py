import pygame as pg

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward.elementwise() * self.radius
        b = (self.position - forward.elementwise() * self.radius).elementwise() - right
        c = (self.position - forward.elementwise() * self.radius).elementwise() + right
        return [a, b, c]

    def draw(self, screen):
        pg.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.rotate(-dt)
        elif keys[pg.K_d]:
            self.rotate(dt)
        elif keys[pg.K_w]:
            self.move(dt)
        elif keys[pg.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_SPEED

