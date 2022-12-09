from .manager import Manager


class MovementManager(Manager):
    def __init__(self):
        super(MovementManager, self).__init__()

        self.positions = []
        self.velocities = []
        self.decays = []

    def update(self):
        for i in range(len(self.ids)):
            decay = 1 if not self.decays[i] else self.decays[i].decay

            self.positions[i].x += self.velocities[i].x
            self.positions[i].y += self.velocities[i].y

            self.velocities[i].x *= decay
            self.velocities[i].y *= decay

            if self.velocities[i].x < 1:
                self.velocities[i].x = 0
            if self.velocities[i].y < 1:
                self.velocities[i].y = 0

    def add_entity(self, entity):
        if entity.has_component("velocity") and entity.has_component("position"):
            self.ids.append(entity.get_id())
            self.positions.append(entity.get_component("position"))
            self.velocities.append(entity.get_component("velocity"))
            self.decays.append(entity.get_component("velocity_decay"))

    def add_entities(self, entities):
        for entity in entities:
            self.add_entity(entity)

    def remove_entity(self, entity):
        if entity.get_id() in self.ids:
            index = self.ids.index(entity.get_id())
            self.ids.pop(index)
            self.positions(index)
            self.velocities(index)

    def remove_entities(self, entities):
        for entity in entities:
            self.remove_entity(entity)
