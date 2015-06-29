from cookiebakery.cookies import Cookie
from cookiebakery.graph import CookieGraph
from graph_tool import Vertex

class TestGraph:

    def test_singleton(self):
        graph1 = CookieGraph()
        graph2 = CookieGraph()
        assert graph1 is graph2

    def test_add(self):
        g = CookieGraph()
        cookie = Cookie()
        assert isinstance(cookie.vertex, Vertex)
