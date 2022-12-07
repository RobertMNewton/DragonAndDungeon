import pygame
from .manager import Manager
from pygame.locals import K_w, K_a, K_s, K_d
from constants import *


class Controller(Manager):
    def __init__(self, entity):
        super(Controller, self).__init__()

        self.entity = entity

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.entity.get_component("velocity").y -= PLAYER_SPEED
            self.entity.get_component("animation").set_animation("walk up")
        if keys[K_s]:
            self.entity.get_component("velocity").y += PLAYER_SPEED
            self.entity.get_component("animation").set_animation("walk down")
        if keys[K_d]:
            self.entity.get_component("velocity").x += PLAYER_SPEED
            self.entity.get_component("animation").set_animation("walk right")
        if keys[K_a]:
            self.entity.get_component("velocity").x -= PLAYER_SPEED
            self.entity.get_component("animation").set_animation("walk left")
