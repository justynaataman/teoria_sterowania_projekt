from statemachine import StateMachine, State, Transition

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "close_gripper", "initial": False, "value": "close_gripper"},  # 1
    {"name": "end", "initial": False, "value": "end"},  # 2
    {"name": "end_failure", "initial": False, "value": "end_failure"},  # 3
]

master_states = [State(**opt) for opt in options] 

# create transitions for a master (as a dict)
master_transitions = {}
for indices in form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
        master_transitions[op_identifier] = transition

        # add transition to source state
        master_states[from_idx].transitions.append(transition)

#pachy
grab = ["m_0_1", "m_1_2"]
grab_failure = ["m_0_1", "m_1_3"]

paths_grab_obj = [recon_obj, not_recon_obj]
