from .manager import Manager
from constants import *


class SceneManager(Manager):
    def __init__(self, scene, world):
        super(SceneManager, self).__init__()

        self.scene = scene.get_component("scene")
        self.world = world

    def update(self):
        pass

    def initialise_scene(self, player):
        self.scene.set_scene_data(self.world.get_location_data((-16 * 20, -16 * 20), (16 * 20, 16 * 20)))
        self.scene.add_entity(player)

