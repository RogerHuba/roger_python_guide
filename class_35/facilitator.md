# DSA Graphs

## Jokes

- I just saw my math teacher lock himself in his office with a piece of graph paper. I think he must be plotting something.
- I made a graph showing all of my past relationships. It has an ex-axis and a why-axis
- I may be willing to solve equations. Graphing is where I draw the line!

## Where we are at

- Review the Overall Class Schedule. Get ready for REACT stuff.
- Things will taper down in the final module.
- During that final module you will be going though whiteboarding interviews.

## Graphs

- Bring up the implementation asignment and show the requirements.
  - Notice you are doing an adjacency list and not an adjacency matrix

- Bring up the Graph readme.
- [Grapghs](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-35/resources/graphs.html)

> What are some real world scenarios that depict a graph?

    - Airline 
    - Sprinkler

> Graph is a non-linear data structure.

- Draw out Linear vs Non-linear structures.
Linear - Normally easier to implement and traverse

Talk about some Terminology (Start Drawing with Invision)

Vertex - Also a node.  Used interchangably
    Does not have to have an edge (Island)

Edge - A connection between 2 nodes
    - In the absence of specification, you will assume bi-directional
    - Can also have a weight
    - Can be uni-direction
    - Can be bi directional

Neighbors
    - adjacnet nodes connected by an edge
    - No Neighbors

Degree - This is the number of edges connected to that vertex (draw one)

### Code Time

```python
class Graph:

    def _init__(self):
        pass

    def add_node(self):
        pass

    def add_edge(self):
        pass

    def get_node(self):
        pass

    def get_neighbor(self):
        pass    

    def size(self):
        pass

class Vertex:
    def __init(self):
        pass

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
```

What kind of tracking are we going to use to use in the graph? What is the purposes here? This will hold all of the vertex in the graph. When we add a vertex in the graph, we will need to add it in the adjacency list.
