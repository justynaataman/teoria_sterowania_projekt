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


path_a = None
model = robot.Puma560()

rot1 = rpy2r([0, 0, 0], unit='deg')
tran1 = [0, 0, 0]
start = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)

#create visualization in networkX
visor = nx.DiGraph()
visor, visor_pos = create_graph(visor)



des_id = 0
for path in paths:
   update_graph(visor_pos, visor, "wait")
   # create a supervisor
   supervisor = Generator.create_master(master_states, master_transition)
   print(des_path[des_id])
   time.sleep(3.0)
   des_id = des_id + 1
   print('\n' + str(supervisor))
   i = 0
   # run supervisor for exemplary path
   print("Executing path: {}".format(path))
   for event in path:

       # launch a transition in our supervisor
       master_transition[event]._run(supervisor)
       events = ['camera', 'move_base', 'grab_obj', 'move_arm', 'check_box_pos', 'arm_box', 'put_obj']
       print(supervisor.current_state)
       val = supervisor.current_state.value
       slave_states = None
       slave_transition = None
       slave_path = None
       #for ev in events:
           # add slave
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
           start, path_a, i = animate_robot(model, start, path_a, i)
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
           start, path_a, i = animate_robot(model, start, path_a, i)
         
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
   print(path_a)
   plt.clf()
   time.sleep(10)

   model.animate(stances=path_a, frame_rate=30, unit='deg')

print('Supervisor done!')


