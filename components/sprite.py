import pygame
from .component import Component


class Sprite(Component):
    def __init__(self, path_to_texture, trans_c=None, size=None, offset=None):
        super(Sprite, self).__init__()

        self.name = "sprite"

        self.surf = pygame.image.load(path_to_texture)

        if not size:
            self.size = self.surf.get_size()
        else:
            self.size = size

        if not offset:
            self.offset = (self.size[0] / 2, self.size[1] / 2)
        else:
            self.offset = offset

        if size:
            self.surf = pygame.transform.scale(self.surf, size)

        if trans_c:
            self.surf.set_colorkey(trans_c)
