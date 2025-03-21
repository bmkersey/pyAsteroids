import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import sys

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updateable, drawable)
  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = (updateable)
  Shot.containers = (shots, updateable, drawable)
  field = AsteroidField()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill(BLACK)
    dt = clock.tick(60) / 1000
    updateable.update(dt)
    for asteroid in asteroids:
      if asteroid.collision_check(player):
        print("Game Over!")
        sys.exit()
      for shot in shots:
        if asteroid.collision_check(shot):
          asteroid.split()
          shot.kill()
    
    

    for d in drawable:
      d.draw(screen)
    pygame.display.flip()


if __name__ == "__main__":
  main()