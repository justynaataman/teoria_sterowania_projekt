import networkx as nx
import matplotlib.pyplot as plt

def cam_viz():
    camera = nx.DiGraph()
    camera.add_edges_from([('start', 'get_camera_output'), ('get_camera_output', 'obj_recognition'), ('obj_recognition', 'return_true'), ('obj_recognition', 'return_false')])
    val_map = {'start': 0.4,
               'return_false': 0.6,
            'return_true': 0.6}
    values = [val_map.get(node, 0.25) for node in camera.nodes()]
    pos = nx.spring_layout(camera)
    nx.draw_networkx_nodes(camera, pos, cmap=plt.get_cmap('jet'),
                           node_color = values, node_size = 500)
    nx.draw_networkx_labels(camera, pos)
    nx.draw_networkx_edges(camera, pos, edge_color='r', arrows=True)
    nx.draw_networkx_edges(camera, pos,  arrows=False)
    plt.show()
