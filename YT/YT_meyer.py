import matplotlib.pyplot as plt
import pygsp.graphs as graphs
import pygsp.filters as filters
G = graphs.Ring(N=20)
G.estimate_lmax()
G.set_coordinates('line1D')
g = filters.Meyer(G)
s = g.localize(G.N // 2)
fig, axes = plt.subplots(1, 2)
_ = g.plot(ax=axes[0])
_ = G.plot(s, ax=axes[1])
plt.show()