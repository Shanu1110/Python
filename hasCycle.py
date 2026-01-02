def hasCycle(graph):
    visited = set()
    recStack = set()

    def dfs(v):
        visited.add(v)
        recStack.add(v)

        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recStack:
                return True

        recStack.remove(v)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False