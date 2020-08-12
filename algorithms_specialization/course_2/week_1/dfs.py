import sys
sys.setrecursionlimit(10000)


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.positions = {}
        self.leaders = {}

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_edges(self, vertex, edgeType):
        return self.vertices[vertex][edgeType]

    def set_explored(self, vertex):
        self.vertices[vertex]['explored'] = True

    def is_explored(self, vertex):
        return self.vertices[vertex]['explored'] == True

    def reset_explored(self):
        for vertex in self.vertices:
            self.vertices[vertex]['explored'] = False

    def set_position(self, vertex, position):
        self.positions[str(position)] = vertex

    def get_vertices_by_position(self):
        return reversed(list(self.positions.values()))

    def set_leader(self, vertex, leader):
        if leader in self.leaders:
            self.leaders[leader].append(vertex)
        else:
            self.leaders[leader] = [vertex]

    def get_leaders(self):
        return self.leaders


# TODO: correct this method
# def dfs_loop(vertices, edgeType):
#     global graph
#     for vertex in vertices:
#         if graph.is_explored(vertex):
#             continue
#         dfs(vertex, edgeType)

# def dfs(vertex, edgeType):
#     global graph
#     global position
#     global leader
#     if not graph.is_explored(vertex):
#         leader = vertex
#         graph.set_explored(vertex)
#         edges = graph.get_edges(vertex, edgeType)
#         for edge in edges:
#             if not graph.is_explored(edge):
#                 dfs(edge, edgeType)
#         if edgeType == 'reverseEdges':
#             position += 1
#             graph.set_position(vertex, position)
#         if edgeType == 'edges':
#             graph.set_leader(vertex, leader)


def dfs_loop(vertices, edgeType):
    global graph
    position = 0
    leader = None
    for vertex in vertices:
        if graph.is_explored(vertex):
            continue
        vertices_stack = [vertex]
        leader = vertex

        while vertices_stack:
            v = vertices_stack.pop()
            if not graph.is_explored(v):
                graph.set_explored(v)
                vertices_stack.append(v)
                if edgeType == 'edges':
                    graph.set_leader(v, leader)
                edges = graph.get_edges(v, edgeType)
                for edge in edges:
                    if not graph.is_explored(edge):
                        vertices_stack.append(edge)
            else:
                if edgeType == 'reverseEdges':
                    position += 1
                    graph.set_position(v, position)


vertices = {}
position = 0
leader = None

# file = open("./course_2/week_1/graph_dummy.txt", 'r')
file = open("./course_2/week_1/directed_graph.txt", 'r')

for line in file:
    key, value = line.split()
    if key not in vertices:
        vertices[key] = {'explored': False,
                         'edges': [value], 'reverseEdges': []}
    else:
        vertices[key]['edges'].append(value)
    if value not in vertices:
        vertices[value] = {'explored': False,
                           'edges': [], 'reverseEdges': [key]}
    else:
        vertices[value]['reverseEdges'].append(key)
file.close()


graph = Graph(vertices)

# step 1: perform DFS on reverse edges and add positions.
# step 2: sort by posistions without using sorting algorithm
# step 3: perfomr DFS on edges and add leaders
# step 4: create leaders dictionary
# step 5: return top 5

dfs_loop(graph.get_vertices(), 'reverseEdges')

graph.reset_explored()

positioned_vertices = graph.get_vertices_by_position()


dfs_loop(positioned_vertices, 'edges')

# Each leader is a strongly connected node network
leads = sorted(
    list(map(lambda x: len(x), graph.get_leaders().values())), reverse=True)
print(leads[: 5])
