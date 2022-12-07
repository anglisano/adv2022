from collections import defaultdict

def open_file(path_file):
    with open(path_file, 'r') as file:
        list_input = file.readlines()
    list_input=[i.strip() for i in list_input]
    return list_input

#diccionario con el tamaño de cada directorio
def simplify_dir_size(list_input):
    size_dir=defaultdict(int)
    path=[]
    for line in list_input:
        words=line.split(' ')
        if words[1]=='cd':
            if words[2]=='..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls' or words[0] == 'dir':
            next
        else:
            size_single_file=int(words[0])
            print(path, size_single_file)
            #acumulo el tamaño de cada archivo
            #en el directorio actual y todos los superiores
            for i in range(len(path)+1):
                print('/'.join(path[:i]), size_single_file)
                size_dir['/'.join(path[:i])]+=size_single_file
    print('-'*50)
    #print(size_dir)
    for path, size in size_dir.items():
        print(f'{path} {size}')
    return size_dir



def return_dir_with_size_less_than_n(size_dir, n):
    sum_size=0
    for path, size in size_dir.items():
        if size<n:
            sum_size+=size
    return sum_size


def main():
    list_input=open_file('2022-07/input.txt')#_example
    size_dir=simplify_dir_size(list_input)
    sum_size=return_dir_with_size_less_than_n(size_dir, 100000)
    print(sum_size)

    #problem 2
    # find de minimum directory size that can be deleted
    # to free space_required
    necessary_space=70000000-30000000
    used=size_dir['/']
    size_dir_sorted=sorted(size_dir.items(), key=lambda x: x[1])
    for path, size in size_dir_sorted:
        
        if used-size<necessary_space:
            print(path, size)
            break



if __name__ == '__main__':
    main()