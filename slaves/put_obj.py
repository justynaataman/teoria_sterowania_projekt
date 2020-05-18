#setup automa
from statemachine import StateMachine, State, Transition
from .funct import create_tr

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "open_gripper", "initial": False, "value": "open_gripper"},  # 1
]

put_obj_states = [State(**opt) for opt in options]
 
form_to = [
   [0, [1]],
]
 
put_obj_transitions = {}
put_obj_transitions, put_obj_states = create_tr(put_obj_transitions, put_obj_states, form_to)
"""
for indices in form_to:
   from_idx, to_idx_tuple = indices  
   for to_idx in to_idx_tuple:  
       op_identifier = "m_{}_{}".format(from_idx, to_idx)  # 
       transition = Transition(put_obj_states[from_idx], put_obj_states[to_idx], identifier=op_identifier)
       put_obj_transitions[op_identifier] = transition
       put_obj_states[from_idx].transitions.append(transition)
"""


 
#best opt
put_obj = ["m_0_1"]
paths_put_obj = [put_obj]
 


