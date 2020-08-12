# take a vertex
# for each of other vertices:
#        find all possible paths to that vertex
#        compare the distances and store the min open
#        repeat.


# TODO: implement this algorithm using min Heap.

class Graph:
    def __init__(self, page):
        self.vertices = {}
        for line in page:
            key, *values = line.split()
            edges = {}
            for v in values:
                val, dist = v.split(",")
                edges[val] = dist
                self.vertices[key] = {
                    "explored": False,
                    "edges": edges,
                }

    def get_vertices(self):
        return self.vertices


def find_shortest_path(vertices, s_v):
  global distances
  distances[s_v] = 0
  distance_to_vertex(s_v)



def distance_to_vertex(v):
  global vertices
  global distances

  edges = vertices[v]['edges']
  for e in edges.keys():
    dist = distances[v] + int(edges[e])
    if not e in distances or dist < distances[e]:
      distances[e] = dist
      distance_to_vertex(e)

  


file = open("./course_2/week_2/dijkstras.txt", "r")

graph = Graph(file)
vertices = graph.get_vertices()
visited = []
distances = {}

find_shortest_path(vertices, "1")

nodes = [7,37,59,82,99,115,133,165,188,197]

for n in nodes:
  print(str(n) + ' : ' + str(distances[str(n)]))


# expected answers
# 7 : 2599
# 37 : 2610
# 59 : 2947
# 82 : 2052
# 99 : 2367
# 115 : 2399
# 133 : 2029
# 165 : 2442
# 188 : 2505
# 197 : 3068