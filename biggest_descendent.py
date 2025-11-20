def biggest_descendent(graph, root, value):

    biggest = {}

    def dfs(u):
        max_val = value[u]

        for v in graph.neighbors(u):
            child_max = dfs(v)
            if child_max > max_val:
                max_val = child_max

        biggest[u] = max_val
        return max_val

    dfs(root)
    return biggest