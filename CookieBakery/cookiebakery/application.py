from cookiebakery.cookies.evolution import Evolution
from cookiebakery.graph import CookieGraph
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
from graph_tool.all import *
import random
import time


count = 0

def run_simulation():
    graph = CookieGraph().graph
    evolution = Evolution()

    for i in range(100):
        anc = random.choice(evolution.ancestors)
        evolution.next(anc.last())

    graph_draw(graph, vertex_text=graph.vertex_index, vertex_font_size=18, output_size=(2000, 2000), output="nodes.png")
