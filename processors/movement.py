from .processor import Processor


class MovementProcessor(Processor):
    def __init__(self):
        super(MovementProcessor, self).__init__()

        self.positions = []
        self.velocities = []

    def update(self):
        for i in range(len(self.ids)):
            self.positions[i].x += self.velocities[i].x
            self.positions[i].y += self.velocities[i].y

    def add_entity(self, entity):
        if entity.has_component("velocity") and entity.has_component("position"):
            self.ids.append(entity.get_id())
            self.positions.append(entity.get_component("position"))
            self.velocities.append(entity.get_component("velocity"))

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
