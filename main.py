import pygame
from entities.entity import Entity
from components.position import Position
from components.sprite import Sprite
from components.velocity import Velocity
from components.velocity_decay import VelocityDecay
from components.control import Control
from components.camera import CameraComponent
from components.scene_component import SceneComponent
from managers.camera_manager import CameraManager
from managers.control import Controller
from managers.movement import MovementProcessor
from managers.scene_manager import SceneManager
from utils.world import World
from constants import *


if __name__ == "__main__":
    # initialise pygame
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Entity(
        Sprite("assets/character_designs/ragged_man.png", trans_c=(255, 255, 255), size=(16 * 3, 32 * 3)),
        Position(0, 0, 1),
        Velocity(),
        Control(),
        VelocityDecay(decay=0.5)
    )
    player.add_tag("player")

    world = World(seed=123)

    scene = Entity()
    scene.add_component(
        SceneComponent(
            SCENE_SIZE
        )
    )

    scene_manager = SceneManager(scene, world)
    scene_manager.initialise_scene(player)

    camera = Entity()
    camera.add_component(
        CameraComponent(
            0,
            0,
            0,
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            (VIEW_WIDTH, VIEW_HEIGHT)
        )
    )

    camera_manager = CameraManager(camera, scene, player)

    control_manager = Controller(player)

    movement_manager = MovementProcessor()
    movement_manager.add_entity(player)

    # main game loop
    running = True
    while running:
        control_manager.update()
        movement_manager.update()
        scene_manager.update()

        if pygame.event.get(pygame.QUIT):
            running = False

        screen.blit(camera_manager.update(), (0, 0))
        pygame.display.flip()

        pygame.event.pump()

    pygame.quit()
