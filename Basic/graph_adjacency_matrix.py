class GraphAdjMat:
    """
    基于邻接矩阵实现的无向图类, 适用于顶点少,边数多的稠密图
    """
    def __init__(self, vertices: list[int], edges: list[list[int]]) -> None:
        # vertices
        self.vertices = []
        # adjacency matrix
        self.adj_mat = []
        # add vertices
        for val in vertices:
            self.add_vertex(val)
        # add edges
        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self) -> int:
        return len(self.vertices)
    
    def add_vertex(self, val: int):
        n = self.size()
        self.vertices.append(val)
        new_row = [0] * n
        self.adj_mat.append(new_row)
        for row in self.adj_mat:
            row.append(0)
            
    def remove_vertex(self, index: int):
        if index >= self.size():
            raise IndexError("索引溢出")
        self.vertices.pop(index)
        self.adj_mat.pop(index)
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
    
    def remove_edge(self, i: int, j: int):
        if i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0
    
    def print_matrix(self):    
        print(" 顶点列表 = ", self.vertices)
        print(" 邻接矩阵 = ")
        for row in self.adj_mat:
            print(row)
            
            
if __name__ == '__main__':
    vertices = [0, 1, 2, 3]
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    graph = GraphAdjMat(vertices, edges)
    graph.print_matrix()
    