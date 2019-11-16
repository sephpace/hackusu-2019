
import pygame
import numpy as np

from scene import Scene

from gameobjects import Planet, Projectile, City


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
    scene.add(Planet((0., 0.)))
    scene.add(Projectile((50., 0.)))
    scene.add(City((7.5, -14.5), color=(0, 0, 255), rotation=.5))

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
                    scene.camera.move_up = True
                if key == pygame.K_a:
                    scene.camera.move_left = True
                if key == pygame.K_s:
                    scene.camera.move_down = True
                if key == pygame.K_d:
                    scene.camera.move_right = True

            if event.type == pygame.KEYUP:
                key = event.key
                if key == pygame.K_w:
                    scene.camera.move_up = False
                if key == pygame.K_a:
                    scene.camera.move_left = False
                if key == pygame.K_s:
                    scene.camera.move_down = False
                if key == pygame.K_d:
                    scene.camera.move_right = False

            # Mouse events
            if event.type == pygame.MOUSEMOTION:
                _, _, right_click = event.buttons
                if right_click:
                    print(scene.pixel_to_coord(np.array(event.pos)))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    print(scene.pixel_to_coord(np.array(event.pos)))

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update the scene
        scene.update()

        # Update the display
        pygame.display.update()

        # Set frame rate to 60 fps
        clock.tick(60)

    # Stop the game
    stop()


def stop():
    pygame.quit()
    exit(0)
