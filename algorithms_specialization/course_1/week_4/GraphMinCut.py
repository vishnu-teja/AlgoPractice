import random
import copy

# pick two random vertices
# merge edges of vertex 2 into vertex 1
# loop through all the vertices and replace vertex 2 with vertex 1 in their edges
# remove vertex 1 from edges of vertex 1
# delete vertex 2


def graph_min_cuts(graph):
    while len(graph) > 2:
        v1 = random.choice(
            list(graph.keys()))
        v2 = random.choice(graph[v1])
        graph[v1].extend(graph[v2])

        for x in graph[v2]:
            if(v2 in graph[x]):
                graph[x].remove(v2)
                graph[x].append(v1)

        while v1 in graph[v1]:
            graph[v1].remove(v1)
        del graph[v2]
    return len(list(graph.values())[0])


# result should be 17 for this given data input.
file = open('./week_4/graph_data.txt', 'r')

graph_dict = {}


for line in file:
    key, *values = line.split()
    graph_dict[key] = list(values)
file.close()


min_cuts = len(graph_dict) ** 2
for i in range(10):
    graph = copy.deepcopy(graph_dict)
    cuts = graph_min_cuts(graph)
    if len(list(graph.values())[0]) < min_cuts:
        min_cuts = len(list(graph.values())[0])

print(min_cuts)
