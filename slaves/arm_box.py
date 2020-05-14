#setup automa
from statemachine import StateMachine, State, Transition

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
for indices in form_to:
   from_idx, to_idx_tuple = indices  
   for to_idx in to_idx_tuple:  
       op_identifier = "m_{}_{}".format(from_idx, to_idx)  # 
       transition = Transition(arm_box_states[from_idx], arm_box_states[to_idx], identifier=op_identifier)
       arm_box_transitions[op_identifier] = transition
       arm_box_states[from_idx].transitions.append(transition)
 

class Generator(StateMachine):
   states = []
   transitions = []
   states_map = {}
   current_state = None
 
   def __init__(self, states, transitions):
 
       # creating each new object needs clearing its variables (otherwise they're duplicated)
       self.states = []
       self.transitions = []
       self.states_map = {}
       self.current_state = states[0]
 
       # create fields of states and transitions using setattr()
       # create lists of states and transitions
       # create states map - needed by StateMachine to map states and its values
       for s in states:
           setattr(self, str(s.name).lower(), s)
           self.states.append(s)
           self.states_map[s.value] = str(s.name)
 
       for key in transitions:
           setattr(self, str(transitions[key].identifier).lower(), transitions[key])
           self.transitions.append(transitions[key])
 
       # super() - allows us to use methods of StateMachine in our Generator object
       super(Generator, self).__init__()
 
   # define a printable introduction of a class
   def __repr__(self):
       return "{}(model={!r}, state_field={!r}, current_state={!r})".format(
           type(self).__name__, self.model, self.state_field,
           self.current_state.identifier,
       )
 

#best opt
arm_pose_ok = ["m_0_1", "m_1_2"]
#worse opt
arm_pose_not_ok = ["m_0_1", "m_1_3"]

paths_arm_box = [arm_pose_ok, arm_pose_not_ok]
 


