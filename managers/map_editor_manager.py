import pygame
import json
from utils.terrain import Terrain
from .manager import Manager
from constants import *
from math import floor


class MapEditorManager(Manager):
    def __init__(self, camera_entity):
        super(MapEditorManager, self).__init__()

        self.camera = camera_entity.get_component("camera")

    def update(self):
        pygame.event.get()

        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            x, y = pygame.mouse.get_pos()
            cam_x, cam_y = self.camera.get_position()

            x = x / SCREEN_WIDTH * VIEW_WIDTH + cam_x
            y = y / SCREEN_HEIGHT * VIEW_HEIGHT + cam_y

            map = json.load(open("assets/dev_map/map.json", 'r'))

            map["0"][str(floor(x / 16))][str(floor(y / 16))] = "grass_path_1"

            json.dump(map, open("assets/dev_map/map.json", 'w'))
