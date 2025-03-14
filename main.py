import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,ASTEROID_MIN_RADIUS,ASTEROID_KINDS, ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS
from player import Player


def main():
    pg.init()
    print("Starting Asteroids")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    fpsClock = pg.time.Clock()
    dt = 0

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.Surface.fill(screen, (0,0,0))
        player.update(dt)
        player.draw(screen)


        pg.display.flip()
        dt = fpsClock.tick(60) / 1000

if __name__ == "__main__":
    main()
