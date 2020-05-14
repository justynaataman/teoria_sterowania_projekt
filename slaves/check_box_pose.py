#setup automa
from statemachine import StateMachine, State, Transition

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "get_base_pose", "initial": False, "value": "get_base_pose"},  # 1
    {"name": "return_false", "initial": False, "value": "return_false"},  # 2
    {"name": "return_true", "initial": False, "value": "return_true"},  # 3
]

check_box_pose_states = [State(**opt) for opt in options]
 
form_to = [
   [0, [1]],
   [1, [1, 2]],
   [2, [1, 3]],
]
 
check_box_pose_transitions = {}
for indices in form_to:
   from_idx, to_idx_tuple = indices  
   for to_idx in to_idx_tuple:  
       op_identifier = "m_{}_{}".format(from_idx, to_idx)  # 
       transition = Transition(check_box_pose_states[from_idx],check_box_pose_states[to_idx], identifier=op_identifier)
       check_box_pose_transitions[op_identifier] = transition
       check_box_pose_states[from_idx].transitions.append(transition)
 


 
#best opt
base_pose_ok = ["m_0_1", "m_1_2"]
#worse opt
base_pose_not_ok = ["m_0_1", "m_1_3"]

paths_check_box_pos = [base_pose_ok, base_pose_not_ok]
 


