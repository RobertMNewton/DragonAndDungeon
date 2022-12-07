import pygame
from .manager import Manager


class CameraManager(Manager):
    def __init__(self, camera_entity, scene_entity, follow_entity):
        super(CameraManager, self).__init__()

        self.camera = camera_entity.get_component('camera')
        self.scene = scene_entity.get_component('scene')
        self.follow_position = follow_entity.get_component('position')

        self.surface = pygame.surface.Surface(self.camera.view_size)

    def change_entity(self, entity):
        self.camera = entity.get_component('camera')

    def change_scene(self, scene):
        self.scene = scene.get_component('scene')

    def update(self, clear=True):
        self.camera.x = self.follow_position.x
        self.camera.y = self.follow_position.y
        self.camera.z = self.follow_position.z

        if clear:
            self.surface.fill((0, 0, 0))

        cam_x, cam_y = self.camera.get_position()

        for depth_key in self.scene.get_depth_keys():
            for i in self.scene.get_render_order(depth_key):
                entity_x, entity_y = self.scene.data[i].get_position()

                offset_x, offset_y = self.scene.data[i].get_component('sprite').offset

                entity_x -= offset_x
                entity_y -= offset_y

                render_x = entity_x - cam_x
                render_y = entity_y - cam_y

                self.surface.blit(self.scene.data[i].get_sprite(), (render_x, render_y))

            if depth_key > self.camera.get_position(include_z=True)[-1]:
                break

        for i in self.scene.get_front():
            entity_x, entity_y = self.scene.data[i].get_position()

            render_x = cam_x - entity_x
            render_y = cam_y - entity_y

            self.surface.blit(self.scene.data[i].get_sprite(), (render_x, render_y))

        return pygame.transform.scale(self.surface, self.camera.window_size)

    def get_surface(self):
        return pygame.transform.scale(self.surface, self.camera.window_size)
