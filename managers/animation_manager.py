from .manager import Manager


class AnimationManager(Manager):
    def __init__(self):
        super(AnimationManager, self).__init__()

        self.animations = []
        self.sprites = []

    def update(self):
        for i in range(len(self.animations)):
            self.sprites[i].surf = self.animations[i].next_frame()

    def add_entity(self, entity):
        self.animations.append(entity.get_component("animation"))
        self.sprites.append(entity.get_component("sprite"))
