from copy import deepcopy
# parse input


def extract_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    # sacar los \n de cada linea
    lines = [line.replace('\n', '') for line in lines]
    # detectar fila que no tiene nada para separar
    for i in range(len(lines)):
        if lines[i] == '':
            break

    input = lines[:i-1]
    number_of_rows = int(max(lines[i-1].split(' ')))
    movements = lines[i+1:]

    return input, number_of_rows, movements

# preprocess input


def preprocess_input(input, number_of_rows):

    input_list = []
    for line in input:
        single_line = []
        c = 0
        for i in list(line):
            c += 1
            if c == 2:
                single_line.append(i)
            elif c == 4:
                c = 0
        input_list.append(single_line)

    # now we need a better format
    returned_list = []
    for i in range(number_of_rows):
        single_line = []
        for line in input_list:
            if line[i] != ' ':
                single_line.append(line[i])
        single_line.reverse()
        returned_list.append(single_line)

    return returned_list


def apply_simple_movement(input, number_of_movements, from_, to_):
    for i in range(1, number_of_movements+1):
        # faltara check si hay para mover...
        block_to_move = input[from_-1][-1]
        input[to_-1].append(block_to_move)
        input[from_-1].pop(-1)

    return input


def apply_complex_movement(input, number_of_movements, from_, to_):
    block_to_move = input[from_-1][::-1][:number_of_movements][::-1]
    for i in block_to_move:
        input[to_-1].append(i)
    for i in range(1, number_of_movements+1):
        input[from_-1].pop(-1)

    return input


def move(input, input_2, movements):
    for movement in movements:
        list_movement = movement.split()
        number_of_movements = int(list_movement[1])
        from_ = int(list_movement[3])
        to_ = int(list_movement[5])
        input = apply_simple_movement(input, number_of_movements, from_, to_)
        input_2 = apply_complex_movement(
            input_2, number_of_movements, from_, to_)


def extract_last_index(input):
    word = ''
    for i in input:
        word += i[-1]
    return word


def main():
    path = '2022-05/input.txt'
    input, number_of_rows, movements = extract_input(path)
    input = preprocess_input(input, number_of_rows)
    input_2 = deepcopy(input)
    move(input, input_2, movements)
    word = extract_last_index(input)
    print(word)
    word2 = extract_last_index(input_2)
    print(word2)


if __name__ == "__main__":
    main()
