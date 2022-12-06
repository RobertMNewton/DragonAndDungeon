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

        self.size = size

        if not seed:
            seed = random.random() * 10

    def update(self):
        for i in range(len(self.ids)):
            pass

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
            self.positions(index)

    def remove_entities(self, entities):
        for entity in entities:
            self.remove_entity(entity)

    def create_tile(self, x, y, texture):
        tile = Entity()

        tile.add_tag("tile")

        tile.add_component(Position(x, y))
        tile.add_component(Sprite(texture, trans_c=(255, 255, 255), size=self.size))