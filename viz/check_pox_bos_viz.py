import networkx as nx
import matplotlib.pyplot as plt

check_box_pos = nx.DiGraph()



check_box_pos.add_edges_from([('start', 'get_base_pose'), ('get_base_pose', 'return_false'), ('get_base_pose', 'return_true')])

val_map = {'start': 0.4,
           'return_false': 0.6, 
	    'return_true': 0.6}

values = [val_map.get(node, 0.25) for node in check_box_pos.nodes()]

pos = nx.spring_layout(check_box_pos)
nx.draw_networkx_nodes(check_box_pos, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(check_box_pos, pos)
nx.draw_networkx_edges(check_box_pos, pos, edge_color='r', arrows=True)
nx.draw_networkx_edges(check_box_pos, pos,  arrows=False)


plt.show()
