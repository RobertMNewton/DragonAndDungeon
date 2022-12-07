import pygame
from .manager import Manager


class CameraManager(Manager):
    def __init__(self, entity, scene):
        super(CameraManager, self).__init__()

        self.camera = entity.get_component('camera')
        self.scene = scene.get_component('scene')

        self.surface = pygame.surface.Surface(self.camera.view_size)

    def change_entity(self, entity):
        self.camera = entity.get_component('camera')

    def change_scene(self, scene):
        self.scene = scene.get_component('scene')

    def update(self):
        cam_x, cam_y = self.camera.get_position()

        for i in self.scene.get_back():
            entity_x, entity_y = self.scene.data[i].get_position()

            render_x = entity_x - cam_x
            render_y = entity_y - cam_y

            self.surface.blit(self.scene.data[i].get_sprite(), (render_x, render_y))

        for depth_key in self.scene.get_depth_keys:
            for i in self.scene.get_render_order(depth_key):
                entity_x, entity_y = self.scene.data[i].get_position()

                render_x = entity_x - cam_x
                render_y = entity_y - cam_y

                self.surface.blit(self.scene.data[i].get_sprite(), (render_x, render_y))

        for i in self.scene.get_front():
            entity_x, entity_y = self.scene.data[i].get_position()

            render_x = entity_x - cam_x
            render_y = entity_y - cam_y

            self.surface.blit(self.scene.data[i].get_sprite(), (render_x, render_y))

        return pygame.transform.scale(self.surface, self.camera.window_size)