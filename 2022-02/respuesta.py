

with open('2022-02/input.txt', 'r') as file:
    lines = file.readlines()

#sacar los \n de cada linea
lines1 = [line.strip() for line in lines]
lines2 = [line.split(' ') for line in lines1]

# lines2=[['A','Y'],['B','X'],['C','Z']]

# def estrategi
def estrategi(entrada:str):
    if entrada=='A':#rock
        return 'Y' #paper
    elif entrada=='B': #paper
        return 'X' #rock
    elif entrada=='C':#sissors
        return 'Z'#sissors

def recuento_puntuacion(entrada:str,respuesta:str):
    if entrada=='A' and respuesta=='Y': #rock vs paper
        return 2+6
    elif entrada=='A' and respuesta=='X': #rock vs rock
        return 3+3
    elif entrada=='A' and respuesta=='Z': #rock vs sissors
        return 1+0
    elif entrada=='B' and respuesta=='Y': #paper vs paper
        return 3+3
    elif entrada=='B' and respuesta=='X': #paper vs rock
        return 1+0
    elif entrada=='B' and respuesta=='Z': #paper vs sissors
        return 2+6
    elif entrada=='C' and respuesta=='Y': #sissors vs paper
        return 1+0
    elif entrada=='C' and respuesta=='X': #sissors vs rock
        return 2+6
    elif entrada=='C' and respuesta=='Z': #sissors vs sissors
        return 3+3

# calculamos el resultado a la lista
resultado_con_estrategia = []
resultado_sin_estrategia = []
for i in lines2:
    respuesta=estrategi(i[0])
    calculo_con_estrategia=recuento_puntuacion(i[0],respuesta)
    calculo_sin_estrategia=recuento_puntuacion(i[0],i[1])
    resultado_con_estrategia.append(calculo_con_estrategia)
    resultado_sin_estrategia.append(calculo_sin_estrategia)

sum(resultado_con_estrategia)
sum(resultado_sin_estrategia)
len(lines2)
len(resultado_con_estrategia)