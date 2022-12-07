from random import random
from math import ceil, floor
from entities.entity import Entity
from components.position import Position
from components.sprite import Sprite


class World:
    def __init__(self, seed=None):
        if not seed:
            self.seed = int(random() * 10E15)
        else:
            self.seed = seed

    def get_location_data(self, pos1, pos2):
        data = []
        for iy in range(ceil(pos2[1]) - floor(pos1[1])):
            absolute_y = pos2[0] + (16 * iy)
            for ix in range(ceil(pos2[0]) - floor(pos1[0])):
                absolute_x = pos1[0] + (16 * ix)
                data.append(self.create_tile(absolute_x, absolute_y, "assets/grassland_textures/grass_grassy.png"))
        return data

    def create_tile(self, x, y, texture):
            tile = Entity()

            tile.add_tag("tile")

            tile.add_component(Position(x, y))
            tile.add_component(Sprite(texture, trans_c=(255, 255, 255)))

            return tile
