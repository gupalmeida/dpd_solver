import os
import sys
import numpy as np

def getValue(varname,filename='input.inp',dtype='int'):
    """ Gets value of a given variable from input file. Variable name is given as string and the method returns numerical value according to dtype argument given by user. dtype argument must be passed as string and its default value is 'int'."""
    # defining input file path and file name
    fp = os.getcwd() + '/' + filename
    f = open(fp,'r')
    value = ""

    try:
        while f.readline(): # while not EOF
            for line in f:
                if ('@' + varname) in line: # get value for varname
                    #print(line) # debug print
                    line = f.readline()
                    value = line.rstrip('\n')
                    #print(value,type(value)) # debug print
                else : continue
    except:
        print("Error to get variable value from input file.")

    f.close()
    if dtype == 'bool':
        value = value.lower() in ['true','1','y','yes']
    cmd = dtype + '(value)'
    #print(cmd) # debug print
    return eval(cmd)

def exportFields(cname,solution=None,timeStep=None,varList=list()):
    """ Writes output file in dat format for visualizing data in ParaView or Tecplot. For temporal analysis the parameter 'timeStep' should be provided. Also, a list of variable names may be provided in order to allow the method to write their respective values."""

    if solution is not None:
        # GETTING COORDINATE VECTORS FROM SOLUTION
        # solution tuple is given in the following order
        # (n_dim, x_coord, y_coord, z_coord, solution_variables)
        x = solution[0]
        y = solution[1]
        z = solution[2]

        # OPENING FILE FOR WRITING
        fp = os.getcwd() + '/' + cname + '.dat'
        f = open(fp,'w')

        # DEFINING HEADER
        h1 = "TITLE = \" " + cname + " \" \n"
        if len(varList) != 0:
            variables = ",\"" + "\",\"".join(varList) + "\""
            h2 = "VARIABLES = \"X\", \"Y\", \"Z\"" + variables + "\n"
        else : 
            h2 = "VARIABLES = \"X\", \"Y\", \"Z\"\n"
        h3 = "ZONE T =\"Zone-one\", I={:d} ,J={:d} , K={:d},DATAPACKING=POINT\n".format(np.shape(x)[0],np.shape(x)[1],np.shape(x)[2])

        # WRITING HEADER
        f.write(h1)
        f.write(h2)
        f.write(h3)

        # WRITING SOLUTION
        # mapping variables into strings for writing
        data = np.array([arr.astype(str) for arr in solution])

        # getting number of nodes in each direction
        _i,_j,_k = np.shape(solution[0])
        for k in range(_k):
            for j in range(_j):
                for i in range(_i):
                    x_ = data[0]
                    y_ = data[1]
                    z_ = data[2]
                    f.write(" ".join([x_[i,j,k],y_[i,j,k],z_[i,j,k]])+"\n")


        # CLOSING OUTPUT FILE
        f.close()

    else : print("Empty solution. Not writing output file")

def write_csv(cname,solution,sep=','):
    """ Simply exports your data to a csv file using any desired separator. No header should be specified. """
        
    # OPENING FILE FOR WRITING
    fp = os.getcwd() + '/' + cname + '.dat'
    f = open(fp,'w')

    ### TODO - Implement columnwise file writer
    f.close()
    return None

def write_to_file(cname,data):
    """ Simply writes an array to a file. """

    # OPENING FILE FOR WRITING
    fp = os.getcwd() + '/' + cname + '.dat'
    f = open(fp,'w')

    for value in data:
        f.write(str(value))

    f.close()

def clear_data():
    """ Clears all data related to previous simulations. """
    pass