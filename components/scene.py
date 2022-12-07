from .component import Component


class SceneComponent(Component):
    def __init__(self, size):
        super(SceneComponent, self).__init__()

        self.name = 'scene'

        self.size = size

        self.data = {"tile_data": [], "entity_data": []}
        self.offset = (0, 0)

