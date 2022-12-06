import pygame
from entities.entity import Entity
from components.position import Position
from components.sprite import Sprite
from components.velocity import Velocity
from processors.render import Renderer


if __name__ == "__main__":
    # initialise pygame
    pygame.init()

    # create drawing window
    SCREEN_WIDTH = 480 * 3
    SCREEN_HEIGHT = 320 * 3

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Entity(
        Sprite("Assets/Character Designs/ragged_man.png", trans_c=(255, 255, 255), size=(16 * 3, 32 * 3)),
        Position(start_x=SCREEN_WIDTH // 2, start_y=SCREEN_HEIGHT // 2),
        Velocity()
    )

    renderer = Renderer(screen)

    renderer.add_entity(player)

    # main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # FF00CA
        test_surf = pygame.transform.scale(pygame.image.load("test_map.png"), (SCREEN_WIDTH, SCREEN_WIDTH))
        screen.blit(test_surf, (0, 0))

        renderer.update()

        pygame.display.flip()

    pygame.quit()
