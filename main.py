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

    player = Entity(
        Sprite("assets/dude/right_0.png", trans_c=(255, 255, 255), offset=(8, 8)),
        Position(0, 0, 1),
        Velocity(),
        Control(),
        VelocityDecay(decay=0.5)
    )
    player.add_tag("player")

    player_animation = AnimationComponent()
    player_animation.add_animation_from_paths(
        "walk down",
        [
            "assets/dude/backwards_0.png",
            "assets/dude/backwards_1.png",
            "assets/dude/backwards_2.png"
        ]
    )
    player_animation.add_animation_from_paths(
        "walk up",
        [
            "assets/dude/forward_0.png",
            "assets/dude/forward_1.png",
            "assets/dude/forward_2.png"
        ]
    )
    player_animation.add_animation_from_paths(
        "walk left",
        [
            "assets/dude/left_0.png",
            "assets/dude/left_1.png",
            "assets/dude/left_2.png"
        ]
    )
    player_animation.add_animation_from_paths(
        "walk right",
        [
            "assets/dude/right_0.png",
            "assets/dude/right_1.png",
            "assets/dude/right_2.png"
        ]
    )

    player.add_component(player_animation)

    animation_manager = AnimationManager(clock)
    animation_manager.add_entity(player)

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

    camera_manager = CameraManager(camera, scene, player, world)

    control_manager = Controller(player)

    movement_manager = MovementManager()
    movement_manager.add_entity(player)

    # main game loop
    running = True
    while running:
        control_manager.update()
        movement_manager.update()
        animation_manager.update()
        scene_manager.update()

        if pygame.event.get(pygame.QUIT):
            running = False

        screen.blit(camera_manager.update(), (0, 0))
        pygame.display.flip()

        pygame.event.pump()

    pygame.quit()
