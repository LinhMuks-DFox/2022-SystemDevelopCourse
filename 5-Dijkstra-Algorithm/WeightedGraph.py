class WeightedGraph:

    def __init__(self, graph_path: str):
        self.V = None
        self.E = None
        with open(graph_path, "r") as graph_meta:
            self.V, self.E = (int(s) for s in graph_meta.readline().split())
            if self.V < 0:
                raise ValueError("V must be non-negative")

            if self.E < 0:
                raise ValueError("E must be non-negative")

            # (key : weight)
            self.adj = [dict() for _ in range(self.V)]

            for line in graph_meta:
                a, b, v = (int(s) for s in line.split())
                if a == b:
                    raise ValueError("Self Loop is Detected!")

                if b in self.adj[a]:
                    raise ValueError("Parallel Edges are Detected!")

                self.adj[a][b] = v
                self.adj[b][a] = v

    def validate_vertex(self, v: int):
        if v < 0 or v >= self.V:
            raise ValueError(f"Vertex {v} is invalid.")

    def adj_map(self, v: int):
        self.validate_vertex(v)
        return self.adj[v].keys()

    def weight_of(self, v: int, w: int):
        if self.has_edge(v, w):
            return self.adj[v][w]
        raise ValueError(f"No edge of {v}, {w}")
    def __repr__(self) -> str:
        return f"WeightedGraph V:{self.V} E: {self.E}"

    def __str__(self):
        sb = f"V: {self.V}, E: {self.E}\n"
        for index, ads_map in enumerate(self.adj):
            sb += f"{index} : "
            for key, value in ads_map.items():
                sb += f"{key}: {value} "
            sb += "\n"

        return sb

    def has_edge(self, v: int, w: int) -> bool:
        self.validate_vertex(v)
        self.validate_vertex(w)
        return w in self.adj[v]

    def degree(self, v: int) -> int:
        self.validate_vertex(v)
        return len(self.adj[v])
