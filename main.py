#setup automa
from statemachine import StateMachine, State, Transition
from slaves import *
from Generator.generator import Generator
import argparse
import robopy.base.model as robot
import sys
from robopy import rpy2r
from robopy.base import pose
import time
from moves import move_lin
from move import animate_robot
import networkx as nx
from viz import *
import matplotlib.pyplot as plt

#create visualization in networkX
visor = nx.DiGraph()
visor, visor_pos = create_graph(visor)

def trace(data):
    nodeA = ""
    nodeB = ""
    flaga = 0
    for sign in data:
        if sign == '.':
            flaga = 1
        else:
            if flaga == 0:
                nodeA = nodeA + sign
            else:
                nodeB = nodeB + sign
    print("avaible traces:")
    show_path(nodeA, nodeB, visor)
    print("")

def display(data):
    if data == 'all':
        cam_viz()
        move_b_viz()
        grab_obj_viz()
        check_box_pos_viz()
        arm_box_viz()
        move_a_viz()
        put_o_viz()
    else:
        # wait, cam, grab, check_box_pos, is_arm, move_b, move_a, put_o
        if data == 'cam':
            cam_viz()
        if data == 'move_b':
            move_b_viz()
        if data == 'grab':
            grab_obj_viz()
        if data == 'check_box_pos':
            check_box_pos_viz()
        if data == 'is_arm':
            arm_box_viz()
        if data == 'move_a':
            move_a_viz()
        if data == 'put_o':
            put_o_viz()





des_id = 0
def automata(path, des_id):
   update_graph(visor_pos, visor, "wait")
   def start_point(robot):
   

    rot1 = rpy2r([0, 0, 0], unit='deg')
    tran1 = [0.0, 0.0, 0.0]
    start = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)


    rot2 = rpy2r([0, 0, 0], unit='deg')
    tran2 = [0.1, 0.1, 0.1]
    stop = pose.SE3(tran2[0], tran2[1], tran2[2], rot2)

    new_path = move_lin(robot, start, stop)

 
    return new_path, stop

   """
   rot1 = rpy2r([0, 0, 0], unit='deg')
   tran1 = [0.0, 0, 0]
   start = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)
   rot1 = rpy2r([0, 0, 0], unit='deg')
   tran1 = [0.01, 0.01, 0.01]
   stop = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)
   path_a = move_lin(robot, start, stop)
   """
  
   
   #path_a = None
   # create a supervisor
   supervisor = Generator.create_master(master_states, master_transition)
   print(des_path[des_id])
   time.sleep(3.0)
   des_id = des_id + 1
   print('\n' + str(supervisor))
   i = 0
   # run supervisor for exemplary path
   print("Executing path: {}".format(path))
   model = robot.Puma560()
   path_a, start =start_point(model)
   for event in path:

       # launch a transition in our supervisor
       master_transition[event]._run(supervisor)
       events = ['camera', 'move_base', 'grab_obj', 'move_arm', 'check_box_pos', 'arm_box', 'put_obj']
       print(supervisor.current_state)
       val = supervisor.current_state.value
       slave_states = None
       slave_transition = None
       slave_path = None
       if val == "camera":
           print("cam")
           update_graph(visor_pos, visor, "cam")
           slave_states = camera_states
           slave_transition = camera_transitions
           slave_path = paths_camera
       if val == "move_base":
           update_graph(visor_pos, visor, "move_b")
           slave_states = move_base_states
           slave_transition = move_base_transitions
           slave_path = paths_move_base
           print("move base")
           print(path_a)

       if val == "grab_obj":
           update_graph(visor_pos, visor, "grab")
           print("grab obj")
           slave_states = grab_obj_states
           slave_path = paths_grab_obj
           slave_transition = grab_obj_transitions
      
       if val == "move_arm":
           update_graph(visor_pos, visor, "move_a")
           slave_transition = move_arm_transitions
           slave_states = move_arm_states
           slave_path = paths_move_arm
           print("move arm")
           start, path_a, i = animate_robot(model, start, path_a, i)
       if val == 'check_box_pos':
           update_graph(visor_pos, visor, "check_box_pos")
           slave_transition = check_box_pose_transitions
           slave_states = check_box_pose_states
           slave_path = paths_check_box_pos
           print("check box pos")
       if val == "arm_box":
           update_graph(visor_pos, visor, "is_arm")
           slave_transition = arm_box_transitions
           slave_states = arm_box_states
           slave_path = paths_arm_box
           print("arm box")
       if val == "put_obj":
           update_graph(visor_pos, visor, "put_o")
           slave_transition = put_obj_transitions
           slave_states = put_obj_states
           slave_path = paths_put_obj
           print('put obj')

         
       #create slave automata
       if slave_states is not None:
           slave = Generator.create_master(slave_states, slave_transition)
           #for now first path
           ss = slave_path[0]
           for x in ss:
               slave_transition[x]._run(slave)
               print(slave.current_state)
               time.sleep(1.0)
       time.sleep(2.0)
       print("")
   plt.clf()
   model= robot.Puma560()
   model.animate(stances=path_a, frame_rate=30, unit='deg')

   print('Supervisor done!')



if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="num of path to run",
                        type=int, default=0)
    parser.add_argument("--display_trace", help="add if you want to display graph for one of slaves. add name of the slave, eg --display=cam.  add all to display all graphs. Avaible nodes: wait, cam, grab, check_box_pos, is_arm, move_b, move_a, put_o",
                        type=str, default=None)
    parser.add_argument("--trace", help="print trace between 2 nodes. format: --trace=nodeA.nodeB. Avaible nodes: wait, cam, grab, check_box_pos, is_arm, move_b, move_a, put_o",
                        type=str, default=None)
    args = parser.parse_args()
    if args.path>2:
        print("add another path: 0, 1, 2")
    else:
        if args.display_trace is None:
            if args.trace != None:
                trace(args.trace)
            automata(path=paths[args.path], des_id=args.path)
        else:
            display(args.display_trace)



