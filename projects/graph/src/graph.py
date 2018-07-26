"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        self.vertices[label] = set()
    
    def add_edge(self, vertex1, vertex2):
        assert (vertex1 in self.vertices and vertex2 in self.vertices), "One or more specified vertices aren't in the graph"

        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)