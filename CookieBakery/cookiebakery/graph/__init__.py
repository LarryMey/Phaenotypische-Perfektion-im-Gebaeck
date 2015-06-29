from graph_tool.all import Graph

class CookieGraph:
    # there is only one graph, so implement as singleton
    class __Graph__:
        
        def __init__(self):
            self.graph = Graph()

        def add(self, cookie):
            cookie.vertex = self.graph.add_vertex()
            for parent in cookie.parents:
                self.graph.add_edge(parent.vertex, cookie.vertex)

    __instance__ = None

    def __new__(cls):
        if not CookieGraph.__instance__:
            CookieGraph.__instance__ = CookieGraph.__Graph__()
        return CookieGraph.__instance__

    def __getattr__(self, name):
        return getattr(self.__instance__, name)

    def __setattr__(self, name):
        return setattr(self.__instance__, name)
