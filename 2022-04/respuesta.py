
with open('2022-04/input.txt', 'r') as file:
    list_input = file.read().split()

# list_input = [
#     '2-4,6-8',
#     '2-3,4-5',
#     '5-7,7-9',
#     '2-8,3-7',
#     '6-6,4-6',
#     '2-6,4-8']


list_input = [i.split(',') for i in list_input]


def calculate_initial_and_end_value(elf_section):
    initial_value, end_value = elf_section.split('-')
    return initial_value, end_value


def list_of_elf_sections(initial_section, end_section):
    list_elf_sections = list(range(int(initial_section), int(end_section)+1))
    return list_elf_sections


def check_if_we_have_a_free_elf(
    list_of_elf_section, 
    list_of_other_elf_sections,
    overlap=False):
    free_elf1 = False
    free_elf2 = False
    # compare the list of elf sections with the list of other elf sections
    for section in list_of_elf_section:
        if section in list_of_other_elf_sections:
            free_elf1 = True
        elif overlap:
            next
        else:
            free_elf1 = False
            break
    # compare the list of other elf sections with the list of elf sections
    for section in list_of_other_elf_sections:
        if section in list_of_elf_section:
            free_elf2 = True
        elif overlap:
            next
        else:
            free_elf2 = False
            break
    # if one elfs is free return 1
    free_elf = free_elf1 or free_elf2


    return free_elf


def main():
    list_of_free_elfs = []
    list_of_free_elfs_overlap = []
    for elfs in list_input:
        elf1, elf2 = elfs

        initial_section_elf1, end_section_elf1 = calculate_initial_and_end_value(
            elf1)
        initial_section_elf2, end_section_elf2 = calculate_initial_and_end_value(
            elf2)

        list_of_elf1_sections = list_of_elf_sections(
            initial_section_elf1, end_section_elf1)
        list_of_elf2_sections = list_of_elf_sections(
            initial_section_elf2, end_section_elf2)

        free_elf = check_if_we_have_a_free_elf(
            list_of_elf1_sections, list_of_elf2_sections)
        list_of_free_elfs.append(free_elf)

        free_elf_overlap = check_if_we_have_a_free_elf(
            list_of_elf1_sections, list_of_elf2_sections, overlap=True)
        list_of_free_elfs_overlap.append(free_elf_overlap)
    print(f' number of free elfs are: {sum(list_of_free_elfs)}')
    print(f' number of free elfs overlap are: {sum(list_of_free_elfs_overlap)}')


if __name__ == '__main__':
    main()
