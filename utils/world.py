import random
from .terrain import Terrain
from math import ceil, floor
from entities.entity import Entity
from components.position import Position
from math import cos, sin


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

        random.seed(self.seed + cos(x) + sin(y) + x + y)

        roll = random.randint(0, len(Terrain.terrain_tiles) - 1)

        return self.create_tile(x, y, Terrain.terrain_tiles[roll])


    def create_tile(self, x, y, sprite):
        tile = Entity()

        tile.add_tag("tile")

        tile.add_component(Position(x, y))
        tile.add_component(sprite)

        return tile


