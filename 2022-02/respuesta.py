

with open('2022-02/input.txt', 'r') as file:
    lines = file.readlines()

# sacar los \n de cada linea
lines1 = [line.strip() for line in lines]
lines2 = [line.split(' ') for line in lines1]

# lines2=[['A','Y'],['B','X'],['C','Z']]

# def estrategi


def estrategi(entrada: str):
    if entrada == 'A':  # rock
        return 'Y'  # paper
    elif entrada == 'B':  # paper
        return 'X'  # rock
    elif entrada == 'C':  # sissors
        return 'Z'  # sissors


def recuento_puntuacion(entrada: str, respuesta: str):
    if entrada == 'A' and respuesta == 'X':  # rock vs rock
        return 1+3
    elif entrada == 'A' and respuesta == 'Y':  # rock vs paper
        return 2+6
    elif entrada == 'A' and respuesta == 'Z':  # rock vs sissors
        return 3+0
    elif entrada == 'B' and respuesta == 'X':  # paper vs rock
        return 1+0
    elif entrada == 'B' and respuesta == 'Y':  # paper vs paper
        return 2+3
    elif entrada == 'B' and respuesta == 'Z':  # paper vs sissors
        return 3+6
    elif entrada == 'C' and respuesta == 'X':  # sissors vs rock
        return 1+6
    elif entrada == 'C' and respuesta == 'Y':  # sissors vs paper
        return 2+0
    elif entrada == 'C' and respuesta == 'Z':  # sissors vs sissors
        return 3+3


# calculamos el resultado a la lista
resultado_con_estrategia = []
resultado_sin_estrategia = []
for i in lines2:
    respuesta = estrategi(i[0])
    calculo_con_estrategia = recuento_puntuacion(i[0], respuesta)
    calculo_sin_estrategia = recuento_puntuacion(i[0], i[1])
    resultado_con_estrategia.append(calculo_con_estrategia)
    resultado_sin_estrategia.append(calculo_sin_estrategia)

sum(resultado_con_estrategia)
sum(resultado_sin_estrategia)
print(f'el resultado del ejercicio es: {sum(resultado_sin_estrategia)}')


# ara k ja lentenc el fare algo millo

calculo_respuesta = {
    'A': {'X': 1+3, 'Y': 2+6, 'Z': 3+0},
    'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6},
    'C': {'X': 1+6, 'Y': 2+0, 'Z': 3+3}
}
calculo_respuesta_2 = {
    'A': {'X': 3+0, 'Y': 1+3, 'Z': 2+6},
    'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6},
    'C': {'X': 2+0, 'Y': 3+3, 'Z': 1+6}
}
acumulado_respuesta = 0
acumulado_respuesta_2 = 0
for i in lines2:
    acumulado_respuesta += calculo_respuesta[i[0]][i[1]]
    acumulado_respuesta_2 += calculo_respuesta_2[i[0]][i[1]]
print(f'el resultado del ejercicio algo mas pro es: {acumulado_respuesta}')
print(f'el resultado del ejercicio algo mas pro es: {acumulado_respuesta_2}')