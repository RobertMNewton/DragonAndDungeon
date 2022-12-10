import pygame
import json
from utils.terrain import Terrain
from .manager import Manager
from constants import *
from math import floor


class MapEditorManager(Manager):
    def __init__(self, camera_entity, world, scene_entity):
        super(MapEditorManager, self).__init__()

        self.camera = camera_entity.get_component("camera")
        self.world = world
        self.scene = scene_entity.get_component("scene")

        self.terrain_index = 0
        self.terrains = list(Terrain.terrain_tiles_dict.keys())

    def update(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            x, y = pygame.mouse.get_pos()
            cam_x, cam_y = self.camera.get_position()

            x = x / SCREEN_WIDTH * VIEW_WIDTH + cam_x
            y = y / SCREEN_HEIGHT * VIEW_HEIGHT + cam_y

            print(self.world.map_data["0"][str(int(x // 16))][str(int(y // 16))])

            self.world.map_data["0"][str(int(x // 16))][str(int(y // 16))] = self.terrains[self.terrain_index]
            self.scene.change_position(0, int(x // 16), int(y // 16), self.world.get_spot_data((int(x // 16) * 16, int(y // 16) * 16)))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.terrain_index += 1
        elif keys[pygame.K_q]:
            self.terrain_index -= 1

        if self.terrain_index == -1:
            self.terrain_index = len(self.terrains) - 1
        elif self.terrain_index == len(self.terrains):
            self.terrain_index = 0