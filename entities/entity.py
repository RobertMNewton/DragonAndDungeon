class Entity:
    new_id = 0
    def __init__(self, *components):
        self._id = Entity.new_id
        Entity.new_id += 1

        self.components = {component.get_name(): component for component in components}

        self.tags = []

    def get_id(self):
        """
        :return: Entity's Unique ID
        """
        return self._id

    def has_component(self, name):
        """
        :param name: string
        :return: Whether entity has component matching name parameter
        """
        return name in self.components.keys()

    def get_component(self, name):
        """
        :param name: string
        :return: Entity component matching name parameter
        """
        return self.components.get(name, None)

    def get_components(self):
        """
        :return: Dictionary of entity's components
        """
        return self.components

    def add_component(self, component):
        """
        :param component: Component to add
        :return: None
        """
        if not self.has_component(component.get_name()):
            self.components[component.get_name()] = component

    def remove_component(self, name):
        """
        :param name: string of name of component to remove
        :return: None
        """
        if self.has_component(name):
            self.components.pop(name)

    def get_tags(self):
        return self.tags

    def has_tag(self, name):
        return name in self.tags

    def add_tag(self, name):
        self.tags.append(name)

    def remove_tag(self, name):
        self.tags.remove(name)

    def get_position(self, default=(0, 0, 0)):
        if self.has_component('position'):
            return self.get_component('position').x, self.get_component('position').y
        return default

    def get_sprite(self, default=None):
        if self.has_component('sprite'):
            return self.get_component('sprite').surf
        return default

    def __repr__(self):
        return str(self._id)
