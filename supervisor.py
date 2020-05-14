#setup automa
from statemachine import StateMachine, State, Transition
from slaves.arm_box import *
from slaves.camera import *
from slaves.check_box_pose import *
from slaves.grab_obj import *
from slaves.move_arm import *
from slaves.move_base import *
from slaves.put_obj import *
from Generator import generator



 
for path in paths:
 
   # create a supervisor
   supervisor = Generator.create_master(master_states, master_transitions)
   print('\n' + str(supervisor))
 
   # run supervisor for exemplary path
   print("Executing path: {}".format(path))
   for event in path:
 
       # launch a transition in our supervisor
       master_transitions[event]._run(supervisor)
       print(supervisor.current_state)
 
       # add slave
       if supervisor.current_state.value == "camera":
          
       if supervisor.current_state.value == "move_base":
           # TODO: automata 2 (for) slave2
           ...
 
       if supervisor.current_state.value == "grab_obj":
           # TODO: automata 3 (for) slave3
           ...
 
       if supervisor.current_state.value == "move_arm":
           # TODO: automata 3 (for) slave3
           …
     if supervisor.current_state.value == "check_box_pos”:
           # TODO: automata 3 (for) slave3
           ...
     if supervisor.current_state.value == "arm_box":
           # TODO: automata 3 (for) slave3
           ...
     if supervisor.current_state.value == "put_obj":
           # TODO: automata 3 (for) slave3
           ...
 
           print("Supervisor done!")


