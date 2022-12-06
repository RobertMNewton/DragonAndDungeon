from .component import Component


class VelocityDecay(Component):
    def __init__(self, decay=1):
        super(VelocityDecay, self).__init__()

        self.name = "velocity_decay"
        self.decay = decay