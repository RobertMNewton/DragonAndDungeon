from .manager import Manager


class AnimationManager(Manager):
    def __init__(self, clock):
        super(AnimationManager, self).__init__()

        self.animations = []
        self.sprites = []

        self.clock = clock

    def update(self):
        dt = self.clock.tick()
        for i in range(len(self.animations)):
            self.sprites[i].surf = self.animations[i].next_frame(dt)

    def add_entity(self, entity):
        self.animations.append(entity.get_component("animation"))
        self.sprites.append(entity.get_component("sprite"))
