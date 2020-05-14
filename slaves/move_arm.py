#setup automa
from statemachine import StateMachine, State, Transition

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "inv_kin", "initial": False, "value": "inv_kin"},  # 1
    {"name": "move", "initial": False, "value": "move"},  # 2
    {"name": "stop", "initial": False, "value": "stop"},  # 3
]

move_arm_states = [State(**opt) for opt in options]
 
form_to = [
   [0, [1]],
   [1, [2, 3]],
   [2, [3]],
]
 
move_arm_transitions = {}
for indices in form_to:
   from_idx, to_idx_tuple = indices  
   for to_idx in to_idx_tuple:  
       op_identifier = "m_{}_{}".format(from_idx, to_idx)  # 
       transition = Transition(move_arm_states[from_idx], move_arm_states[to_idx], identifier=op_identifier)
       move_arm_transitions[op_identifier] = transition
       move_arm_states[from_idx].transitions.append(transition)
 


 
#best opt
inv_kin_ok = ["m_0_1", "m_1_2", "m_2_3"]
#worse opt
singularity = ["m_0_1", "m_1_3"]

paths_move_arm = [singularity, inv_kin_ok]
 


