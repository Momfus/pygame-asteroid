import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create pygame sprite groups
    updatable = pygame.sprite.Group()  # Cambiado a Group
    drawable = pygame.sprite.Group()   # Cambiado a Group
    asteroids = pygame.sprite.Group()

    # Set static containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create the Clock object and dt variable (BEFORE the game loop)
    clock = pygame.time.Clock()
    dt = 0  # Variable to store delta time (time between frames)

    # Instantiate the Player object at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Instantiate the AsteroidField object
    asteroid_field = AsteroidField()

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Fill the screen with black color
        screen.fill("black")

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Update the screen (always at the end of the loop)
        pygame.display.flip()

        # Control FPS and update dt (INSIDE the game loop, at the end)
        dt = clock.tick(60) / 1000  # Cap FPS to 60 (60 FPS)

    # Exit the game
    pygame.quit()

if __name__ == "__main__":
    main()