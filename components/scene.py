from .component import Component


class SceneComponent(Component):
    def __init__(self, size):
        super(SceneComponent, self).__init__()

        self.name = 'scene'

        self.size = size

        self.data = []
        self.render_order = {""front": []}
        self.render_order_keys = []
        self.offset = [0, 0]

    def get_render_order(self, depth_key):
        return self.render_order.get(depth_key, [])

    def get_front(self):
        return self.get_render_order("front")

    def get_depth_keys(self):
        keys = self.render_order_keys

    def set_scene_data(self, data):
        self.data = data

    def add_entity(self, entity):
        self.data.append(entity)
        z = int(entity.get_component("position").z)
        if z in self.render_order.keys():
            self.render_order[z].append(len(self.data) - 1)
        else:
            self.render_order[z] = [len(self.data) - 1]

    def remove_entity(self, entity):
        z = int(entity.get_component("position").z)
        if z in self.render_order_keys:
            key = z
        else:
            if
