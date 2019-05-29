# Node class for the position in the grid
class Node(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        return self._x == other.x and self._y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return 'Node({}, {})'.format(self._x, self._y)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self._x, self._y))
