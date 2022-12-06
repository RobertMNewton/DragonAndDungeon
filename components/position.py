from component import Component
class Position(Component):
    def __init__(self, start_x=0, start_y=0):
        super(Position, self).__init__()

        self.name = "position"

        self.x = start_x
        self.y = start_y
