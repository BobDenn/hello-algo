import collections
from graph_adjacency_list import GraphAdjList, Vertex


def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[int]:
    """广度优先遍历"""
    res = []
    visited = set([start_vet])
    # 队列用于实现 BFS
    que = collections.deque([start_vet])
    while len(que) > 0:
        vet = que.popleft() # 队首顶点出队
        res.append(vet.value) # 记录访问顶点
        # 遍历该顶点的所有邻接顶点
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue
            que.append(adj_vet)
            visited.add(adj_vet)
    return res


if __name__ == "__main__":
    v0 = Vertex(0)
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)
    v7 = Vertex(7)
    v8 = Vertex(8)
    
    edges = [
        [v0, v1], [v0, v3], [v1, v0], [v1, v4], [v1, v2], 
        [v2, v1], [v2, v5], [v3, v0], [v3, v4], [v3, v6], 
        [v4, v3], [v4, v1], [v4, v5], [v4, v7], [v5, v4], 
        [v5, v2], [v5, v8], [v6, v3], [v6, v7], [v7, v6], 
        [v7, v4], [v7, v8], [v8, v7], [v8, v5]
    ]
    
    graph = GraphAdjList(edges)
    res = graph_bfs(graph, v0)
    print(f"广度优先遍历的结果: {res}")
    