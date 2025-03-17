import asyncio
import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,ASTEROID_MIN_RADIUS,ASTEROID_KINDS, ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


pg.init()
print("Starting Asteroids")
print(f"Screen Width: {SCREEN_WIDTH}")
print(f"Screen Height: {SCREEN_HEIGHT}")

fpsClock = pg.time.Clock()

updateable = pg.sprite.Group()
drawable = pg.sprite.Group()
asteroids = pg.sprite.Group()
shots = pg.sprite.Group()

Player.containers = (updateable, drawable)
Asteroid.containers = (asteroids, updateable, drawable)
AsteroidField.containers = (updateable)
Shot.containers = (shots, updateable, drawable)

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

async def main():
    dt = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.Surface.fill(screen, (0,0,0))

        for entity in updateable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for entity in asteroids:
            if entity.detect_collision(player):
                print("Game Over!")
                exit(1)

            for shot in shots:
                if shot.detect_collision(entity):
                    entity.split()
                    shot.kill()
                    break

        pg.display.flip()
        dt = fpsClock.tick(60) / 1000
        await asyncio.sleep(0)

asyncio.run(main())
