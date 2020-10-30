import pygrib
import numpy as np
import os
from sys import argv

# obtain all the fluxes file path
def get_filepaths(directory,string):

    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            if string in filepath:
                file_paths.append(filepath)  # Add it to the list.

    return file_paths
    


def deaccumulatedsata(grbs,i):
    gout=grbs.message(i+1)
    if grbs.message(i+1).endStep==1:
            gout.values=grbs.message(i+1)['values']/3600.0
    if grbs.message(i+1).endStep>1:
            deux=(grbs.message(i+1)['values']-grbs.message(i)['values'])/3600.0
            gout.values=deux
    print(grbs.message(i+1).endStep)        
    print(gout.endStep)
    gout.endStep=grbs.message(i+1).endStep
    #gout.timeRangeIndicator=0
    msg = gout.tostring()
    return msg
    
##### MAIN #####
string='4_FC'
script=argv[0]
directory=argv[1]
filepaths=get_filepaths(directory,string)

for fn in filepaths:
    grbs=pygrib.open(fn)
    fnout=fn.replace('4_FC','0_FC')
    #if not os.path.exists(fnout):
    grbout = open(fnout,'wb')
    [grbout.write(deaccumulatedsata(grbs,i)) for i in np.arange(0,grbs.messages)]
    grbout.close()
    grbs.close()