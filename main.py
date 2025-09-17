import pygame # pyright: ignore[reportMissingImports]
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        rt = clock.tick(FPS)
        dt = rt/1000


if __name__ == "__main__":
    main()
