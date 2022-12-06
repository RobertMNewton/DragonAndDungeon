class Entity:
    new_id = 0
    def __init__(self, *components):
        self._id = Entity.new_id
        Entity.new_id += 1

        self.components = {component.get_name(): component for component in components}

    def get_id(self):
        """Return unique id of this entity"""
        return self._id

    def has_component(self, name):
        """Return true if this entity has component with given name"""
        return name in self.components.keys()

    def get_component(self, name):
        """Return component of given name"""
        return self.components.get(name, default=None)

    def get_components(self):
        """Returns dictionary of this entity's components"""
        return self.components

    def add_component(self, component):
        """Add new component to this entity, returns True"""
        if not self.has_component(component.get_name()):
            self.components.update(component.get_name(), component)

    def remove_component(self, name):
        """Remove component of given name from entity"""
        if self.has_component(name):
            self.components.pop(name)
