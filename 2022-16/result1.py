

import re

with(open('2022-16/input.txt')) as f:
    txt = f.read()

pattern = r'Valve ([A-Z]{2}) .*=(\d*); .* valves? (.*)'
search_pattern=re.findall(pattern, txt)
graph=dict()
for i in search_pattern:
    graph[i[0]]={'flow':int(i[1]), 'neighbors':i[2].split(', ')}

time_limit=30

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