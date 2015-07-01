#!/usr/bin/python
from graph_tool.all import *
from cookiebakery.cookies.evolution import Evolution
from cookiebakery.graph import Graph
from gi.repository import Gtk, GObject
import random
import time


graph = Graph().graph
evolution = Evolution()
count = 0
pos = arf_layout(graph)

def run_simulation():
    def update_state():
        global graph
        global evolution
        global count
        global pos

        if count % 60 == 0:
            anc = random.choice(evolution.ancestors)
            evolution.next(anc.last())
            win.graph.fit_to_window(ink=True)
        count += 1

        pos = arf_layout(graph, pos=pos)
        win.graph.regenerate_surface(lazy=False)
        win.graph.queue_draw()
        return True

    win = GraphWindow(graph, pos, geometry=(500, 400))
    win.connect("delete-event", Gtk.main_quit)
    GObject.timeout_add(100, update_state)
    win.show_all()
    Gtk.main()
