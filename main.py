import pygame


if __name__ == "__main__":
    # initialise pygame
    pygame.init()

    # create drawing window
    screen = pygame.display.set_mode(size=(1920, 1080))

    # main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 170, 0))

        pygame.display.flip()

    pygame.quit()
