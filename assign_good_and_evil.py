import dsc40graph

def assign_good_and_evil(graph: dsc40graph.UndirectedGraph):

    #contains good / evil
    label_map = {}
    #helper
    def opposite(label):
        return 'evil' if label == 'good' else 'good'

    for start in graph.nodes:
        if start in label_map:
            continue

        label_map[start] = 'good'
        stack = [start]

        while stack:
            u = stack.pop()
            u_label = label_map[u]

            for v in graph.neighbors(u):
                if v not in label_map:
                    label_map[v] = opposite(u_label)
                    stack.append(v)
                else:
                    if label_map[v] == u_label:
                        return None

    return label_map

