import re


def find_mul_section_first_pattern():
    matches = []
    modified_matches = []
    pattern = re.compile(r'(mul\(\d+,\d+\))')
    with open('inputs.txt', 'r') as file:
        datas = [line.strip() for line in file]
    for data in datas:
        matches.append(pattern.findall(data))
    for line in matches:
        modified_matches = modified_matches + line
    find_mul_section_second_pattern(modified_matches)

def find_mul_section_second_pattern(matches:list) -> list:
    result = 0
    pattern = re.compile(r'\d+')
    for data in matches:
        second_matches = pattern.findall(data)
        result = result + (int(second_matches[0]) * (int(second_matches[1])))

    print(result)


find_mul_section_first_pattern()
