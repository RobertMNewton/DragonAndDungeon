from .manager import Manager


class SceneManager(Manager):
    def __init__(self, scene, world):
        super(SceneManager, self).__init__()

        self.scene = scene.get_component("scene")
        self.world = world

    def initialise_scene(self):
        self.scene.set_data(self.world.get_location_data((-16, -16), (16, 16)))