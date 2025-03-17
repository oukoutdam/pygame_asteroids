import pygame as pg

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

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
        self.shot_timer -= dt

        if keys[pg.K_a]:
            self.rotate(-dt)
        elif keys[pg.K_d]:
            self.rotate(dt)
        elif keys[pg.K_w]:
            self.move(dt)
        elif keys[pg.K_s]:
            self.move(-dt)
        elif keys[pg.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_SPEED

    def shoot(self):
        if self.shot_timer > 0:
            return

        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pg.Vector2(0, 1).rotate(self.rotation).elementwise() * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

