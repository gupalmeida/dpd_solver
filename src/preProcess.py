import os,sys
import numpy as np
import IOtools as io

class mesh:
    """ The mesh class presents methods for importing, exporting and generating computational meshes for use in simulations. """

    def genStrcdBlock(self,origin=(0,0,0),dim_x=1,dim_y=1,dim_z=1,
            nx=10,ny=10,nz=1,indexing='ij',write_msh_file=False):
        """ This method consists in generating a simple structure block mesh. The user should pass the origin of the block as a tuple, the dimensions in x, y and z directions (dim_x, dim_y and dim_z), as well as the number of nodes in each direction (nx, ny and nz). """

        # defining vertices
        x0 = origin[0] - dim_x/2.0
        x1 = origin[0] + dim_x/2.0

        y0 = origin[1] - dim_y/2.0
        y1 = origin[1] + dim_y/2.0

        z0 = origin[2] - dim_z/2.0
        z1 = origin[2] + dim_z/2.0

        # writing space vectors
        x_ = np.linspace(x0,x1,nx)
        y_ = np.linspace(y0,y1,ny)
        z_ = np.linspace(z0,z1,nz)

        # obtaining block mesh coordinate arrays
        x,y,z = np.meshgrid(x_,y_,z_,indexing=indexing)

        return (x,y,z)
