from statemachine import StateMachine, State, Transition


def create_tr(arm_box_transitions, arm_box_states, form_to):
    for indices in form_to:
       from_idx, to_idx_tuple = indices
       for to_idx in to_idx_tuple:
           op_identifier = "m_{}_{}".format(from_idx, to_idx)  #
           transition = Transition(arm_box_states[from_idx], arm_box_states[to_idx], identifier=op_identifier)
           arm_box_transitions[op_identifier] = transition
           arm_box_states[from_idx].transitions.append(transition)
    return arm_box_transitions, arm_box_states