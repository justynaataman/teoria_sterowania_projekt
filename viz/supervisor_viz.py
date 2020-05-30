import networkx as nx
import matplotlib.pyplot as plt


def create_graph(visor):
    visor.add_edges_from([('wait', 'cam'), ('wait', 'move_b'), ('move_b', 'cam'),
                          ('cam', 'grab'), ('cam', 'move_a'), ('move_a', 'cam'),
                          ('grab', 'check_box_pos'), ('check_box_pos', 'move_b'), ('move_b', 'is_arm'),
                          ('check_box_pos', 'is_arm'), ('is_arm', 'move_a'), ('move_a', 'is_arm'),
                          ('is_arm', 'put_o'), ('put_o', 'wait')])
    pos = {
        'wait': (1, 10),
        'cam': (1, 5),
        'grab': (3, 5),
        'check_box_pos': (7, 5),
        'is_arm': (10, 5),
        'move_b': (5, 8),
        'move_a': (5, 1),
        'put_o': (10, 10)
    }
    return visor, pos



def show_path(stan1, stan2, visor):
    for path in nx.all_simple_paths(visor, source=stan1, target=stan2):
        print(path)


def update_graph(pos, visor, name= None):
    plt.clf()
    if name!= None:
        #val_map = {'wait': 0.0, name: 1.0, 'put_o': 0.8}
        val_map = {'wait': 'yellow', 'put_o': 'green',  name: 'red'}
    else:
        val_map={
            'wait': 'yellow',
            'put_o': 'green'
        }
    values = [val_map.get(node, 'blue') for node in visor.nodes()]
    nx.draw_networkx_nodes(visor, pos, cmap=plt.get_cmap('jet'),
                           node_color=values, node_size=1000)
    nx.draw_networkx_labels(visor, pos)
    nx.draw_networkx_edges(visor, pos, edge_color='r', arrows=True)
    nx.draw_networkx_edges(visor, pos, arrows=False)
    plt.ion()
    plt.show()
    plt.pause(0.1)

if __name__=='__main__':
    visor = nx.DiGraph()
    visor, pos = create_graph(visor)
    lista = list(visor.nodes)
    for element in lista:
        update_graph(pos, element)



