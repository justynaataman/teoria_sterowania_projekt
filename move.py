import numpy as np
from robopy.base import pose
from robopy import rpy2r
import random
from moves import move_lin

def animate_robot(robot, start, path, i):
   
    r1 = random.randint(-10,10)
    r1 /= 10 
    r2 = random.randint(-10,10)
    r2 /= 10 
    r3 = random.randint(-10,10)
    r3 /= 10 
    t1 = random.randint(-10,10)
    t1 /= 10 
    t2 = random.randint(-10,10)
    t2 /= 10 
    t3 = random.randint(-10,10)
    t3 /= 10 
    rot1 = rpy2r([0, 0, 0], unit='deg')
    tran1 = [float(t1), float(t2), float(t3)]
    path2 = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)
    new_path = move_lin(robot, start, path2)
    print(path)
    print("######")
    print(new_path)
    if i == 0:
        path.append(new_path)
    else: 
        path = np.concatenate((path, new_path), axis=0) 
    i += 1 
    return path2
