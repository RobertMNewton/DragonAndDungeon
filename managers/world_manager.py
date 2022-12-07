import random
from .manager import Manager
from entities.entity import Entity
from components.position import Position
from components.sprite import Sprite


class WorldManager(Manager):
    def __init__(self, player, size=None, seed=None):
        super(WorldManager, self).__init__()

        self.player = player
        self.positions = []

        self.tiles = []

        self.tx = 32
        self.ty = 22

        self.size = size

        if not seed:
            self.seed = int(random.random() * 10E15)
        else:
            self.seed = seed

    def update(self):
        added_tiles = []
        removed_tiles = []

        tx = self.tx // 2 * 16
        ty = self.ty // 2 * 16

        x, y = self.player.get_component("position").get()
        x -= tx
        y -= ty

        noise = self.get_noise((x - tx, y - ty), (x + tx, y + ty))

        for iy in range(self.ty):
            for ix in range(self.tx):
                new_x = ix * self.size[0] + (x % (self.tx * 16 / 3)) - (16 * 2 * 3)
                new_y = iy * self.size[1] + (y % (self.ty * 16 / 3)) - (16 * 2 * 3)

                self.tiles[iy][ix].get_component("position").x = new_x
                self.tiles[iy][ix].get_component("position").y = new_y

        return added_tiles, removed_tiles

    def add_entity(self, entity):
        if entity.has_tag("tile"):
            self.ids.append(entity.get_id())
            self.positions.append(entity.get_component("position"))

    def add_entities(self, entities):
        for entity in entities:
            self.add_entity(entity)

    def remove_entity(self, entity):
        if entity.get_id() in self.ids:
            index = self.ids.index(entity.get_id())
            self.ids.pop(index)
            self.positions.pop(index)

    def remove_entities(self, entities):
        for entity in entities:
            self.remove_entity(entity)

    def create_tile(self, x, y, texture):
        tile = Entity()

        tile.add_tag("tile")

        tile.add_component(Position(x, y))
        tile.add_component(Sprite(texture, trans_c=(255, 255, 255), size=self.size))

        return tile

    def generate_initial_tiles(self):
        added_tiles = []
        x, y = self.player.get_component("position").get()

        tx = self.tx * 16
        ty = self.ty * 16

        noise = self.get_noise((x - (tx // 2), y - (ty // 2)), (x + (tx // 2), y + (ty // 2)))

        for iy in range(self.ty):
            for ix in range(self.tx):
                texture = "assets/grassland_textures/grass_grassy.png"
                tile = self.create_tile(x + (ix * 16), y + (iy * 16), texture)

                added_tiles.append(tile)
                self.tiles.append(tile)

        return added_tiles

    def get_tiles(self):
        return self.tiles

    @staticmethod
    def get_noise(pos1, pos2):
        return [[1 for _1 in range(int(pos2[0] - pos1[0]))] for _2 in range(int(pos2[1] - pos2[1]))]

