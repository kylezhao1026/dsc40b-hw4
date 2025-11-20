def cluster(graph, weights, level):
    visited = set()
    clusters = []

    for start in graph.nodes:
        if start in visited:
            continue

        stack = [start]
        component = set()

        while stack:
            u = stack.pop()
            if u in visited:
                continue

            visited.add(u)
            component.add(u)

            for v in graph.neighbors(u):
                if v not in visited and weights(u, v) >= level:
                    stack.append(v)

        clusters.append(frozenset(component))

    return frozenset(clusters)
