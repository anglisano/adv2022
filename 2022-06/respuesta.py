
with open('2022-06/input.txt', 'r') as file:
    list_input = list(file.read())

# list_input=list('mjqjpqmgbljsphdztnvjfqwrcgsmlb') #7
# list_input=list('bvwbjplbgvbhsrlpgdmjqwftvncz') #5
# list_input=list('nppdvjthqldpwncqszvftbrmjlhg') #6
# list_input=list('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') #10
# list_input=list('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') #11

set(list_input[2:4])
#extract n diferent letters from input

def travel_n_different_letters(list_input, n):
    for i in range(n-1,len(list_input)):
        if len(set(list_input[i-n+1:i+1]))==n:
            return i+1
    return -1

def main():
    p1=travel_n_different_letters(list_input, 4)
    print(f'letters: {p1}')
    p2=travel_n_different_letters(list_input, 14)
    print(f'letters: {p2}')

if __name__ == '__main__':
    main()