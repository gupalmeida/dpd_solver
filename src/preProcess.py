import os,sys,shutil
import numpy as np
import IOtools as io

class mesh:
    """ The mesh class presents methods for importing, exporting and generating computational meshes for later use in simulations. """

    def __init__(self):
        print(">>> Initializing mesh parameters")
        meshfile = 'mesh.inp'
        self.action = io.getValue('meshAction',filename=meshfile,dtype='str')
        self.mshtype = io.getValue('meshType',filename=meshfile,dtype='str')
        self.writeMesh = io.getValue('writeMesh',filename=meshfile,dtype='bool')
        self.writeNodeData = io.getValue('writeNodeData',filename=meshfile,dtype='bool')
        self.nx = io.getValue('nx',filename=meshfile,dtype='int')
        self.ny = io.getValue('ny',filename=meshfile,dtype='int')
        self.nz = io.getValue('nz',filename=meshfile,dtype='int')
        print(">>> Finished!\n")

    def __write_node_file__(self,cname,nodeArray,fpath='nodes',rm_dir=False):
        """ Writes node array to a file in a given coordinate axis. """

        if fpath == 'nodes':
            fp = os.getcwd() + '/mesh/nodes/'
        elif fpath == 'centroids':
            fp = os.getcwd() + '/mesh/centroids/'
        fn = fp + cname

        # checking for existing directory
        isDir = os.path.exists(fp)

        try:
            os.makedirs(fp)
        except OSError:
            print(">>> Warning: Creation of the directory %s failed" %fp)
        else:
            print(">>> Successfully created the directory %s " %fp)
 
        # writting the data
        f = open(fn,'w')

        for value in nodeArray:
            f.write(str(value)+'\n')
            
        f.close()

    def __read_node_file__(self,cname):
        """ Reads node coordinates from file and return it as a numpy array. """

        fp = os.getcwd() + '/mesh/nodes/'
        fn = fp + cname

        l = open(fn,'r').read()
        arr = np.array(l.split()).astype(float)

        return arr

    def genStructBlock(self,origin=(0,0,0),dim_x=1,dim_y=1,dim_z=1):
        """ Generates a simple structured block mesh. The user should pass the origin of the block as a tuple, the dimensions in x, y and z directions (dim_x, dim_y and dim_z), as well as the number of nodes in each direction (nx, ny and nz). """
        indexing = 'ij'
        write_msh_file = self.writeMesh
        write_node_data = self.writeNodeData
        nx = self.nx
        ny = self.ny
        nz = self.nz

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

        # exporting vertices coord
        nodeData = (x_,y_,z_)
        if write_node_data:
            print(">>> Writing nodes coordinates to file...")
            self.__write_node_file__(cname='x_nodes',nodeArray=x_)
            self.__write_node_file__(cname='y_nodes',nodeArray=y_)
            self.__write_node_file__(cname='z_nodes',nodeArray=z_)
            print(">>> Finished!\n")

        # obtaining block mesh coordinate arrays
        x,y,z = np.meshgrid(x_,y_,z_,indexing=indexing)
        data = (x,y,z)

        # writing mesh file
        if write_msh_file:
            print(">>> Writing structured block to file...")
            io.exportFields("mesh",solution=data)
            print(">>> Finished!\n")

        return data

    def compute_centroids__(self):
        """ Computes cell centroids from nodes coordinates. """
        xv = self.__read_node_file__(cname='x_nodes')
        yv = self.__read_node_file__(cname='y_nodes')
        zv = self.__read_node_file__(cname='z_nodes')
        print(">>> Total number of nodes: {:d} x {:d} x {:d}\n".format(len(xv),len(yv),len(zv)))
        
        # computing centroids coordinates from vertices
        print(">>> Computing cell centroids...")
        xc = np.empty(len(xv)-1)
        yc = np.empty(len(yv)-1)
        zc = np.empty(len(zv)-1)
        for i in range(len(xv)-1):
            xc[i] = (xv[i] + xv[i+1])/2.0
        self.__write_node_file__(cname='x_c',nodeArray=xc,fpath='centroids')

        for i in range(len(yv)-1):
            yc[i] = (yv[i] + yv[i+1])/2.0
        self.__write_node_file__(cname='y_c',nodeArray=yc,fpath='centroids')

        for i in range(len(zv)-1):
            zc[i] = (zv[i] + zv[i+1])/2.0
        self.__write_node_file__(cname='z_c',nodeArray=zc,fpath='centroids')

        print(">>> Finished\n")
        print(">>> Total number of centroid coordinates: {:d} x {:d} x {:d}\n".format(len(xc),len(yc),len(zc)))


class particle:

    def __init__(self):
        print(">>> Initializing particle parameters\n")
        self.id = int()
        self.dp = io.getValue('dp',dtype='float')
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.ux = 0.0
        self.uy = 0.0
        self.uz = 0.0