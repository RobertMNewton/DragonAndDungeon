import pygame
from .processor import Processor
from pygame.locals import K_w, K_a, K_s, K_d, KEYDOWN, QUIT


class Controller(Processor):
    def __init__(self, entity):
        super(Controller, self).__init__()

        self.entity = entity

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_s:
                    self.entity.get_component("velocity").y += 1
                elif event.key == K_w:
                    self.entity.get_component("velocity").y -= 1
                elif event.key == K_d:
                    self.entity.get_component("velocity").x += 1
                elif event.key == K_a:
                    self.entity.get_component("velocity").x -= 1
            elif event.type == QUIT:
                pygame.quit()
