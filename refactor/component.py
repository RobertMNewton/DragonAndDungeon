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
