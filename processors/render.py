import pygame
from processor import Processor


class Renderer(Processor):
    def __init__(self, screen):
        super(Renderer, self).__init__()

        self.screen = screen

        self.sprites = []
        self.positions = []

        self.num = 0

    def update(self):
        """
        Render all sprites to screen surface
        :return:
        """
        for i in range(self.num):
            self.screen.blit(self.sprites[i].surf, self.positions[i])

    def set_screen(self, screen):
        """
        Set new screen surface
        :param screen:
        :return:
        """
        self.screen = screen

    def add_entity(self, entity):
        """
        Add components of given entity object
        """
        if entity.has_component("position") and entity.has_component("sprite"):
            self.ids.append(entity.get_id())
            self.sprites.append(entity.get_component("sprite"))
            self.positions.append(entity.get_component("position"))

    def add_entities(self, entities):
        """
        Add components from list of entities
        """
        for entity in entities:
            self.add_entity(entity)

    def remove_entity(self, entity):
        """
        Remove given entity from process lists
        :param entity:
        :return:
        """
        if entity.id in self.ids:
            index = self.ids.index(entity.id)

            self.ids.pop(index)
            self.positions.pop(index)
            self.sprites.pop(index)

