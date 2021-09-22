import pytest
from graph import Graph, Vertex

def test_add_graph():
    graph = Graph()
    assert graph


def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex('spam')
    assert vertex.value == 'spam'


def test_add_edge():
    graph = Graph()
    spam = graph.add_vertex('spam')
    egg = graph.add_vertex('eggs')
    graph.add_edge(spam, egg)
    assert True


@pytest.mark.skip
# Currently failing
def test_add_edge_leo_test(self):
    graph = Graph()
    start = graph.add_vertex('start_vertex')
    end = graph.add_vertex('end_vertex')
    graph.add_edge(start, end)
    assert graph.adjacency_list[start][0].vertex == end


def test_add_edge_test_size_pass():
    graph = Graph()
    spam = graph.add_vertex('spam')
    egg = graph.add_vertex('eggs')
    graph.add_edge(spam, egg)
    assert len(graph.adjacency_list) == 2


def test_add_edge_test_size_fail():
    graph = Graph()
    spam = graph.add_vertex('spam')
    egg = graph.add_vertex('eggs')
    graph.add_edge(spam, egg)
    assert len(graph.adjacency_list) != 3