import pygame
from .component import Component


class Sprite(Component):
    def __init__(self, path_to_texture, trans_c=None):
        super(Sprite, self).__init__()

        self.name = "sprite"

        self.surf = pygame.image.load(path_to_texture).convert()
        if trans_c:
            self.surf.set_colorkey(trans_c)
