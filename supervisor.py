#setup automa
from statemachine import StateMachine, State, Transition

options = [
    {"name": "wait_for_xy", "initial": True, "value": "wait_for_xy"},  # 0
    {"name": "camera", "initial": False, "value": "camera"},  # 1
    {"name": move base", "initial": False, "value": "move base"},  # 2
    {"name": "grab_obj", "initial": False, "value": "grab_obj"},  # 3
    {"name": "move_arm", "initial": False, "value": "move_arm"}, #4
    {"name": "check_box_pos", "initial": False, "value": "check_box_pos"}, #5
    {"name": "arm_box", "initial": False, "value": "arm_box"}, #6
    {"name": "put_obj", "initial": False, "value": "put_obj"}] #7

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
 
 
 
 
 
 
 


# create a generator class
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
path_1 = ["m_0_1", "m_1_3", "m_3_5", "m_5_6", "m_6_7", “m_7_0”]
#worse opt
path_2 = ["m_0_2", "m_2_1", "m_1_3", "m_3_5", “m_5_2”, “m_2_6”, “m_6_4”, “m_4_6”, “m_6_7”, “m_7_0”]
#
path_3 = ["m_0_1", "m_1_4", "m_4_1", "m_1_3", “m_3_5”, “m_5_6”, “m_6_4”, “m_4_6”, “m_6_7”, “m_7_0”]
paths = [path_1, path_2, path_3]
 
for path in paths:
 
   # create a supervisor
   supervisor = Generator.create_master(master_states, master_transitions)
   print('\n' + str(supervisor))
 
   # run supervisor for exemplary path
   print("Executing path: {}".format(path))
   for event in path:
 
       # launch a transition in our supervisor
       master_transitions[event]._run(supervisor)
       print(supervisor.current_state)
 
       # add slave
       if supervisor.current_state.value == "camera":
          
       if supervisor.current_state.value == "move_base":
           # TODO: automata 2 (for) slave2
           ...
 
       if supervisor.current_state.value == "grab_obj":
           # TODO: automata 3 (for) slave3
           ...
 
       if supervisor.current_state.value == "move_arm":
           # TODO: automata 3 (for) slave3
           …
     if supervisor.current_state.value == "check_box_pos”:
           # TODO: automata 3 (for) slave3
           ...
     if supervisor.current_state.value == "arm_box":
           # TODO: automata 3 (for) slave3
           ...
     if supervisor.current_state.value == "put_obj":
           # TODO: automata 3 (for) slave3
           ...
 
           print("Supervisor done!")


