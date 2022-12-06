import pygame
from .component import Component


class Sprite(Component):
    def __init__(self, path_to_texture):
        super(Sprite, self).__init__()

        self.name = "sprite"

        self.surf = pygame.image.load(path_to_texture).convert()
        self.rect = self.surf.get_rect()
