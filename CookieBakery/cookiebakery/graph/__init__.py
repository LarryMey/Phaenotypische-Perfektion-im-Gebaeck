from graph_tool.all import Graph as GT_Graph

class Graph:
    # there is only one graph, so implement as singleton
    class __Graph__:
        
        def __init__(self):
            self.graph = GT_Graph()

        def add(self, cookie):
            cookie.vertex = self.graph.add_vertex()
            for parent in cookie.parents:
                self.graph.add_edge(parent.vertex, cookie.vertex)

    __instance__ = None

    def __new__(cls):
        if not Graph.__instance__:
            Graph.__instance__ = Graph.__Graph__()
        return Graph.__instance__

    def __getattr__(self, name):
        return getattr(self.__instance__, name)

    def __setattr__(self, name):
        return setattr(self.__instance__, name)
