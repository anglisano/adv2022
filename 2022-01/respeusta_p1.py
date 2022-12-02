

#READ TXT FILE
# Path: p1\input.txt

with open('2022-01/input.txt', 'r') as file:
    lines = file.readlines()

#sacar los \n de cada linea
lines1 = [line.strip() for line in lines]

# definimos la lista de elfos
elfos = []
acumulado = 0
for i in lines1:
    
    if i:
        acumulado = acumulado + int(i)
    else:
        elfos.append(acumulado)
        acumulado = 0

# extract max of list and index
maximo = max(elfos)
index = elfos.index(maximo)
print(f'El elfo {index+1} tiene el regalo mas grande con {maximo}')