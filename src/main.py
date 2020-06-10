import numpy as np
import IOtools as io
import preProcess as pre
from numerics import fvm
from numerics import dpd

### HERE WILL BE THE PLACE WHERE IMPORTANT STUFF TAKES PLACE. FOR NOW,
### YOU WILL FIND ONLY DEBUG COMMANDS. HOLD ON, GOOD TIMES ARE COMING!!!

def main():
    caseId = io.getValue('runcaseID',dtype='str')
    simType = io.getValue('simType',dtype='int')
    
    if simType == 1:
        print(">>> Staring simulation...")
        print(">>> FVM")
        # creating computational mesh
        meshTools = pre.mesh()
        msh = meshTools.genStructBlock()
        meshTools.compute_centroids__()
        solution = fvm(msh)
        solution.solve()
        print(">>> Simulation finished\n")

    elif simType == 2:
        print(">>> Staring simulation")
        print(">>> DPD")
        print(">>> Simulation finished\n")

# ===========================================================
if __name__== "__main__":
    main()
