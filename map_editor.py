import pygame
from entities.entity import Entity
from components.position import Position
from components.sprite import Sprite
from components.velocity import Velocity
from components.velocity_decay import VelocityDecay
from components.control import Control
from components.camera import CameraComponent
from components.scene_component import SceneComponent
from components.animation_component import AnimationComponent
from managers.animation_manager import AnimationManager
from managers.camera_manager import CameraManager
from managers.map_editor_manager import MapEditorManager
from managers.control import Controller
from managers.movement_manager import MovementManager
from managers.scene_manager import SceneManager
from utils.world import World
from constants import *


if __name__ == "__main__":
    # initialise pygame
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    god = Entity(
        Position(0, 0, 1),
        Velocity(),
        Control(),
        VelocityDecay(decay=0.5)
    )

    animation_manager = AnimationManager(clock)

    world = World(seed=123)

    scene = Entity()
    scene.add_component(
        SceneComponent(
            SCENE_SIZE
        )
    )

    scene_manager = SceneManager(scene, world)
    scene_manager.initialise_scene(god)

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

    editor = MapEditorManager(camera, world, scene)

    camera_manager = CameraManager(camera, scene, god, world)

    control_manager = Controller(god)

    movement_manager = MovementManager()
    movement_manager.add_entity(god)

    # main game loop
    running = True
    while running:
        control_manager.update()
        animation_manager.update()
        movement_manager.update()
        scene_manager.update()
        editor.update()

        if pygame.event.get(pygame.QUIT):
            running = False

        screen.blit(camera_manager.update(), (0, 0))
        pygame.display.flip()

        pygame.event.pump()

    pygame.quit()
