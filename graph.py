'''graph.py'''


class Node(object):
    '''a node'''

    def __init__(self, value, identifier):
        self.__value = value
        self.__identifier = identifier

    @property
    def value(self):
        '''get value'''
        return self.__value

    @property
    def identifier(self):
        '''id'''
        return self.__identifier

    def print_info(self):
        '''get info'''
        print "ID:", self.__identifier, "Value:", self.__value


class Graph(object):
    '''the graph'''

    def __init__(self, dims):
        cols = dims[0]
        rows = dims[1]
        self._nodes = {}
        for i in range(0, cols):
            for j in range(0, rows):
                nodekey = str(i) + ',' + str(j)
                self._nodes[nodekey] = Node([i, j], len(self._nodes))

    def get_node(self, node):
        '''get a node by list [1,1]'''
        nodekey = str(node[0]) + ',' + str(node[1])
        if nodekey in self._nodes:
            return self._nodes[nodekey]
            