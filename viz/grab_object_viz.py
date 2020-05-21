import networkx as nx
import matplotlib.pyplot as plt

grab_obj = nx.DiGraph()


grab_obj.add_edges_from([('start', 'close_gripper'), ('close_gripper', 'end'), ('close_gripper', 'end_with_failure')])

val_map = {'start': 0.4,
           'end': 0.6, 
	   'end_with_failure': 0.6}

values = [val_map.get(node, 0.25) for node in grab_obj.nodes()]

pos = nx.spring_layout(grab_obj)
nx.draw_networkx_nodes(grab_obj, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(grab_obj, pos)
nx.draw_networkx_edges(grab_obj, pos, edge_color='r', arrows=True)
nx.draw_networkx_edges(grab_obj, pos,  arrows=False)


plt.show()
