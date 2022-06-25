from dataclasses import dataclass
from queue import PriorityQueue

import WeightedGraph


@dataclass(order=True)
class Node:
    dis: int
    v: int


class Dijstra:

    def __init__(self, G: WeightedGraph.WeightedGraph, s: int):
        self.G = G
        self.G.validate_vertex(s)
        self.s = s
        self.dis = [65536 for _ in range(self.G.V)]  # int array
        self.pre = [-1 for _ in range(self.G.V)]
        self.dis[s] = 0
        self.pre[s] = s
        self.visited = [False for _ in range(self.G.V)]  # boolean array

        pq = PriorityQueue()
        pq.put_nowait(Node(v=s, dis=0))

        while pq.empty() is False:
            cur = pq.get_nowait().v
            if self.visited[cur]:
                continue
            self.visited[cur] = True

            for w in self.G.adj_map(cur):
                if self.visited[w] is False:
                    if self.dis[cur] + self.G.weight_of(cur, w) < self.dis[w]:
                        self.dis[w] = self.dis[cur] + self.G.weight_of(cur, w)
                        pq.put_nowait(Node(v=w, dis=self.dis[w]))
                        self.pre[w] = cur

    def is_connected_to(self, v: int):
        self.G.validate_vertex(v)
        return self.visited[v]

    def dis_to(self, v: int):
        self.G.validate_vertex(v)
        return self.dis[v]

    def get_path(self, t: int)->list:
        ret = []
        if self.is_connected_to(t) is False:
            return ret
        cur = t
        while cur != self.s:
            ret.append(cur)
            cur = self.pre[cur]
        ret.append(self.s)
        ret.reverse()
        return ret
