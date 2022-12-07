import pygame
from .component import Component


class AnimationComponent(Component):
    def __init__(self):
        super(AnimationComponent, self).__init__()

        self.name = 'animation'

        self.animations = {}

        self.frame = 0
        self.key = None

    def add_animation_from_paths(self, key, paths):
        self.animations[key] = []
        for path in paths:
            self.animations[key].append(pygame.image.load(path).convert())
            self.animations[key][-1].set_colorkey((255, 255, 255))

        self.key = key

    def next_frame(self):
        self.frame += 1
        if self.frame == len(self.animations[self.key]):
            self.frame = 0

        return self.animations[self.key][self.frame]

    def set_animation(self, key):
        if key != self.key:
            self.key = key
            self.frame = -1
