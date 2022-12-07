import pygame
from .component import Component


class AnimationComponent(Component):
    def __init__(self):
        super(AnimationComponent, self).__init__()

        self.name = 'animation'

        self.animations = {}

        self.frame_time = 12
        self.frame = 0

        self.frozen = True

        self.sprite_frame = 0

        self.key = None

    def add_animation_from_paths(self, key, paths):
        self.animations[key] = []
        for path in paths:
            self.animations[key].append(pygame.image.load(path).convert())
            self.animations[key][-1].set_colorkey((255, 255, 255))

        self.key = key

    def next_frame(self):
        if not self.frozen:
            self.frame += 1
            if not self.frame % self.frame_time:
                self.sprite_frame += 1
            if self.sprite_frame == len(self.animations[self.key]):
                self.sprite_frame = 0

        return self.animations[self.key][self.sprite_frame]

    def set_animation(self, key):
        if key != self.key:
            self.key = key
            self.frame = 0
            self.sprite_frame = 0

    def freeze(self, frame=None):
        self.frozen = True
        if frame:
            self.sprite_frame = frame
        else:
            self.sprite_frame = 0

    def unfreeze(self, frame=None):
        self.frozen = False
        if frame:
            self.sprite_frame = frame
        else:
            self.sprite_frame = self.sprite_frame
