#!/usr/bin/python
from cookiebakery.cookies.evolution import Evolution
from cookiebakery.graph import Graph
from graph_tool.draw import GraphWindow, arf_layout, sfdp_layout
from gi.repository import Gtk, GObject
import logging
import random
import time


logformat = "%(asctime)s %(levelname)s [%(name)s][%(threadName)s] %(message)s"
logging.basicConfig(format=logformat, level=logging.DEBUG)

count = 0
pos = None


def run_simulation():
    logformat = "%(asctime)s %(levelname)s [%(name)s][%(threadName)s] %(message)s"
    logging.basicConfig(format=logformat, level=logging.DEBUG)

    evolution = Evolution()
    while(True):
            time.sleep(20)
            anc = random.choice(evolution.ancestors)
            evolution.next(anc.last())


def run_visualization():
    global pos
    graph = Graph().graph

    def update_state():
        global count
        global pos

        if count % 60 == 0:
            logging.debug('fit to window')
            win.graph.fit_to_window(ink=False)
        count += 1

        pos = arf_layout(pos.get_graph(), pos=pos, max_iter=1)
        win.graph.regenerate_surface(lazy=False)
        win.graph.queue_draw()
        return True

    while graph.num_vertices() < 2:
        time.sleep(4)
        logging.info("waiting for cookies")

    pos = arf_layout(graph, max_iter=0)
    win = GraphWindow(pos.get_graph(), pos, geometry=(500, 400))
    win.connect("delete-event", Gtk.main_quit)
    GObject.timeout_add(100, update_state)
    win.show_all()
    Gtk.main()
