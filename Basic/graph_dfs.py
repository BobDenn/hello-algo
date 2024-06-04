from graph_adjacency_list import GraphAdjList, Vertex


def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    """深度优先遍历DFS辅助函数"""
    res.append(vet) # 记录访问顶点
    visited.add(vet) # 标记该顶点已被访问
    # 遍历该顶点的所有邻接顶点
    for adjVet in graph.adj_list[vet]:
        if adjVet in visited:
            continue
        dfs(graph, visited, res, vet) # 递归访问顶点
