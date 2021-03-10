# import numpy as np
# from scipy import sparse
#
# from pygsp import utils
# from pygsp.graphs import Graph
import pygsp.graphs as graphs
import matplotlib.pyplot as plt

G = graphs.Minnesota()
fig, axes = plt.subplots(1, 2)
_ = axes[0].spy(G.W, markersize=0.5)
_ = G.plot(ax=axes[1])
plt.show()