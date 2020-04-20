import os
import sys

def getValue(varname,dtype='int'):
    """ This method gets value of a given variable from input file. Variable name is given as string and the method returns numerical value according to dtype argument given by user. dtype argument must be passed as string and its default value is 'int'."""
    # defining input file path and file name
    fp = os.getcwd() + "/input.inp"
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
    cmd = dtype + '(value)'
    #print(cmd) # debug print
    return eval(cmd)

def writeToParaview(fname,solution=None,timeStep=None):
    """ This method writes output file in csv format for visualize data in ParaView. For temporal analysis the parameter 'timeStep' should be provided. """

    fp = os.getcwd() + '/' + fname + '.csv'
    header = 'x coord, y coord, z coord,'
    f = open(fp,'w')
    f.write(header)
    f.write('testing')
    f.close()
    ### TODO
    ### Implementation yet to finish
