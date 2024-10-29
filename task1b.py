from generate_random_graph import generate_random_graph

for num_of_vertices in range(100, 1100, 100):

    graph = generate_random_graph(num_of_vertices, 0.5, True, False, True, 0, 10)
