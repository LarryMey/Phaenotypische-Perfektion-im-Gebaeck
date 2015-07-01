from cookiebakery.cookies import Cookie
from cookiebakery.graph import Graph
from graph_tool import Vertex

class TestGraph:

    def test_singleton(self):
        graph1 = Graph()
        graph2 = Graph()
        assert graph1 is graph2

    def test_add(self):
        g = Graph()
        cookie = Cookie()
        assert isinstance(cookie.vertex, Vertex)
