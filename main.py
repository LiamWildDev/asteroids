import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")

        for obj in asteroids:
            if player.check_collisions(obj):
                print("Game over!")
                pygame.quit()
            for bullet in shots:
                if bullet.check_collisions(obj):
                    obj.split()
                    bullet.kill()

        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        
        
if __name__ == "__main__":
    main()