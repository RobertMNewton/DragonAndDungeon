from .component import Component


class CollisionBox(Component):
    def __init__(self, bbox: tuple[int, int, int], offset: tuple[int, int, int] = (0, 0, 0)):
        super(CollisionBox, self).__init__()

        self.name = "collision box"

        # tuple format x y z
        self.bbox = bbox
        self.offset = offset

        self.collisions = []

    def get_width(self):
        return self.bbox[0]

    def get_length(self):
        return self.bbox[1]

    def get_height(self):
        return self.bbox[2]

    def get_bbox(self):
        return self.bbox

    def get_offset(self):
        return self.offset

    def add_collision(self, entity):
        self.collisions.append(entity)

    def reset_collisions(self):
        self.collisions = []
