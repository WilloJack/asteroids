import sys
import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0 
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    #MAKES THE GAME RUN UNTIL QUIT OR CRASH
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        #TELLS THE SCREEN TO DRAW AND TO REFRESH   
        screen.fill('black')
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        #WILL CAP THE REFRESH RATE AND UPDATE "Delta time" dt WITH SAME VALUE FOR LATER USE 
        game_clock.tick(60)
        dt = game_clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()