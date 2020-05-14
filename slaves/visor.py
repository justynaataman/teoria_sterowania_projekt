from statemachine import StateMachine, State, Transition

options = [
    {"name": "wait_for_xy", "initial": True, "value": "wait_for_xy"},  # 0
    {"name": "camera", "initial": False, "value": "camera"},  # 1
    {"name": "move base", "initial": False, "value": "move base"},  # 2
    {"name": "grab_obj", "initial": False, "value": "grab_obj"},  # 3
    {"name": "move_arm", "initial": False, "value": "move_arm"}, #4
    {"name": "check_box_pos", "initial": False, "value": "check_box_pos"}, #5
    {"name": "arm_box", "initial": False, "value": "arm_box"}, #6
    {"name": "put_obj", "initial": False, "value": "put_obj"}] #7
]

master_states = [State(**opt) for opt in options]

form_to = [
   [0, [1, 2]],
   [1, [3, 4]],
   [2, [1, 6]],
   [3, [5]],
   [4, [1, 6]],
   [5, [2, 6]],
   [6, [4, 7]],
   [7, [0]]
]

master_transition = {}
for indices in form_to:
   from_idx, to_idx_tuple = indices
   for to_idx in to_idx_tuple:
       op_identifier = "m_{}_{}".format(from_idx, to_idx)  #
       transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
       master_transitions[op_identifier] = transition
       master_states[from_idx].transitions.append(transition)

#pachy
path_1 = ["m_0_1", "m_1_3", "m_3_5", "m_5_6", "m_6_7", "m_7_0"]
#worse opt
path_2 = ["m_0_2", "m_2_1", "m_1_3", "m_3_5", "m_5_2”, "m_2_6", "m_6_4", "m_4_6", "m_6_7", "m_7_0"]
#
path_3 = ["m_0_1", "m_1_4", "m_4_1", "m_1_3", "m_3_5", "m_5_6", "m_6_4", "m_4_6", "m_6_7", "m_7_0"]
paths = [path_1, path_2, path_3]