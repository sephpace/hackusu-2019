
import pygame
import numpy as np

from scene import Scene

from gameobjects import Planet, Projectile, City


def start():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((1000, 700))
    clock = pygame.time.Clock()

    scene, player1, player2 = setup(screen)
    main_loop(screen, scene, clock, player1, player2)


def setup(screen):
    # Initialize the scene object
    scene = Scene(screen)

    # Add game objects to the scene
    planets = [Planet((50., 20.), color=(200, 100, 255)), Planet((-50., 20.), color=(100, 255, 100)), Planet((0., -20.), scale=25., color=(255, 255, 100))]
    for planet in planets:
        scene.add(planet)
    player1 = City((-57.5, 5.5), color=(0, 0, 255), rotation=-.5)
    player2 = City((57.5, 5.5), color=(255, 0, 0), rotation=.5)
    scene.add(player1)
    scene.add(player2)

    return scene, player1, player2


def main_loop(screen, scene, clock, player1, player2):
    font = pygame.font.SysFont('arial', 30)

    running = True
    active_player = player1
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
                    # TODO: Implement screen dragging with right click
                    # print(scene.pixel_to_coord(np.array(event.pos)))
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    active_player.shoot(scene, scene.pixel_to_coord(np.array(event.pos)))

                    # Swap turns
                    if active_player == player1:
                        active_player = player2
                    else:
                        active_player = player1

        # Clear the screen
        screen.fill((0, 0, 0))

        # Display the player whose turn it is
        if active_player == player1:
            text = font.render('Player 1\'s Turn', False, player1.color)
            screen.blit(text, (0, 0, text.get_width(), text.get_height()))
        else:
            text = font.render('Player 2\'s Turn', False, player2.color)
            screen.blit(text, (0, 0, text.get_width(), text.get_height()))

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
