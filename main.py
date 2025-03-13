import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,ASTEROID_MIN_RADIUS,ASTEROID_KINDS, ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS


def main():
    pg.init()
    print("Starting Asteroids")
    print(f"Screen Width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.Surface.fill(screen, (0,0,0))
        pg.display.flip()

if __name__ == "__main__":
    main()
