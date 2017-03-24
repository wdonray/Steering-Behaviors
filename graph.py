"""For Main Menu."""


class Node(object):
    """A node."""

    def __init__(self, value, identifier):
        """Initialize."""
        self.__value = value
        self.__identifier = identifier

    @property
    def value(self):
        """Get value."""
        return self.__value

    @property
    def identifier(self):
        """ID."""
        return self.__identifier

    def print_info(self):
        """Get info."""
        print "ID:", self.__identifier, "Value:", self.__value


class Graph(object):
    """The graph."""

    def __init__(self, dims):
        """Initialize."""
        cols = dims[0]
        rows = dims[1]
        self._nodes = {}
        for i in range(0, cols):
            for j in range(0, rows):
                nodekey = str(i) + ',' + str(j)
                self._nodes[nodekey] = Node([i, j], len(self._nodes))

    def get_node(self, node):
        """Get a node by list [1,1]."""
        nodekey = str(node[0]) + ',' + str(node[1])
        if nodekey in self._nodes:
            return self._nodes[nodekey]
            