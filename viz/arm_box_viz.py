import networkx as nx
import matplotlib.pyplot as plt
def arm_box_viz():
    arm_box = nx.DiGraph()

    start = "start"
    get_arm_pose = "get_arm_pose"
    return_false = "return_false"
    return_true = "return_true"


    arm_box.add_edges_from([('start', 'get_arm_pose'), ('get_arm_pose', 'return_false'), ('get_arm_pose', 'return_true')])

    val_map = {'start': 0.4,
               'return_false': 0.6,
            'return_true': 0.6}

    values = [val_map.get(node, 0.25) for node in arm_box.nodes()]

    pos = nx.spring_layout(arm_box)
    nx.draw_networkx_nodes(arm_box, pos, cmap=plt.get_cmap('jet'),
                           node_color = values, node_size = 500)
    nx.draw_networkx_labels(arm_box, pos)
    nx.draw_networkx_edges(arm_box, pos, edge_color='r', arrows=True)
    nx.draw_networkx_edges(arm_box, pos,  arrows=False)


    plt.show()
