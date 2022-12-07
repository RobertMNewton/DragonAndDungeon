from .component import Component


class CameraComponent(Component):
    def __init__(self, x, y, z, window_size, view_size):
        super(CameraComponent, self).__init__()

        self.name = 'camera'

        self.x = x
        self.y = y
        self.z = z

        self.window_size = window_size
        self.view_size = view_size

    def get_position(self, include_z=False):
        if not include_z:
            return self.x, self.y
        else:
            return self.x, self.y, self.z
