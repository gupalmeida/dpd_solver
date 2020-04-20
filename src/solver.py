import numpy as np
import IOtools as io

def main():
    n = io.getValue('n')
    caseId = io.getValue('runcaseID',dtype='str')
    io.writeToParaview(caseId)

if __name__== "__main__":
    main()
