from reader import day11

'''
idea:
you can test that this digraph doesn't have any cycle, this means, we have a network,
that means we can go "layer by layer", either fft or dac must be in closer layer to svr

solution:
find total number of paths to each vertex
check which from fft or dac has less paths available, less paths means it's in previous layer
get subgraphs G1 and G2 from finding which vertices can be reached starting from fft and dac respectively
if fft is earlier:
find number of paths to dac in G1, suppose it's x
find number of paths to out in G2, suppose it's y
else
find number of paths to out in G2, suppose it's y
find number of paths to dac in G1, suppose it's x
result = number of paths to fft in original graph * x * y

'''

file = 'input.txt'
data = day11(file)


def find_backwards_neghborhoods(neighbors_list):
    backwards = {key: set() for key in neighbors_list}
    backwards['out'] = set()
    for key in neighbors_list:
        for vert in neighbors_list[key]:
            backwards[vert].add(key)

    return backwards


def find_all_paths_linear(neighbors_list, start, end):
    #processed = 'vert' : number_of_paths
    vertices_paths = {vert : 0 for vert in neighbors_list.keys()}
    vertices_paths[start] = 1
    vertices_paths[end] = 0
    processed_verts = set()
    backward_neghbors = find_backwards_neghborhoods(neighbors_list)
    waiting_to_be_processed = [start]
    while waiting_to_be_processed:
        #current vertex is a vertex that had every backwards neighbor processed
        curr_vert = waiting_to_be_processed.pop(0)
        processed_verts.add(curr_vert)
        for back_neigh in backward_neghbors.get(curr_vert):
            vertices_paths[curr_vert] += vertices_paths[back_neigh]
        #check if any front neighbors can be processed now
        if neighbors_list.get(curr_vert) is None:
            continue
        for front_neigh in neighbors_list.get(curr_vert):
            if backward_neghbors.get(front_neigh).issubset(processed_verts):
                waiting_to_be_processed.append(front_neigh)
    return vertices_paths

def get_subgraph_reachable_from_vertex(neighbors_list, start):
    #BFS
    reached_vertices = set()
    to_process = [start]
    while to_process:
        curr_vert = to_process.pop(0)
        reached_vertices.add(curr_vert)
        try:
            for neigh in neighbors_list[curr_vert]:
                if neigh not in reached_vertices:
                    to_process.append(neigh)
                    #remove duplicates
                    to_process = set(to_process)
                    to_process = list(to_process)
        except KeyError:
            continue
    #     print(reached_vertices)
    #
    # print(reached_vertices)
    new_graph = {vert : [] for vert in reached_vertices}
    for vert in new_graph:
        try:
            for neigh in neighbors_list[vert]:
                if neigh in reached_vertices:
                    new_graph[vert].append(neigh)
        except KeyError:
            continue

    return new_graph


if __name__=='__main__':
    all_possible_paths_num = find_all_paths_linear(data, 'svr', 'out')
    print(all_possible_paths_num['fft'] , all_possible_paths_num['dac'])
    new_graph_from_fft = get_subgraph_reachable_from_vertex(data, 'fft')
    new_graph_from_dac = get_subgraph_reachable_from_vertex(data, 'dac')
    if all_possible_paths_num['fft'] < all_possible_paths_num['dac']:
        all_possible_paths_num_from_fft = find_all_paths_linear(new_graph_from_fft,'fft', 'out')
        all_possible_paths_num_from_dac = find_all_paths_linear(new_graph_from_dac, 'dac', 'out')
        print(f'{all_possible_paths_num["fft"]} * {all_possible_paths_num_from_fft["dac"]} * {all_possible_paths_num_from_dac["out"]}'
              f'= {all_possible_paths_num["fft"]*all_possible_paths_num_from_fft["dac"]*all_possible_paths_num_from_dac["out"]}')
    else:
        all_possible_paths_num_from_dac = find_all_paths_linear(new_graph_from_dac, 'dac', 'out')
        all_possible_paths_num_from_fft = find_all_paths_linear(new_graph_from_fft, 'fft', 'out')
        print(
            f'{all_possible_paths_num["fft"]} * {all_possible_paths_num_from_fft["dac"]} * {all_possible_paths_num_from_dac["out"]}')
    print(get_subgraph_reachable_from_vertex(data, 'ccc'))