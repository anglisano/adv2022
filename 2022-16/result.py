def dfs(graph, start, visited, time, pressure):
    # Mark the current valve as visited
    visited.add(start)

    # Open the current valve and add its flow rate to the pressure
    pressure += graph[start]['flow']
    time += 1

    # Find the next valve to visit
    max_flow = -1
    next_valve = None
    for neighbor in graph[start]['neighbors']:
        if neighbor not in visited and graph[neighbor]['flow'] > max_flow:
            max_flow = graph[neighbor]['flow']
            next_valve = neighbor

    # If we have found a valve to visit, move to it and continue the search
    if next_valve is not None:
        time, pressure = dfs(graph, next_valve, visited, time, pressure)

    return time, pressure

def max_pressure(graph, time_limit):
    # Create a set to track visited valves
    visited = set()

    # Start the search at valve AA
    time, pressure = dfs(graph, 'AA', visited, 0, 0)

    # If we have not reached the time limit, continue the search from the remaining unvisited valves
    while time < time_limit and visited != set(graph.keys()):
        for valve in graph.keys():
            if valve not in visited:
                time, pressure = dfs(graph, valve, visited, time, pressure)

    return pressure

# Test the solution

graph = {
    'AA': {'flow': 0, 'neighbors': ['DD', 'II', 'BB']},
    'BB': {'flow': 13, 'neighbors': ['CC', 'AA']},
    'CC': {'flow': 2, 'neighbors': ['DD', 'BB']},
    'DD': {'flow': 20, 'neighbors': ['CC', 'AA', 'EE']},
    'EE': {'flow': 3, 'neighbors': ['FF', 'DD']},
    'FF': {'flow': 0, 'neighbors': ['EE', 'GG']},
    'GG': {'flow': 0, 'neighbors': ['FF', 'HH']},
    'HH': {'flow': 22, 'neighbors': ['GG']},
    'II': {'flow': 0, 'neighbors': ['AA', 'JJ']},
    'JJ': {'flow': 21, 'neighbors': ['II']}
}

time_limit = 30

print(max_pressure(graph, time_limit))  # Expected output: 54



import collections as c, itertools, re, functools

r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

V, F, D = set(), dict(), c.defaultdict(lambda: 1000)

for v, f, us, in re.findall(r, open('input.txt').read()):
    V.add(v) # store node here
    if f != '0': F[v] = int(f) # stroe flow here
    for u in us.split(', ') : D[u, v] = 1

for k, i, j in itertools.product(V, V, V):
    D[i, j] = min(D[i, j], D[i, k] + D[k, j])

@functools.cache
def search(t, u = 'AA', vs = frozenset(F), e = False):
    tt = max([F[v] * (t - D[u, v] - 1) + search(t - D[u, v] - 1, v, vs - {v}, e)
    for v in vs if D[u, v] < t] + [search(26, vs = vs) if e else 0])
    return tt

print('Part 1: the most pressure you can release is: ' + str(search(30)))
print('Part 2: the most pressure you and the elephant can release is: ' + str(search(26, e = True)))

