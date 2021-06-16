from data_structures.stacks_and_queues.stacks_and_queues import Queue


class Vertex:
    """Vertex class
    """

    def __init__(self, val: any) -> None:
        self.val = val

    def __str__(self):
        return self.val

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val})'


class Edge:
    """Edge class
    """

    def __init__(self, vertex: Vertex, weight: int) -> None:
        self.vertex = vertex
        self.weight = weight


class Graph:
    """Graph class
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, val: any) -> Vertex:
        """Add a new vertex to the graph

        Args:
            val (any): Value of the new vertex

        Returns:
            Vertex: Successfully added vertex
        """
        vertex = Vertex(val)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start: Vertex, end: Vertex, weight: int = 1) -> None:
        """Add a new edge between 2 vertices

        Args:
            start (Vertex): Start vertex
            end (Vertex): End vertex
            weight (int, optional): Edge weight. Defaults to 1.

        Raises:
            KeyError: If start vertex not in the graph
            KeyError: If end vertex not in the graph
        """
        if start not in self.adjacency_list:
            raise KeyError('Start Vertex is not in the Graph')
        if end not in self.adjacency_list:
            raise KeyError('End Vertex is not in the Graph')

        edge = Edge(end, weight)
        adjacencies = self.adjacency_list[start]
        adjacencies.append(edge)

    def get_nodes(self) -> set:
        """Get all graph vertices

        Returns:
            set: Set of vertices that are part of the graph
        """
        return set(self.adjacency_list.keys())

    def get_neighbors(self, vertex: Vertex) -> list:
        """Get a list of vertices that are connected to the provided vertex

        Args:
            vertex (Vertex): Vertex

        Raises:
            KeyError: If provided vertex is not part of the graph

        Returns:
            list: list of objects that contain vertex object and edge weight
        """
        if not vertex in self.adjacency_list:
            raise KeyError('Given Vertex is not in the Graph')

        edges = self.adjacency_list[vertex]

        return [{'vertex': edge.vertex,
                 'weight': edge.weight} for edge in edges]

    def breadth_first(self, start: Vertex) -> set:
        """Traverse a graph in breadth-first manner and return a set of Vertices

        Args:
            start (Vertex): Starting point of the traversal

        Raises:
            KeyError: If provided vertex is not part of the graph

        Returns:
            set: Set of vertices
        """
        q = Queue()
        output = set()

        if not start in self.adjacency_list:
            raise KeyError('Given Vertex is not part of the Graph')

        q.enqueue(start)

        while not q.is_empty():
            vertex = q.dequeue()
            output.add(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor['vertex'] not in output:
                    q.enqueue(neighbor['vertex'])

        return output

    def pre_order(self, start: Vertex, output: set = None) -> set:
        if output is None:
            output = set()

        if start in self.adjacency_list:
            output.add(start)
        else:
            raise KeyError('Given Vertex is not part of the Graph')

        for edge in self.adjacency_list[start]:
            output = self.pre_order(edge.vertex, output)

        return output

    def size(self) -> int:
        """Get the size of the graph

        Returns:
            int: Number of vertices in the graph
        """
        return len(self.get_nodes())
