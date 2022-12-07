import random
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
        for iy in range((ceil(pos2[1]) - floor(pos1[1])) // 16):
            absolute_y = pos1[1] + (16 * iy)
            for ix in range((ceil(pos2[0]) - floor(pos1[0])) // 16):
                absolute_x = pos1[0] + (16 * ix)
                data.append(self.get_spot_data((absolute_x, absolute_y)))
        return data

    def get_spot_data(self, pos):
        x, y = pos

        random.seed(self.seed * x + y)
        roll = random.random()
        if roll < 0.75:
            return self.create_tile(x, y, "assets/grassland_textures/grass_grassy.png")
        elif roll < 0.85:
            return self.create_tile(x, y, "assets/grassland_textures/grass_rock_small.png")
        elif roll < 0.95:
            return self.create_tile(x, y, "assets/grassland_textures/grass_rock_cluster_2.png")
        else:
            return self.create_tile(x, y, "assets/grassland_textures/grass_rock_cluster_1.png")

    def create_tile(self, x, y, texture):
        tile = Entity()

        tile.add_tag("tile")

        tile.add_component(Position(x, y))
        tile.add_component(Sprite(texture, trans_c=(255, 255, 255)))

        return tile


