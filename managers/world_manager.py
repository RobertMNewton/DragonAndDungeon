from .manager import Manager


class WorldManager(Manager):
    def __init__(self):
        super(WorldManager, self).__init__()

        self.positions = []

    def update(self):
        for i in range(len(self.ids)):
            pass

    def add_entity(self, entity):
        if entity.has_tag("tile"):
            self.ids.append(entity.get_id())
            self.positions.append(entity.get_component("position"))

    def add_entities(self, entities):
        for entity in entities:
            self.add_entity(entity)

    def remove_entity(self, entity):
        if entity.get_id() in self.ids:
            index = self.ids.index(entity.get_id())
            self.ids.pop(index)
            self.positions(index)

    def remove_entities(self, entities):
        for entity in entities:
            self.remove_entity(entity)
