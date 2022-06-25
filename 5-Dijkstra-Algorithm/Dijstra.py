import WeightedGraph


class Dijstra:

    def __init__(self, G: WeightedGraph.WeightedGraph, s: int):
        self.G = G
        self.G.validate_vertex(s)
        self.s = s
        self.dis = [float("inf") for _ in range(self.G.V)]  # int array
        self.dis[s] = 0
        self.visited = [False for _ in range(self.G.V)]  # boolean array

        while True:
            cur_dis = float("inf")
            cur = -1
            for v in range(self.G.V):
                if self.visited[v] is False and self.dis[v] < cur_dis:
                    cur_dis = self.dis[v]
                    cur = v
            if cur == -1:
                break
            self.visited[cur] = True
            for w in self.G.adj_map(cur):
                if self.visited[w] is False:
                    if self.dis[cur] + self.G.weight_of(cur, w) < self.dis[w]:
                        self.dis[w] = self.dis[cur] + self.G.weight_of(cur, w)

    def is_connected_to(self, v: int):
        self.G.validate_vertex(v)
        return self.visited[v]

    def dis_to(self, v: int):
        self.G.validate_vertex(v)
        return self.dis[v]
