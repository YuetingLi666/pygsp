# -*- coding: utf-8 -*-

from . import Graph

import numpy as np
from scipy import sparse


class Torus(Graph):
    r"""
    Create a Torus graph.

    Parameters
    ----------
    Nv : int
        Number of vertices along the first dimension (default is 16)
    Mv : int
        Number of vertices along the second dimension (default is Nv)

    Examples
    --------
    >>> from pygsp import graphs
    >>> Nv = 32
    >>> G = graphs.Torus(Nv=Nv)

    References
    ----------
    See :cite:`strang1999discrete` for more informations.

    """

    def __init__(self, Nv=16, Mv=None, **kwargs):

        if not Mv:
            Mv = Nv

        # Create weighted adjancency matrix
        K = 2 * Nv
        J = 2 * Mv
        i_inds = np.zeros((K*Mv + J*Nv), dtype=float)
        j_inds = np.zeros((K*Mv + J*Nv), dtype=float)

        for i in range(Mv):
            i_inds[i*K + np.arange(K)] = i*Nv + \
                np.concatenate((np.array([Nv - 1]), np.arange(Nv - 1),
                                np.arange(Nv)))

            j_inds[i*K + np.arange(K)] = i*Nv + \
                np.concatenate((np.arange(Nv), np.array([Nv - 1]),
                                np.arange(Nv - 1)))

        for i in range(Mv - 1):
            i_inds[K*Mv + i*2*Nv + np.arange(2*Nv)] = \
                np.concatenate((i*Nv + np.arange(Nv),
                                (i + 1)*Nv + np.arange(Nv)))

            j_inds[K*Mv + i*2*Nv + np.arange(2*Nv)] = \
                np.concatenate(((i + 1)*Nv + np.arange(Nv),
                                i*Nv + np.arange(Nv)))

        i_inds[K*Mv + (Mv - 1)*2*Nv + np.arange(2*Nv)] = \
            np.concatenate((np.arange(Nv), (Mv - 1)*Nv + np.arange(Nv)))

        j_inds[K*Mv + (Mv - 1)*2*Nv + np.arange(2*Nv)] = \
            np.concatenate(((Mv - 1)*Nv + np.arange(Nv), np.arange(Nv)))

        self.W = sparse.csc_matrix((np.ones((K*Mv + J*Nv)), (i_inds, j_inds)),
                                   shape=(Mv*Nv, Mv*Nv))

        # Create Coordinate
        T = 1.5 + np.sin(np.arange(Mv)*2*np.pi/Mv).reshape(1, Mv)
        U = np.cos(np.arange(Mv)*2*np.pi/Mv).reshape(1, Mv)
        xtmp = np.cos(np.arange(Nv).reshape(Nv, 1)*2*np.pi/Nv)*T
        ytmp = np.sin(np.arange(Nv).reshape(Nv, 1)*2*np.pi/Nv)*T
        ztmp = np.kron(np.ones((Nv, 1)), U)
        self.coords = np.concatenate((np.reshape(xtmp, (Mv*Nv, 1), order='F'),
                                      np.reshape(ytmp, (Mv*Nv, 1), order='F'),
                                      np.reshape(ztmp, (Mv*Nv, 1), order='F')),
                                     axis=1)
        self.Nv = Nv
        self.Mv = Nv
        self.directed = False
        self.gtype = 'Torus'
        self.plotting = {"vertex_size": 30,
                         "limits": np.array([-2.5, 2.5, -2.5, 2.5, -2.5, 2.5])}

        super(Torus, self).__init__(W=self.W, directed=self.directed,
                                    gtype=self.gtype, coords=self.coords,
                                    plotting=self.plotting, **kwargs)
