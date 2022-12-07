import pygame
from .manager import Manager


class CameraManager(Manager):
    def __init__(self, entity, scene):
        super(CameraManager, self).__init__()

        self.camera = entity.get_component('camera')
        self.scene = scene.get_component('scene')

        self.surface = pygame.surface.Surface(self.camera.game_size)

    def change_entity(self, entity):
        self.camera = entity.get_component('camera')

    def change_scene(self, scene):
        self.scene = scene.get_component('scene')

    def update(self):
        pass