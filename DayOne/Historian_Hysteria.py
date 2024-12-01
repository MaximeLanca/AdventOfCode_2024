def analyse_list():
    inputs_list = get_data()
    distances_values_list = []
    list_one = []
    list_two = []

    for inputs in inputs_list:
        inputs_split = inputs.split()
        list_one.append(int(inputs_split[0]))
        list_two.append(int(inputs_split[1]))

    similarity_score_part_two = calculate_similarity_number(list_one, list_two)

    list_one.sort()
    list_two.sort()

    for i in range(len(list_one)):
        distances_values_list.append(abs(list_one[i] - list_two[i]))
    total_distance = sum(distances_values_list)

    print(f"Total distance: {total_distance}")
    print(f"Similarity score: {similarity_score_part_two}")


def calculate_similarity_number(list_one, list_two):
    similarity_score = 0
    for n1 in list_one:
        recurrence = 0
        for n2 in list_two:
            if n1 == n2:
                recurrence += 1
        similarity_score = (similarity_score + (n1 * recurrence))
    return similarity_score


def get_data() -> list:
    with open('input.txt', 'r') as file:
        return [lines.strip() for lines in file]


analyse_list()
