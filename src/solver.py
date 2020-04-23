import numpy as np
import IOtools as io
import preProcess as pre

### HERE WILL BE THE PLACE WHERE IMPORTANT STUFF TAKES PLACE. FOR NOW,
### YOU WILL FIND ONLY DEBUG COMMANDS. HOLD ON, GOOD TIMES ARE COMING!!!

def main():
    n = io.getValue('n')
    caseId = io.getValue('runcaseID',dtype='str')
    msh = pre.mesh()
    data = msh.genStrcdBlock()
    io.exportFields(caseId,solution=data,varList=[])

if __name__== "__main__":
    main()
