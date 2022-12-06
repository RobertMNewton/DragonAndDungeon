import pygame
from .processor import Processor
from pygame.locals import K_w, K_a, K_s, K_d, KEYDOWN, QUIT


class Controller(Processor):
    def __init__(self, entity):
        super(Controller, self).__init__()

        self.entity = entity

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.entity.get_component("velocity").y -= 1
        if keys[K_s]:
            self.entity.get_component("velocity").y += 1
        if keys[K_d]:
            self.entity.get_component("velocity").x += 1
        if keys[K_a]:
            self.entity.get_component("velocity").x -= 1
