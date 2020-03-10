import os
import sys

def getValue(varname):
    """ This method gets value of a given variable from input file. Variable name is given as string and the method returns numerical value as a string so that the user converts the value to the correct data type according to the varible to be used. """
    # defining input file path and file name
    fp = os.getcwd() + "/input.inp"
    f = open(fp,'r')
    value = -999999.0

    try:
        while f.readline(): # while not EOF
            for line in f:
                if ('@' + varname) in line: # get value for varname
                    #print(line) # debug print
                    line = f.readline()
                    value = line
                    #print(line) # debug print
                else : continue
    except:
        print("Error to get variable value from input file.")

    f.close()
    return value
