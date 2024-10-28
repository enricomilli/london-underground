from generate_random_graph import generate_random_graph

for i in range(10):
    num_of_nodes = (i+1) * 100

    graph = generate_random_graph(num_of_nodes, 0.5, True, False, True, 0, 10)
