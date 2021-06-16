import pytest
from data_structures.graph.graph import Edge, Graph, Vertex


class TestGraph:
    def test_proof_of_life(self):
        graph = Graph()
        assert graph

    @pytest.fixture
    def graph(self):
        return Graph()

    def test_add_vertex(self, graph):
        vertex = graph.add_vertex('test_val')
        assert vertex.val == 'test_val'

    def test_add_edge(self, graph):
        start = graph.add_vertex('start_vertex')
        end = graph.add_vertex('end_vertex')
        graph.add_edge(start, end)

        assert graph.adjacency_list[start][0].vertex == end

    def test_add_edge_test_size(self, graph):
        start = graph.add_vertex('start_vertex')
        end = graph.add_vertex('end_vertex')
        graph.add_edge(start, end)

        assert len(graph.adjacency_list) == 2

    def test_get_nodes(self, graph):
        vertex_1 = graph.add_vertex('test_1')
        vertex_2 = graph.add_vertex('test_2')
        vertex_3 = graph.add_vertex('test_3')

        expected = set([vertex_1, vertex_2, vertex_3])
        actual = graph.get_nodes()

        assert actual == expected

    def test_get_neighbors(self, graph):
        vertex_1 = graph.add_vertex('test_1')
        vertex_2 = graph.add_vertex('test_2')
        vertex_3 = graph.add_vertex('test_3')
        graph.add_edge(vertex_1, vertex_2, 5)
        graph.add_edge(vertex_1, vertex_3, 8)

        expected = [
            {'vertex':   vertex_2,
             'weight':   5},
            {'vertex':  vertex_3,
             'weight':   8}
        ]
        actual = graph.get_neighbors(vertex_1)

        assert actual == expected

    def test_size(self, graph):
        vertex_1 = graph.add_vertex('test_1')
        vertex_2 = graph.add_vertex('test_2')
        vertex_3 = graph.add_vertex('test_3')

        assert graph.size() == 3

    def test_one_node_graph(self, graph):
        vertex = graph.add_vertex('test')
        graph.add_edge(vertex, vertex)

        assert graph.get_nodes() == set([vertex])
        assert graph.size() == 1
        assert graph.get_neighbors(vertex) == [
            {'vertex': vertex,
             'weight': 1},
        ]

    def test_empty_graph(self, graph):
        assert graph.get_nodes() == set()
        assert graph.size() == 0

    def test_breadth_first(self, graph):
        vertex_1 = graph.add_vertex('test_1')
        vertex_2 = graph.add_vertex('test_2')
        vertex_3 = graph.add_vertex('test_3')
        vertex_4 = graph.add_vertex('test_4')
        vertex_5 = graph.add_vertex('test_5')
        vertex_6 = graph.add_vertex('test_6')

        graph.add_edge(vertex_1, vertex_2)
        graph.add_edge(vertex_2, vertex_3)
        graph.add_edge(vertex_2, vertex_4)
        graph.add_edge(vertex_3, vertex_4)
        graph.add_edge(vertex_3, vertex_5)
        graph.add_edge(vertex_3, vertex_6)
        graph.add_edge(vertex_4, vertex_5)
        graph.add_edge(vertex_5, vertex_6)

        """
        (1) --- (2)
               /    \
             (3) --- (4)
            /   \   /
           (6)---(5)
        """

        expected = set([vertex_1, vertex_2, vertex_3,
                        vertex_4, vertex_6, vertex_5])
        actual = graph.breadth_first(vertex_1)

        assert actual == expected

    def test_preorder(self, graph):
        vertex_1 = graph.add_vertex('A')
        vertex_2 = graph.add_vertex('B')
        vertex_3 = graph.add_vertex('C')
        vertex_4 = graph.add_vertex('D')
        vertex_5 = graph.add_vertex('E')
        vertex_6 = graph.add_vertex('F')
        vertex_7 = graph.add_vertex('G')
        vertex_8 = graph.add_vertex('H')

        graph.add_edge(vertex_1, vertex_2)
        graph.add_edge(vertex_1, vertex_4)
        graph.add_edge(vertex_2, vertex_4)
        graph.add_edge(vertex_2, vertex_3)
        graph.add_edge(vertex_3, vertex_7)
        graph.add_edge(vertex_4, vertex_5)
        graph.add_edge(vertex_4, vertex_8)
        graph.add_edge(vertex_4, vertex_6)
        graph.add_edge(vertex_6, vertex_8)

        """
        (A) --- (D) --- (F)
           \  /  |  \  /
            (B) (E)  (H)
             |
            (C)
             |
            (G)
        """
        # Expected output: A, B, C, G, D, E, H, F
        expected = set([vertex_1, vertex_2, vertex_3,
                        vertex_6, vertex_4, vertex_5, vertex_8, vertex_7])
        actual = graph.pre_order(vertex_1)

        assert actual == expected
