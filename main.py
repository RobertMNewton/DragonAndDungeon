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
from managers.world_manager import WorldManager


if __name__ == "__main__":
    # initialise pygame
    pygame.init()

    # create drawing window
    SCREEN_WIDTH = 480 * 3
    SCREEN_HEIGHT = 320 * 3

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Entity(
        Sprite("assets/character_designs/ragged_man.png", trans_c=(255, 255, 255), size=(16 * 3, 32 * 3)),
        Position(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2, z=1),
        Velocity(),
        Control(),
        VelocityDecay(decay=0.5)
    )
    player.add_tag("player")

    renderer = Renderer(screen)

    renderer.add_entity(player)

    controller = Controller(player)

    movement_manager = MovementProcessor()

    movement_manager.add_entity(player)

    world_manager = WorldManager(player, size=(16 * 3, 16 * 3))
    new_tiles = world_manager.generate_initial_tiles()
    old_tiles = []

    # main game loop
    running = True
    while running:
        if len(new_tiles) > 0:
            renderer.add_entities(new_tiles)
        if len(old_tiles) > 0:
            renderer.remove_entities(old_tiles)

        controller.update()
        movement_manager.update()
        renderer.update()

        new_tiles, old_tiles = world_manager.update()

        if pygame.event.get(pygame.QUIT):
            running = False

        pygame.display.flip()
        pygame.event.pump()

    pygame.quit()
