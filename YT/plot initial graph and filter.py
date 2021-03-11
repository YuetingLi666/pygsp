from pygsp import graphs, filters
import matplotlib.pyplot as plt
import numpy as np
G = graphs.Comet()
G.compute_fourier_basis()  # Fourier to plot the eigenvalues.
# lmax = G.estimate_lmax()
# print('{:.2f}'.format(G.lmax))
DELTAS=[2,20]
s=np.zeros(G.N)
s[DELTAS]=1

# Fig.1
fig = plt.figure(figsize=(25,15))
ax = fig.add_subplot(3,3,1)
G.plot(s, ax=ax)

g = filters.Meyer(G)
# g = filters.Meyer(G,scales=[5,2,1,0.6,0.4])
scales= [0]+g.scales.tolist()
print(scales)
s = g.filter(s, method='exact')
# g2 = filters.Heat(G, scale=5)
# s2 = g2.filter(s)




ax = fig.add_subplot(3, 3, 2)
title='Meyer Scaling(scale={})'.format(scales[0])
G.plot(s[:, 0], ax=ax, title=title)
# G.plot(s[:, 0], ax=ax, title='Meyer Scaling', highlight=DELTAS)
ax.set_axis_off()

for i in range(1, 6):
    ax = fig.add_subplot(3,3,i+2)
    title='Meyer Wavelet(scale={})'.format(scales[i])
    G.plot(s[:,i],ax=ax,title=title)
    ax.set_axis_off()
# ax = fig.add_subplot(3,3,7)
# G.plot(l,ax=ax,title='localization')
# ax.set_axis_off()


ax = fig.add_subplot(3,3,8)
g.plot(ax=ax)




fig.tight_layout()
# plt.savefig('airfoil-meyer.png',dpi=500)
plt.show()



#
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)
# g1.plot(ax=ax1)
# G.plot(s1, ax=ax2, highlight=DELTAS)
# g2.plot(ax=ax3)
# G.plot(s2, ax=ax4, highlight=DELTAS)
