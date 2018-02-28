def dfs(u, graph):
    connection_vertices = list()
    connection_colors = set()
    global visited
    visited[u] = True
    if graph[u]:
        connection_vertices = graph[u][0]
    for v in connection_vertices:
        connection_colors.add(graph[int(v)-1][1])
    connection_colors.add(0)
    global all_colors
    color = min(all_colors.difference(connection_colors))
    if color < 3:
        graph[u][1] = color
    else:
        with open('out.txt', 'w') as file:
            file.write('N')
        exit()

    for v in connection_vertices:
        if not visited[int(v)-1]:
            dfs(int(v)-1, graph)


graph = dict()

with open('in.txt') as file:
    line_array = [row.strip() for row in file]

for i in range(1, len(line_array)):
    i_neighbors = line_array[i][:-2]
    if i_neighbors:
        graph[i-1] = [i_neighbors.split(' '), 0]

all_colors = {i for i in range(len(graph) + 1)}

visited = [False] * len(line_array)

dfs(0, graph)

first_color = dict()
second_color = dict()

for i in range(len(graph)):
    if graph[i][1] == 1:
        first_color[i] = graph[i]
    else:
        second_color[i] = graph[i]

sorted(first_color, key=lambda vertix: vertix)
sorted(second_color, key=lambda vertix: vertix)

first_color_vertix = str()
second_color_vertix = str()

for vertix in first_color.keys():
    first_color_vertix += str(vertix + 1) + ' '
for vertix in second_color.keys():
    second_color_vertix += str(vertix + 1) + ' '


with open('out.txt', 'w') as file:
    file.write('Y\n')
    file.write(first_color_vertix+'\n')
    file.write(second_color_vertix)
