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

    def stub(self):
        print(self.msh)
