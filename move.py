import numpy as np
from robopy.base import pose
from robopy import rpy2r
import random
from moves import move_lin

def animate_robot(robot, start, path, i):
   
   
    if i != 0: 
        i2 = i/2
    else: 
        i2 = i
    rot1 = rpy2r([0, 0, 0], unit='deg')
    tran1 = [0.1, 0.1, 0.1]
    path2 = pose.SE3(tran1[0] + i2, tran1[1] + i2, tran1[2] + i2, rot1)
    new_path = move_lin(robot, start, path2)

    if i == 0:
        path=new_path
    else: 
        path = np.concatenate((path, new_path), axis=0) 
    i += 1
    print(i)
    return path2, path, i
