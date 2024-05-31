class Vertex:
    """顶点类"""
    def __init__(self, val) -> None:
        self.value: int = val
        
    def __str__(self):
        """返回一个用户友好的字符串表示"""
        return f"Vertex({self.value})"
    
    def __repr__(self):
        """返回一个正式的字符串表示"""
        return f"Vertex({self.value})"

    def __eq__(self, other) -> bool:
        """定义顶点的比较方法"""
        if isinstance(other, Vertex):
            return self.value == other.value
        return False

    def __hash__(self):
        """定义顶点的哈希方法, 以便在集合和字典中使用"""
        return hash(self.value)    


class GraphAdjList:
    """ 基于邻接表实现的无向图类 """

    def __init__(self, edges: list[list[Vertex]]):
        """构造方法"""
        self.adj_list: dict[Vertex, list[Vertex]] = {}
        for edge in edges:
            self.add_edge(edge[0], edge[1])
            
    def size(self):        
        return len(self.adj_list)
    
    def add_edge(self, vet1: Vertex, vet2: Vertex):
        """添加一条无向边"""
        if vet1 == vet2:
            raise IndexError("不能连接顶点自身")
        self.add_vertex(vet1)
        self.add_vertex(vet2)
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)
        
    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        """移除一条无向边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError("顶点不在图中")
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)
            
    def add_vertex(self, vet: Vertex):
        """添加一个顶点"""
        if vet in self.adj_list:
            return
        self.adj_list[vet] = []
        
    def remove_vertex(self, vet: Vertex):
        """移除一个顶点"""
        if vet not in self.adj_list:
            raise ValueError()
        # 删除顶点
        self.adj_list.pop(vet)
         #遍历其他顶点的链表，删除所有包含vet的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)
                
    def print_adj_list(self):
        """打印邻接表"""
        print("邻接表= ")
        for vertex in self.adj_list:
            adjacent_vertices = [v.value for v in self.adj_list[vertex]]
            print(f"{vertex.value}: {adjacent_vertices},")
            
            
if __name__ == "__main__":
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    edges = [[v1, v2], [v2, v3], [v3, v4], [v4, v5], [v5, v1]]
    graph = GraphAdjList(edges)
    graph.print_adj_list()
    