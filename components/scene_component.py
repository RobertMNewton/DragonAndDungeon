from .component import Component
from math import floor


class SceneComponent(Component):
    def __init__(self, size):
        super(SceneComponent, self).__init__()

        self.name = 'scene'

        self.size = size

        self.data = []
        self.render_order = {"front": []}
        self.render_order_keys = []

        self.coordinate_keys = {}

    def get_render_order(self, depth_key):
        return self.render_order.get(depth_key, [])

    def get_front(self):
        return self.get_render_order("front")

    def get_depth_keys(self):
        return self.render_order_keys

    def set_scene_data(self, data):
        for entity in data:
            self.add_entity(entity)

    def add_entity(self, entity, depth_key=None):
        self.data.append(entity)
        if not depth_key:
            z = int(entity.get_component("position").z)
            if z in self.render_order.keys():
                self.render_order[z].append(len(self.data) - 1)
            else:
                self.render_order[z] = [len(self.data) - 1]
                self.insert_depth_key(z)
        else:
            self.render_order[depth_key] = [len(self.data) - 1]
            if depth_key != 'front':
                self.insert_depth_key(depth_key)

        x, y = entity.get_position()
        x, y = int(x // 16), int(y // 16)

        if not z in self.coordinate_keys.keys():
            self.coordinate_keys[z] = {x: {y: len(self.data) - 1}}
        elif not x in self.coordinate_keys[z].keys():
            self.coordinate_keys[z][x] = {y: len(self.data) - 1}
        else:
            self.coordinate_keys[z][x][y] = len(self.data) - 1

    def remove_entity(self, entity):
        z = int(entity.get_component("position").z)
        if z in self.render_order_keys:
            key = z
        else:
            key = "front"
        # TODO change to two pointer algorithm
        for i in range(len(self.render_order[key])):
            if self.data[self.render_order[key]].get_id() == entity.get_id():
                self.data.pop(self.render_order[key])
                self.render_order[key].pop(i)
                if len(self.render_order[key]) == 0 and key != "front":
                    self.render_order.pop(key)
                    self.render_order_keys.remove(key)

        x, y = entity.get_position()
        x, y = floor(x), floor(y)

        self.coordinate_keys[z][x].pop(y)
        if len(self.coordinate_keys[z][x]) == 0:
            self.coordinate_keys[z].pop(x)
        if len(self.coordinate_keys[z]) == 0:
            self.coordinate_keys.pop(z)

    def insert_depth_key(self, depth_key):
        if len(self.render_order_keys) >= 1:
            for i in range(len(self.render_order_keys)):
                if i == len(self.render_order_keys) - 1:
                    continue
                elif self.render_order_keys[i] > depth_key and self.render_order_keys[i + 1] < depth_key:
                    continue
            self.render_order_keys.insert(i + 1, depth_key)
        else:
            self.render_order_keys.append(depth_key)

    def change_position(self, z, x, y, new_entity):
        index = self.coordinate_keys[z][x][y]
        self.data[index] = new_entity
