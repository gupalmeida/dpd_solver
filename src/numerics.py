import os,sys
import numpy as np
from preProcess import mesh

class fvm(object):
    """ Finite Volume Method (FVM) class. Contains numerical algorithms using the FVM discretization technique. """

    # declaring private variables, attributes and methods
    #__msh = mesh()

    # --------------------
    # Initialization
    def __init__(self,grid):
        self.msh = grid
        self.solution = np.empty_like(self.msh[0])

    def __computeCentroids(self):
        pass

    def __applyBCs(self):
        _nx = np.shape(self.solution)[0]
        _ny = np.shape(self.solution)[1]
        _nz = np.shape(self.solution)[2]
        self.solution[::] = 0.0
        self.solution[:_ny:] = 1.0
        return self.solution

    def solve(self):
        self.__applyBCs()
        return self.solution

class dpd(object):
    """ Dissipative Particle Dynamics (DPD) class. Contains numerical algorithms using DPD technique. """
    pass
