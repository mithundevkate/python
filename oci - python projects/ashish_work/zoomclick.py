from platform import python_version as pythonversion
print('python: '+pythonversion())
import matplotlib.pyplot as plt
from matplotlib import __version__ as matplotlibversion
print('matplotlib: '+matplotlibversion)
import networkx as nx
from networkx import __version__ as networkxversion
print('networkx: '+networkxversion)

G = nx.DiGraph()
G.add_path([3, 5, 4, 1, 0, 2, 7, 8, 9, 6])
G.add_path([3, 0, 6, 4, 2, 7, 1, 9, 8, 5])

plt.figure(figsize=(8,6))

nx.draw_networkx(G, with_labels=True)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in ['right','top','bottom','left']:
    plt.gca().spines[pos].set_visible(False)

plt.show()
