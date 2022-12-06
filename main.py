import pygame


if __name__ == "__main__":
    # initialise pygame
    pygame.init()

    # create drawing window
    SCREEN_WIDTH = 480 * 3
    SCREEN_HEIGHT = 320 * 3

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    # main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        test_surf = pygame.transform.scale(pygame.image.load("test_map.png"), (SCREEN_WIDTH, SCREEN_WIDTH))
        screen.blit(test_surf, (0, 0))

        pygame.display.flip()

    pygame.quit()
