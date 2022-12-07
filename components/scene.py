from .component import Component


class SceneComponent(Component):
    def __init__(self, size):
        super(SceneComponent, self).__init__()

        self.name = 'scene'

        self.size = size

        self.data = []
        self.render_order = {"back": [], "front": []}
        self.render_order_keys = []
        self.offset = [0, 0]

    def get_render_order(self, depth_key):
        return self.render_order.get(depth_key, [])

    def get_front(self):
        return self.get_render_order("front")

    def get_back(self):
        return self.get_render_order("back")

    def get_depth_keys(self):
        keys = self.render_order_keys
