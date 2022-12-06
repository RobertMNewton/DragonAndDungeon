from .component import Component


class Velocity(Component):
    def __init__(self, start_x=0, start_y=0):
        super(Velocity, self).__init__()

        self.name = "velocity"

        self.x = start_x
        self.y = start_y
