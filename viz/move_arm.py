import networkx as nx
import matplotlib.pyplot as plt

move_arm = nx.DiGraph()


move_arm .add_edges_from([('start', 'inverse_kinematics'), ('inverse_kinematics', 'move'), ('inverse_kinematics', 'stop'), ('move', 'stop')])

val_map = {'start': 0.4,
           'stop': 0.6}

values = [val_map.get(node, 0.25) for node in move_arm.nodes()]

pos = nx.spring_layout(move_arm)
nx.draw_networkx_nodes(move_arm , pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(move_arm , pos)
nx.draw_networkx_edges(move_arm , pos, edge_color='r', arrows=True)
nx.draw_networkx_edges(move_arm , pos,  arrows=False)


plt.show()
