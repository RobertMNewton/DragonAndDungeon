from .manager import Manager


class CollisionManager(Manager):
    def __init__(self):
        super(CollisionManager, self).__init__()

        self.entities = []

    def update(self):
        for i in range(len(self.entities)):
            xi, yi, zi = self.entities[i].get_position(include_z=True)
            oxi, oyi, ozi = self.entities[i].get_component("collision box").get_offset()
            wi, li, hi = self.entities[i].get_component("collision box").get_bbox()
            for j in range(i, len(self.entities) - 1):
                xj, yj, zj = self.entities[j].get_position(include_z=True)
                oxj, oyj, ozj = self.entities[j].get_component("collision box").get_offset()
                wj, lj, hj = self.entities[j].get_component("collision box").get_bbox()

                # left side of i and right side of j
                if xj + oxj > xi + oxi > xj + oxj + wj:
                    print("LEFT COLLISION")
                # right side of i and left side of j
                elif xj + oxj + wj > xi + oxi + wj > xj + oxj:
                    print("RIGHT COLLISION")
                # top side of i and bottom side of j
                elif yi + oyi > yj + oyj + lj:
                    print("TOP COLLISION")
                # bottom side of i and top side of j
                elif yi + oyi + hi < yj + oyj:
                    print("BOTTOM SIDE")

    def add_entity(self, entity):
        if entity.has_component("collision box"):
            self.entities.append(entity)

    def add_entities(self, entities):
        for entity in entities:
            self.add_entity(entity)
