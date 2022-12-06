from .component import Component


class Position(Component):
    def __init__(self, x=0, y=0, z=0):
        super(Position, self).__init__()

        self.name = "position"

        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return self.x, self.y
