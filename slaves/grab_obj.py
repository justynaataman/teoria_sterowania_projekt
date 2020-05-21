from statemachine import StateMachine, State, Transition
from .funct import create_tr

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "close_gripper", "initial": False, "value": "close_gripper"},  # 1
    {"name": "end", "initial": False, "value": "end"},  # 2
 
]

grab_obj_states = [State(**opt) for opt in options]

form_to = [
   [0, [1]],
   [1, [2]],
]

# create transitions for a master (as a dict)
grab_obj_transitions = {}
grab_obj_transitions, grab_obj_states = create_tr(grab_obj_transitions, grab_obj_states, form_to)
"""
for indices in form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(grab_obj_states[from_idx], grab_obj_states[to_idx], identifier=op_identifier)
        grab_obj_transitions[op_identifier] = transition

        # add transition to source state
        grab_obj_states[from_idx].transitions.append(transition)
"""

grab = ["m_0_1", "m_1_2"]


paths_grab_obj = [grab]
