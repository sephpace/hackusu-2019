
import pygame

from scene import Scene


def start():
    pygame.init()

    screen = pygame.display.set_mode((1000, 700))
    clock = pygame.time.Clock()

    scene = setup(screen)
    main_loop(screen, scene, clock)


def setup(screen):
    # Initialize the scene object
    scene = Scene(screen)

    # Add game objects to the scene
    # TODO: Add game objects here

    return scene


def main_loop(screen, scene, clock):
    running = True
    while running:
        # Get input from the user
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                running = False

            # Key events
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_w:
                    pass
                if key == pygame.K_a:
                    pass
                if key == pygame.K_s:
                    pass
                if key == pygame.K_d:
                    pass

            # Mouse events
            # TODO: Add mouse events

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update the scene
        scene.update()

        # Set frame rate to 60 fps
        clock.tick(60)

    # Stop the game
    stop()


def stop():
    pygame.quit()
    exit(0)
