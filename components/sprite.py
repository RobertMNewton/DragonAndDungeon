import pygame
from .component import Component


class Sprite(Component):
    def __init__(self, path_to_texture, trans_c=None, size=None, offset=(0, 0)):
        super(Sprite, self).__init__()

        self.name = "sprite"

        self.surf = pygame.image.load(path_to_texture)
        self.offset = offset

        if trans_c:
            self.surf.set_colorkey(trans_c)
        if size:
            self.surf = pygame.transform.scale(self.surf, size)
