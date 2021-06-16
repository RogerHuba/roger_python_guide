import pytest
from data_structures.graph.graph import Graph
from challenges.get_edges.get_edges import get_edges


class TestGetEdges:

    def test_proof_of_life(self):
        assert Graph
        assert get_edges

    @pytest.fixture()
    def graph(self):
        graph = Graph()

        # Create nodes
        vertex_1 = graph.add_vertex(1)
        vertex_2 = graph.add_vertex(2)
        vertex_3 = graph.add_vertex(3)
        vertex_4 = graph.add_vertex(4)
        vertex_5 = graph.add_vertex(5)
        vertex_6 = graph.add_vertex(6)

        # Create edges
        graph.add_edge(vertex_1, vertex_2, 150)
        graph.add_edge(vertex_2, vertex_1, 150)
        graph.add_edge(vertex_1, vertex_3, 82)
        graph.add_edge(vertex_3, vertex_1, 82)
        graph.add_edge(vertex_2, vertex_3, 99)
        graph.add_edge(vertex_3, vertex_2, 99)
        graph.add_edge(vertex_2, vertex_4, 42)
        graph.add_edge(vertex_4, vertex_2, 42)
        graph.add_edge(vertex_3, vertex_4, 105)
        graph.add_edge(vertex_4, vertex_3, 105)
        graph.add_edge(vertex_3, vertex_5, 37)
        graph.add_edge(vertex_5, vertex_3, 37)
        graph.add_edge(vertex_3, vertex_6, 26)
        graph.add_edge(vertex_6, vertex_3, 26)
        graph.add_edge(vertex_5, vertex_6, 250)
        graph.add_edge(vertex_6, vertex_5, 250)
        graph.add_edge(vertex_4, vertex_6, 73)
        graph.add_edge(vertex_6, vertex_4, 73)

        return graph

    test_data = (
        # Pass
        ([1, 2, 3], (True, '$249')),
        ([1, 2, 4], (True, '$192')),
        ([1, 3, 6, 5], (True, '$358')),
        ([3, 2, 4, 6], (True, '$214')),
        ([5, 6, 3, 2], (True, '$375')),

        # Fail
        ([1, 2, 5], (False, '$0')),
        ([4, 3, 1, 5], (False, '$0')),
        ([2, 6], (False, '$0')),
        ([6, 3, 5, 1], (False, '$0')),
        ([2, 3, 4, 5], (False, '$0')),

    )

    @pytest.mark.parametrize('input, output', test_data)
    def test_get_edges(self, input, output, graph):
        assert get_edges(graph, input) == output
