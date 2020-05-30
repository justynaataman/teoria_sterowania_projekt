import networkx as nx
import matplotlib.pyplot as plt

def put_o_viz():
    put_obj = nx.DiGraph()
    put_obj.add_edges_from([('start', 'open_gripper')])
    val_map = {'start': 0.4,
               'open_gripper': 0.6}
    values = [val_map.get(node, 0.25) for node in put_obj.nodes()]
    pos = nx.spring_layout(put_obj)
    nx.draw_networkx_nodes(put_obj, pos, cmap=plt.get_cmap('jet'),
                           node_color = values, node_size = 500)
    nx.draw_networkx_labels(put_obj, pos)
    nx.draw_networkx_edges(put_obj, pos, edge_color='r', arrows=True)
    nx.draw_networkx_edges(put_obj, pos,  arrows=False)
    plt.show()
