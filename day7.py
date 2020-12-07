import re
from collections import defaultdict


# def bfs(graph, source):
#     visited = set()
#     q = deque([source])
#     while q:
#         u = q.popleft()
#         for v in graph[u]:
#             if v not in visited:
#                 visited.add(v)
#                 q.append(v)
#     return visited

def dfs(graph, visited, source_vertex):
    visited[source_vertex] = True
    neighbors = graph[source_vertex]
    for neighbor in neighbors:
        if not visited[neighbor[1]]:
            dfs(graph, visited, neighbor[1])


def solve_part_1(graph):
    visited = defaultdict(bool)  # can also be a set here
    dfs(graph, visited, 'shiny gold')
    return len(visited.keys()) - 1


def bag_count(graph, source_vertex):
    neighbors = graph[source_vertex[1]]
    count = 0
    for neighbor in neighbors:
        count += neighbor[0] * (1 + bag_count(graph, neighbor))
    return count


def solve_part_2(graph):
    return bag_count(graph, (0, 'shiny gold'))


# graph
# 'bright white' =  [('1', 'light red'), ('3', 'dark orange')]
# 'muted yellow' =  [('2', 'light red'), ('4', 'dark orange')]
# 'shiny gold' =  [('1', 'bright white'), ('2', 'muted yellow')]
# 'faded blue' =  [('9', 'muted yellow'), ('3', 'dark olive'), ('5', 'vibrant plum')]
# 'dark olive' =  [('1', 'shiny gold')]
# 'vibrant plum' =  [('2', 'shiny gold')]
# 'dotted black' =  [('4', 'dark olive'), ('6', 'vibrant plum')]
#
# and it's reverse are returned
def parse_data(data):
    # vibrant purple bags contain 3 shiny lavender bags, 1 mirrored gray bag, 4 muted bronze bags.
    contained_in_graph = defaultdict(list)
    contains_graph = defaultdict(list)
    pattern = re.compile(r"(.+) bags contain (.+)")
    for line in data:
        match = pattern.match(line)
        parent = match.group(1)
        others = match.group(2)
        children = re.findall(r'(\d+) (.+?) bags?', others)
        for count, child_bag_name in children:
            contained_in_graph[child_bag_name].append((count, parent))
            contains_graph[parent].append((int(count), child_bag_name))
    return contained_in_graph, contains_graph


if __name__ == '__main__':
    with open('day7_input.txt') as f:
        data = f.read().splitlines()
        contained_in_graph, contains_graph = parse_data(data)
        result = solve_part_1(contained_in_graph)
        print(result)
        result = solve_part_2(contains_graph)
        print(result)
