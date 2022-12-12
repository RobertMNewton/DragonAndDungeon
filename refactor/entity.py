from component import *
from typing import Optional


class Entity:
    entities = {}
    next_id = 0

    def __init__(self, *components):
        self.id = Entity.next_id
        Entity.next_id += 1

        Entity.entities[self.id] = self

        self.components = []
        self.add_components(*components)

    def __del__(self):
        for component in self.components:
            getattr(self, component).pop_data(self.id)
        Entity.entities.pop(self.id)

    def add_component(self, component: Component) -> None:
        setattr(self, component.__class__.__name__.lower(), component)
        component.add_data(self.id, component)

    def add_components(self, *components: list[Component]) -> None:
        for component in components:
            self.add_component(component)
            self.components.append(component.__class__.__name__.lower())

    def pop_component(self, component: Optional[str, Component]) -> None:
        getattr(self, str(component)).pop_data(self.id)
        delattr(self, str(component))

    def pop_components(self, components: list[Optional[str, Component]]):
        for component in components:
            self.pop_component(components)


class EntityGroup:
    """
    Class for holding groups of entities
    """
    def __init__(self, *entities):
        self.entities = []

        for entity in entities:
            self.entities.append(entity)

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_entities(self, *entities):
        for entity in entities:
            self.add_entity(entity)
