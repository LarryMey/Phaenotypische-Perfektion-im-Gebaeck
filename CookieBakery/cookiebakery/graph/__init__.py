from graph_tool.all import Graph as GT_Graph
from cookiebakery.mq import CookieRecvr
import logging

class Graph:
    # there is only one graph, so implement as singleton
    class __Graph__:

        def __init__(self):
            self.graph = GT_Graph()
            self.cookies = dict()
            self.cookierecvr = CookieRecvr(self)
            self.cookierecvr.start()

        def new_cookie(self, cookie):
            self.cookies[cookie['cid']] = self.graph.add_vertex()
            logging.info('added cookie {} to graph'.format(cookie['cid']))
            for parent in cookie['parents']:
                try:
                    self.graph.add_edge(self.cookies[parent],
                                        self.cookies[cookie['cid']])
                    logging.info(
                        'added eddge from cookie {} to graph'.format(parent))
                except KeyError:
                    logging.info('parent not known in graph')


    __instance__ = None

    def __new__(cls):
        if not Graph.__instance__:
            Graph.__instance__ = Graph.__Graph__()
        return Graph.__instance__

    def __getattr__(self, name):
        return getattr(self.__instance__, name)

    def __setattr__(self, name):
        return setattr(self.__instance__, name)
