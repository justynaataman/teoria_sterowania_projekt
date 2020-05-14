from statemachine import StateMachine, State, Transition

options = [
    {"name": "start", "initial": True, "value": "start"},  # 0
    {"name": "get_cam_out", "initial": False, "value": "get_cam_out"},  # 1
    {"name": "obj_recognition", "initial": False, "value": "obj_recognition"},  # 2
    {"name": "return_false", "initial": False, "value": "return_false"},  # 3
    {"name": "return_true", "initial": False, "value": "return_true"} #4
]

camera_states = [State(**opt) for opt in options]

form_to = [
   [0, [1]],
   [1, [2]],
   [2, [3, 4]],
]
# create transitions for a master (as a dict)
camera_transitions = {}
for indices in form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(camera_states[from_idx], camera_states[to_idx], identifier=op_identifier)
        camera_transitions[op_identifier] = transition

        # add transition to source state
        camera_states[from_idx].transitions.append(transition)

#pachy
recon_obj = ["m_0_1", "m_1_2", "m_2_4"]
not_recon_obj = ["m_0_1", "m_1_2", "m_2_3"]

paths_camera = [recon_obj, not_recon_obj]
