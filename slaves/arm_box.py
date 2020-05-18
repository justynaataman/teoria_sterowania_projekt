#setup automa
from statemachine import StateMachine, State, Transition
from .funct import create_tr

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "get_arm_pose", "initial": False, "value": "get_arm_pose"},  # 1
    {"name": "return_false", "initial": False, "value": "return_false"},  # 2
    {"name": "return_true", "initial": False, "value": "return_true"},  # 3
]

arm_box_states = [State(**opt) for opt in options]
 
form_to = [
   [0, [1]],
   [1, [1, 2]],
   [2, [1, 3]],
]
 
arm_box_transitions = {}
arm_box_transitions, arm_box_states = create_tr(arm_box_transitions, arm_box_states, form_to)
"""
for indices in form_to:
   from_idx, to_idx_tuple = indices  
   for to_idx in to_idx_tuple:  
       op_identifier = "m_{}_{}".format(from_idx, to_idx)  # 
       transition = Transition(arm_box_states[from_idx], arm_box_states[to_idx], identifier=op_identifier)
       arm_box_transitions[op_identifier] = transition
       arm_box_states[from_idx].transitions.append(transition)
 """


 

#best opt
arm_pose_ok = ["m_0_1", "m_1_2"]
#worse opt
arm_pose_not_ok = ["m_0_1", "m_1_3"]

paths_arm_box = [arm_pose_ok, arm_pose_not_ok]
 


