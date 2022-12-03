
with open('2022-03/input.txt', 'r') as file:
    list_input = file.read().split()

# list_input=[
#     'vJrwpWtwJgWrhcsFMMfFFhFp',
#     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#     'PmmdzqPrVvPwwTWBwg',
#     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#     'ttgJtRGJQctTZtZT',
#     'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]

#list of all letters
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_letters = list(letters)
value_letters = list(range(1,52+1))


#function to split text on list of 2 text at half
def split_text(text):
    half = len(text)//2
    return text[:half], text[half:]

#function to calculate the letter that exists in both texts
def calculate_letter(text1, text2):
    list_text1 = list(text1)
    list_text2 = list(text2)
    list_result = []
    for letter in list_text1:
        if letter in list_text2:
            list_result.append(letter)
    return list_result

# function to calculate the value of the letter
def calculate_value_letter(letter):
    value = value_letters[list_letters.index(letter)]
    return value
# funtion to remove duplicates from list
def remove_duplicates(list_with_duplicates):
    list_result = list(dict.fromkeys(list_with_duplicates))
    return list_result
# function to calculate the value of the input
def calculate_value_input(list_input):
    result = 0
    list_results=[]
    for text in list_input:
        text1, text2 = split_text(text)
        list_result = calculate_letter(text1, text2)
        simpel_result=remove_duplicates(list_result)
        if len(simpel_result) > 1:
            print("Error: more than one letter")
            print(f'list_result: {simpel_result} in text1: \
                {text1} and text2: {text2}')
        for letter in simpel_result:
            value = calculate_value_letter(letter)
            list_results.append(value)
            result += value
    return result,list_results

if __name__ == '__main__':
    result = calculate_value_input(list_input)
    print(f'the result is {result[0]}')