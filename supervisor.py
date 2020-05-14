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
from Generator import generator



 
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
       #for ev in events:

           # add slave
       if val == "camera":
          print("cam")

       if val == "move_base":
           #TODO: automata 2 (for) slave2
           print("move base")

       if val == "grab_obj":
               # TODO: automata 3 (for) slave3
           print("grab obj")

       if val == "move_arm":
               # TODO: automata 3 (for) slave3
            print("move arm")
       if val == 'check_box_pos':
               # TODO: automata 3 (for) slave3
            print("check box pos")
       if val == "arm_box":
               # TODO: automata 3 (for) slave3
            print("arm box")
       if val == "put_obj":
               # TODO: automata 3 (for) slave3
            print("put obj")

 
print('Supervisor done!')


