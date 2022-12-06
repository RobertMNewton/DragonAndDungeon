import pygame
from .manager import Manager
from components.position import Position


class Renderer(Manager):
    def __init__(self, screen):
        super(Renderer, self).__init__()

        self.screen = screen

        self.sprites = []
        self.positions = []

        self.render_order = []

    def update(self):
        """
        Render all sprites to screen surface
        :return:
        """
        for i in self.render_order:
            self.screen.blit(self.sprites[i].surf, self.positions[i].get())

    def set_display(self, screen):
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

            if not entity.has_tag("player"):
                self.positions.append(entity.get_component("position"))
            else:
                self.positions.append(Position(420 * 3 // 2, 320 * 3 // 2, 1))

            if len(self.render_order) > 0:
                a = 0
                b = len(self.render_order) - 1
                z = self.positions[-1].z
                while a < b:
                    z_mid = self.positions[self.render_order[(a + b) // 2]].z
                    if z < z_mid:
                        b = b // 2
                    elif z > z_mid:
                        a = b // 2
                    else:
                        a = (a + b) // 2
                        b = a
                self.render_order.insert(a, len(self.render_order) - 1)
            else:
                self.render_order.append(0)

    def recalculate_render_order(self):
        pass

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

            for i in range(index + 1, len(self.render_order)):
                self.render_order[i] -= 1

            self.render_order.pop(index)

    def remove_entities(self, entities):
        for entity in entities:
            self.remove_entity(entity)

