# #!/usr/bin/env python
# Author :
# Version : 1.0


#import pandas as pd
import networkx
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
#import numpy as np

# loading Digraph
G = networkx.DiGraph()

# CSV file reading
with open('C:\\Personal\\ashish_work\\protein_2.csv', 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader][1:]

# Get a list of just the node names (the first item in each row)
node_names = [n[0] for n in nodes]
G.add_nodes_from(node_names)

with open('C:\\Personal\\ashish_work\\protein_2.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [str(e) for e in edgereader][1:]
#print(edges)
#for d in pd.read_csv('protein.csv'):

# Print the number of nodes and edges in our two lists
for e in edges:
    G.add_edge(e.split(',')[0],e.split(',')[1])

    #print(e)
'''
print(G.in_edges)
print(G.out_edges)
print(len(node_names))
print(len(edges))
'''
 # Add nodes to the Graph
#G.add_edges_from(edges) # Add edges to the Graph


## Adding class to make zoom in and zoom out on the basis of cursor wheel scrolling
class ZoomPan:
    def __init__(self):
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None


    def zoom_factory(self, ax, base_scale = 2.):
        def zoom(event):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata # get event x location
            ydata = event.ydata # get event y location

            if event.button == 'down':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'up':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
                print (event.button)

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

            ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * (relx)])
            ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * (rely)])
            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event',onPress)
        fig.canvas.mpl_connect('button_release_event',onRelease)
        fig.canvas.mpl_connect('motion_notify_event',onMotion)

        #return the function
        return onMotion


fig = figure()
ax = fig.add_subplot(111, xlim=(0,1), ylim=(0,1), autoscale_on=True)

ax.set_title('Move cursor to zoom in and zoom out')

pos = networkx.spring_layout(G,scale=5)
x = 1
y = 2
ax.scatter(x,y,networkx.draw(G,pos,node_size=5,with_labels=False))
scale = 1.1
zp = ZoomPan()
figZoom = zp.zoom_factory(ax, base_scale = scale)
figPan = zp.pan_factory(ax)
plt.savefig('C:\\Personal\\ashish_work\\directedgraph.jpg')
show()
