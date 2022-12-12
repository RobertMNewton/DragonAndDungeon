from component import *


class Entity:
    entities = {}
    next_id = 0

    def __init__(self, *components):
        self.id = Entity.next_id
        Entity.next_id += 1

        Entity.entities[self.id] = self

        self.add_components(*components)

    def __del__(self):
        Entity.entities.pop(self.id)

    def add_component(self, component: Component) -> None:
        setattr(self, component.__class__.__name__.lower(), component)
        component.add_data(self.id, component)

    def add_components(self, *components: list[Component]) -> None:
        for component in components:
            self.add_component(component)
