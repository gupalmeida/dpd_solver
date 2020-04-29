import os,sys
import numpy as np
import IOtools as io

class mesh:
    """ The mesh class presents methods for importing, exporting and generating computational meshes for later use in simulations. """

    def __init__(self):
        meshfile = 'mesh.inp'
        self.action = io.getValue('meshAction',filename=meshfile,dtype='str')
        self.mshtype = io.getValue('meshType',filename=meshfile,dtype='str')
        self.writeMesh = io.getValue('writeMesh',filename=meshfile,dtype='bool')
        self.nx = io.getValue('nx',filename=meshfile,dtype='int')
        self.ny = io.getValue('ny',filename=meshfile,dtype='int')
        self.nz = io.getValue('nz',filename=meshfile,dtype='int')

    def __genStructBlock(self,origin=(0,0,0),dim_x=1,dim_y=1,dim_z=1,
            nx=10,ny=10,nz=1,indexing='ij',write_msh_file=False):
        """ Generates a simple structured block mesh. The user should pass the origin of the block as a tuple, the dimensions in x, y and z directions (dim_x, dim_y and dim_z), as well as the number of nodes in each direction (nx, ny and nz). """

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
        # TODO - Include stretching function for points in mesh

        # obtaining block mesh coordinate arrays
        x,y,z = np.meshgrid(x_,y_,z_,indexing=indexing)
        data = (x,y,z)

        # writing mesh file
        if write_msh_file:
            io.exportFields("mesh",solution=data)

        return data

    def createMesh(self):
        if self.action == 'create' and self.mshtype == 'structured':
            return self.__genStructBlock(nx=self.nx,ny=self.ny,nz=self.nz,write_msh_file=self.writeMesh)
        elif self.action == 'create' and self.mshtype == 'unstructured':
            print("Unstructured mesh not implemented yet")
        elif self.action == 'read':
            print("Read mesh not implemented yet")

