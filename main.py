import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        
        # player.update(dt)
        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        for rock in asteroids:
            if rock.is_colision(player):
                print("Game over!")
                exit()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
