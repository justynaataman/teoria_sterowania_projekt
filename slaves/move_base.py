from statemachine import StateMachine, State, Transition
from .funct import create_tr

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "check_engine", "initial": False, "value": "check_engine"},  # 1
    {"name": "moving", "initial": False, "value": "moving"},  # 2
    {"name": "stop", "initial": False, "value": "stop"},  # 3
    {"name": "stop_awaria", "initial": False, "value": "awaria"} #4
]

move_base_states = [State(**opt) for opt in options]

form_to = [
   [0, [1]],
   [1, [2, 4]],
   [2, [3]],
]

# create transitions for a master (as a dict)
move_base_transitions = {}
move_base_transitions, move_base_states = create_tr(move_base_transitions, move_base_states, form_to)
"""
for indices in form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(move_base_states[from_idx], move_base_states[to_idx], identifier=op_identifier)
        move_base_transitions[op_identifier] = transition

        # add transition to source state
        move_base_states[from_idx].transitions.append(transition)
"""
#patchs
moving = ["m_0_1", "m_1_2", "m_2_3"]
failure= ["m_0_1", "m_1_4"]

paths_move_base = [moving, failure]

