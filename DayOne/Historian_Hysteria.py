def get_data() -> list:
    with open('input.txt', 'r') as file:
        return [lines.strip() for lines in file]


def analyse_list():
    inputs_list = get_data()
    print(inputs_list)
    distances_values_list = []
    list_one = []
    list_two = []

    for inputs in inputs_list:
        inputs_split = inputs.split()
        list_one.append(int(inputs_split[0]))
        list_two.append(int(inputs_split[1]))

    list_one.sort()
    list_two.sort()

    for i in range(len(list_one)):
        distances_values_list.append(abs(list_one[i] - list_two[i]))
    total_distance = sum(distances_values_list)
    print(f"Total distance: {total_distance}")


analyse_list()
