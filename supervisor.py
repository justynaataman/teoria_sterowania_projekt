#setup automa
from statemachine import StateMachine, State, Transition
from slaves.arm_box import *
from slaves.camera import *
from slaves.check_box_pose import *
from slaves.grab_obj import *
from slaves.move_arm import *
from slaves.move_base import *
from slaves.put_obj import *
from slaves.visor import *
import Generator



 
for path in paths:
 
   # create a supervisor
   supervisor = Generator.create_master(master_states, master_transition)
   print('\n' + str(supervisor))
 
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
           slave_states = camera_states
           slave_transition = camera_transitions
           slave_path = paths_camera
       if val == "move_base":
           #TODO: automata 2 (for) slave2
           slave_states = move_base_states
           slave_transition = move_base_transitions
           slave_path = paths_move_base
           print("move base")
       if val == "grab_obj":
               # TODO: automata 3 (for) slave3
           print("grab obj")
           slave_states = grab_obj_states
           slave_path = paths_grab_obj
           slave_transition = grab_obj_transitions
       if val == "move_arm":
            # TODO: automata 3 (for) slave3
            slave_transition = move_arm_transitions
            slave_states = move_arm_states
            slave_path = paths_move_arm
            print("move arm")
       if val == 'check_box_pos':
               # TODO: automata 3 (for) slave3
            slave_transition = check_box_pose_transitions
            slave_states = check_box_pose_states
            slave_path = paths_check_box_pos
            print("check box pos")
       if val == "arm_box":
               # TODO: automata 3 (for) slave3
            slave_transition = arm_box_transitions
            slave_states = arm_box_states
            slave_path = paths_arm_box
            print("arm box")
       if val == "put_obj":
            # TODO: automata 3 (for) slave3
            slave_transition = put_obj_transitions
            slave_states = put_obj_states
            slave_path = paths_put_obj
            print('put obj')
       #create slave automata
       print('automata')
       if slave_states is not None:
           slave = Generator.create_master(slave_states, slave_transition)
           #for now first path
           ss = slave_path[0]
           for x in ss:
               slave_transition[x]._run(slave)
               print(slave.current_state)




 
print('Supervisor done!')


