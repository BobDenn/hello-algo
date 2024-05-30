class Vertex:
    """顶点类"""
    def __init__(self, val) -> None:
        self.value = val


class GraphAdjList:
    """ 基于邻接表实现的无向图类 """

    def __init__(self, edges: list[list[Vertex]]):
        """构造方法"""
        self.adj_list: dict[Vertex, list[Vertex]] = {}
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])
            
    def size(self):        
        return len(self.adj_list)
    
    def add_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise IndexError()
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)
        
    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise IndexError()
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)
            
    def add_vertex(self, vet: Vertex):            
        if vet in self.adj_list:
            return
        self.adj_list[vet] = []
        
    def remove_vertex(self, vet: Vertex):
        if vet not in self.adj_list:
            raise ValueError()
        # 删除顶点
        self.adj_list.pop(vet)
         #遍历其他顶点的链表，删除所有包含vet的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)
                
    def print(self):
        print("邻接表= ")
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f"{vertex.val}: {tmp},")
            