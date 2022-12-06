import pygame
from entities.entity import Entity
from components.position import Position
from components.sprite import Sprite
from components.velocity import Velocity
from components.velocity_decay import VelocityDecay
from components.control import Control
from managers.render import Renderer
from managers.control import Controller
from managers.movement import MovementProcessor


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
        Velocity(),
        Control(),
        VelocityDecay(decay=0.8)
    )

    renderer = Renderer(screen)

    renderer.add_entity(player)

    controller = Controller(player)

    movement_manager = MovementProcessor()

    movement_manager.add_entity(player)

    # main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # FF00CA
        test_surf = pygame.transform.scale(pygame.image.load("test_map.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(test_surf, (0, 0))

        controller.update()
        movement_manager.update()
        renderer.update()

        pygame.display.flip()

    pygame.quit()
