import networkx as nx
import matplotlib.pyplot as plt

visor = nx.DiGraph()
"""
arm_box = nx.MultiGraph()
camera = nx.MultiGraph()
check_box_pose = nx.MultiGraph()
grab_obj = nx.MultiGraph()
move_arm = nx.MultiGraph()
move_base = nx.MultiGraph()
put_obj = nx.MultiGraph()
"""
wait = "wait for xy"
cam = "camera"
grab = "grab obj"
move_b = "move base"
move_a = "move arm"
check_box_pos = "check box pos"
arm_b = "is arm over box"
put_o = "put obj"

visor.add_edges_from([('wait', 'cam'), ('cam', 'grab'), ('grab', 'check_box_pos'),
                      ('check_box_pos', 'arm_b'), ('check_box_pos', 'move_b'),
     ('cam', 'move_a'), ('move_b', 'cam'), ('move_b', 'arm_b'), ('arm_b', 'put_o'),
                      ('wait', 'move_b'), ('move_a', 'cam'), ('arm_a', 'arm_b'),
                      ('arm_b', 'move_a'), ('put_o', 'wait')])

val_map = {'wait': 0.4,
           'put_o': 0.6}

values = [val_map.get(node, 0.25) for node in visor.nodes()]

pos = nx.spring_layout(visor)
nx.draw_networkx_nodes(visor, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(visor, pos)
nx.draw_networkx_edges(visor, pos, edge_color='r', arrows=True)
nx.draw_networkx_edges(visor, pos,  arrows=False)
plt.show()