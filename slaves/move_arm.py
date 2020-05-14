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
 
   # method of creating objects in a flexible way (we can define multiple functions
   # which will create objects in different ways)
   @classmethod
   def create_master(cls, states, transitions) -> 'Generator':
       return cls(states, transitions)
 
#best opt
inv_kin_ok = ["m_0_1", "m_1_2", "m_2_3"]
#worse opt
singularity = ["m_0_1", "m_1_3"]

paths_move_arm = [singularity, inv_kin_ok]
 


