from collections import deque
# from dataclasses import dataclass
import re


def clear_imput(path):
    with (open(path)) as f:
        txt = f.read()

    pattern = r'Valve ([A-Z]{2}) .*=(\d*); .* valves? (.*)'
    search_pattern = re.findall(pattern, txt)
    graph = dict()
    for i in search_pattern:
        graph[i[0]] = {'flow': int(i[1]), 'neighbors': i[2].split(', ')}
    return graph


# count how many valves with flow diferent than 0
def count_valves(state):
    return sum([1 for i in state if state[i]['flow'] != 0])

# calculate distances between valves that are not 0
# this will help on the next step of bruteforce


def calculate_distances(state):
    nonempty_valves = []  # i for i in state if state[i]['flow']!=0
    distances = dict()
    for valve in state:
        if state[valve]['flow'] == 0 and valve != 'AA':
            continue
        if valve != 'AA':
            nonempty_valves.append(valve)

        # para partir de distancia 0 en el while
        distances[valve] = {valve: 0, "AA": 0}
        visited = {valve}
        queue = deque([(0, valve)])
        while queue:
            distance, position = queue.popleft()
            for neighbor in state[position]['neighbors']:
                # if distances.get(neighbor,None) is None:
                #     distances[neighbor]={}
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if state[neighbor]['flow'] != 0:
                    distances[valve][neighbor] = distance+1
                queue.append((distance+1, neighbor))
        # clear fake distances
        del distances[valve][valve]
        if valve != "AA":
            del distances[valve]["AA"]
    return distances


def index_int_valves(state):
    nonempty_valves = [i for i in state if state[i]['flow'] != 0]  #
    indexes = dict()
    for idx, valve in enumerate(nonempty_valves):
        indexes[valve] = idx
    return indexes

cache={} # memorizaremos la info aki para no repetir calculos
def dfs(distances, time, valve, bit_opened_valves, state, indexes):
    if (time,valve,bit_opened_valves) in cache:
        return cache[(time,valve,bit_opened_valves)]
    # no puedo recoger las valves abiertas cerradas pk es lista
    # para minimizar espacio
    max_flow = 0
    # print(format(0, '08b'))
    # given a actual position, time and valves opened
    # calculate max flow
    for neighbor in distances[valve]:
        '''
        compare bit_opened_valves with bit
        100000 & 000001 = 0
        100000 & 000010 = 0
        100000 & 000100 = 0
        100000 & 001000 = 0
        100000 & 010000 = 0
        100000 & 100000 = 1
        # esta parte funciona pero no entiendo 100% pk funciona
        # el bit_opened_valves es un int, y el bit es un int
        # al comparar con << el bit estamos cogiendo el bit de la posicion
        # del bit_opened_valves.

        '''
        bit=1<<indexes[neighbor]
        # print(format(bit_opened_valves, '08b'))
        # print(format(bit, '08b'))
        if bit_opened_valves & bit:
            continue
        remaining_time = time-distances[valve][neighbor]
        if remaining_time < 0:
            continue
        max_flow = max(max_flow,
                       dfs(distances, remaining_time, neighbor, bit_opened_valves | bit, state,indexes) \
                        + state[valve]['flow']*remaining_time
                       )
    cache[(time,valve,bit_opened_valves)]=max_flow
    return max_flow


def main():
    path='2022-16/input.txt'
    # path = '2022-16/input_example.txt'
    graph = clear_imput(path)
    number_valves = count_valves(graph)
    distances = calculate_distances(graph)
    indexes = index_int_valves(graph)
    print(indexes)
    # 0 es no valve opened
    max_flow = dfs(distances, 30, 'AA', 0, graph,indexes)
    print(max_flow)

    # part 2
    b=(1<<number_valves)-1
    '''
    para 4 valves
    se haria
    1111
    0110
    1001

    y despues
    1111
    1001
    0110

    nose si se podria reducir a la mitad el calculo por aki...
    '''
    print(format(b, '08b'))
    print(format(b^0, '08b'))
    print(format(b^1, '08b'))
    # el elefante hara el recorrido del resto de valves que no hayamos hecho
    # nosotros
    max_flow2=0
    for i in range(b+1):
        max_flow2=max(max_flow2,
            dfs(distances,26,'AA',i,graph,indexes),
            dfs(distances,26,'AA',b ^ i,graph,indexes)
        )
    print(max_flow2)

if __name__ == '__main__':
    main()
# decide open actual valve or go to other location and open valve
# you can open valve only if you have enough time, if its not opened yet
# and if you have enough pressure/flow
# if you have enough time, pressure and valve is not opened yet, you can open it
# if you have enough time, pressure and valve is opened, you can go to other location
# if you have enough time, but not enough pressure, you can go to other location

# how many stats are there? 2^15 posible states of valves
# 58 possible locations
# 30 possible time
# 2**15*50*30 = 49.152.000 possible states
