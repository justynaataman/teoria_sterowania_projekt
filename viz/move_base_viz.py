import networkx as nx
import matplotlib.pyplot as plt

move_base = nx.DiGraph()


move_base .add_edges_from([('start', 'check_engine'), ('check_engine', 'stop'), ('check_engine', 'moving'), ('moving', 'stop')])

val_map = {'start': 0.4,
           'stop': 0.6}

values = [val_map.get(node, 0.25) for node in move_base.nodes()]

pos = nx.spring_layout(move_base)
nx.draw_networkx_nodes(move_base , pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(move_base , pos)
nx.draw_networkx_edges(move_base , pos, edge_color='r', arrows=True)
nx.draw_networkx_edges(move_base , pos,  arrows=False)


plt.show()
