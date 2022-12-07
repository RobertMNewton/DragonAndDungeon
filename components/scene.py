from .component import Component


class SceneComponent(Component):
    def __init__(self, size):
        super(SceneComponent, self).__init__()

        self.name = 'scene'

        self.size = size

        self.data = []
        self.render_order = {"front": []}
        self.render_order_keys = []

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
            self.insert_depth_key()

    def remove_entity(self, entity):
        z = int(entity.get_component("position").z)
        if z in self.render_order_keys:
            key = z
        else:
            key = "front"
        for i in range(len(self.render_order[key])):
            if self.data[self.render_order[key]].get_id() == entity.get_id():
                self.data.pop(self.render_order[key])
                self.render_order[key].pop(i)
                if len(self.render_order[key]) == 0 and key != "front":
                    self.render_order.pop(key)
                    self.render_order_keys.remove(key)

    def insert_depth_key(self, depth_key):
        if len(self.render_order_keys) >= 1:
            a = 0
            b = len(self.render_order_keys) - 1
            while a < b:
                i = (a + b) // 2
                if self.render_order_keys[i] > depth_key:
                    b = i
                else:
                    a = i
            self.render_order_keys.insert(a, depth_key)
        else:
            self.render_order_keys.append(depth_key)
