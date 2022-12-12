import pygame
from math import sqrt


class Component:
    """
    Component Base Class for storing component data
    """
    data = {}

    @classmethod
    def add_data(cls, eid: int, data: object) -> None:
        """
        Add data to class
        :param eid: Unique entity id to be used as key
        :param data: Position component to store the data
        :return:
        """
        cls.data[eid] = data

    @classmethod
    def pop_data(cls, eid: int) -> None:
        """
        Removes data from class
        :param eid: Unique entity id to be used as key
        :return: Popped Position Component
        """
        return cls.data.pop(eid)

    @classmethod
    def get_data(cls, eid: int) -> object:
        """
        Gets data from class
        :param eid: Unique entity id to be used as key
        :return: Corresponding component
        """
        return cls.data[eid]


class Vector(Component):
    """
    Component for storing Vector data
    """
    def __init__(self, x: float, y: float) -> None:
        super(Vector, self).__init__()

        self.x = x
        self.y = y

    def set(self, x: float = None, y: float = None) -> None:
        """
        Sets the x and y values of vector
        :param x: new x value
        :param y: new y value
        :return:
        """
        if x:
            self.x = x
        if y:
            self.y = y

    def __repr__(self):
        return f"{self.__class__}({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.x + other.x, self.y + other.y)
        else:
            return self.__class__(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.x - other.x, self.y - other.y)
        else:
            return self.__class__(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return self.__class__(self.x * other, self.y * other)

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)


class Position(Vector):
    """
    Component for storing position data
    """
    data = {}


class Box(Component):
    """
    Component for storing position data
    """
    def __init__(self, p1: Position, p2:  Position):
        super(Box, self).__init__()

        self.p1 = p1
        self.p2 = p2

    def get_width(self) -> float:
        if hasattr(self, "width"):
            return self.width
        else:
            setattr(self, "width", self.p2.x - self.p1.x)
            return self.get_width()

    def get_height(self) -> float:
        if hasattr(self, "height"):
            return self.height
        else:
            setattr(self, "height", self.p2.x - self.p1.x)
            return self.get_width()


class CollisionBox(Box):
    """
    Component for collision box data
    """
    data = {}


class Sprite(Component):
    """
    Component for Sprite image data
    """
    data = {}

    def __init__(self, surface: pygame.Surface = None):
        super(Sprite, self).__init__()

        if surface:
            self.surface = surface
        else:
            self.surface = pygame.Surface((0, 0))

    def set_surface(self, surface: pygame.Surface):
        """
        Sets the display surface of sprite
        :type surface: Pygame surface
        """
        self.surface = surface


class Animation(Component):
    """
    Component for storing animation data
    """
    data = {}

    def __init__(self) -> None:
        super(Animation, self).__init__()

        self.animations = {}
        self.current_animation = None

        self.current_frame = 0

        self.t = 0
        self.frozen = False

    def add_animation_from_path(self, info: dict) -> None:
        if info['name'] not in self.animations.keys():
            self.animations[info['name']] = {
                "frames": [pygame.image.load(path) for path in info['paths']],
                "times": info['times']
            }

    def set_animation(self, name: str, frame: int = None) -> None:
        try:
            self.current_animation = name
            if frame:
                self.current_frame = frame
        except:
            raise KeyError(f"Animation Object {self.__name__} does not have key {name}")

    def update_frame(self, dt: int) -> None:
        self.t += dt
        t = self.t % self.animations[self.current_animation]["times"][-1]
        for i in range(self.current_frame, len(self.animations[self.current_animation]["frames"]) - 1):
            t1 = self.animations[self.current_animation]["times"][i]
            t2 = self.animations[self.current_animation]["times"][i + 1]

            if t1 < t < t2:
                self.current_frame = i

                return
        self.current_frame = -1
