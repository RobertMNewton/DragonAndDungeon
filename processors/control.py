import pygame
from .processor import Processor
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT


class Controller(Processor):
    def __init__(self, entity):
        super(Controller, self).__init__()

        self.entity = entity

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.entity.get_component("velocity").y += 1
                elif event.key == K_DOWN:
                    self.entity.get_component("velocity").y -= 1
                elif event.key == K_RIGHT:
                    self.entity.get_component("velocity").x += 1
                elif event.key == K_LEFT:
                    self.entity.get_component("velocity").x -= 1
            elif event.type == QUIT:
                pygame.quit()
