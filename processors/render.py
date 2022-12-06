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
        for i in range(self.num):
            self.screen.blit(self.sprites[i].surf, self.sprites[i].rect)
