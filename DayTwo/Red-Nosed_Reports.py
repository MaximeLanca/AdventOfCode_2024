def analyse_reports():
    safe_reports_number = 0
    reports = get_data()

    for report in reports:
        levels = changes_levels_type(report)
        deltas = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

        is_increasing = all(0 < delta <= 3 for delta in deltas)
        is_decreasing = all(-3 <= delta < 0 for delta in deltas)

        if is_increasing or is_decreasing:
            safe_reports_number += 1

    return safe_reports_number


def analyse_reports_for_problem_dampener():
    safe_reports_number = 0
    reports = get_data()

    for report in reports:
        levels = changes_levels_type(report)
        deltas = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

        is_increasing = all(0 < delta <= 3 for delta in deltas)
        is_decreasing = all(-3 <= delta < 0 for delta in deltas)

        if is_increasing or is_decreasing:
            safe_reports_number += 1
        else:
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i + 1:]
                deltas = [modified_levels[j] - modified_levels[j - 1] for j in range(1, len(modified_levels))]

                is_increasing = all(0 < delta <= 3 for delta in deltas)
                is_decreasing = all(-3 <= delta < 0 for delta in deltas)

                if is_increasing or is_decreasing:
                    safe_reports_number += 1
                    break

    return safe_reports_number


def get_data() -> list:
    try:
        with open('inputs.txt', 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("Le fichier 'inputs.txt' est introuvable.")
        return []


def changes_levels_type(report: str) -> list:
    try:
        return [int(level) for level in report.split()]
    except ValueError:
        print(f"Impossible de convertir le rapport en niveaux : {report}")
        return []


if __name__ == "__main__":
    safe_reports = analyse_reports_for_problem_dampener()
    print(f"Nombre de rapports sûrs avec le Dampener : {safe_reports}")


#def analyse_reports():
#    safe_reports_number = 0
#    reports = get_data()
#
#    for report in reports:
#        cleaned_report = changes_levels_type(report)
#        deltas = [cleaned_report[i] - cleaned_report[i - 1] for i in range(1, len(cleaned_report))]
#
#        is_increasing = all(0 < deltas[i] <= 3 for i in range(len(deltas)))
#        is_decreasing = all(-3 <= deltas[i] < 0 for i in range(len(deltas)))
#        if is_increasing or is_decreasing:
#            safe_reports_number += 1
#
#    print(f"The safe reports number is : {safe_reports_number}")
#
#
#def analyse_reports_for_problem_dampener():
#    safe_reports_number = 0
#    reports = get_data()
#    for report in reports:
#        cleaned_report = changes_levels_type(report)
#        deltas = [cleaned_report[i] - cleaned_report[i - 1] for i in range(1, len(cleaned_report))]
#        is_increasing = all(0 < deltas[i] <= 3 for i in range(len(deltas)))
#        is_decreasing = all(-3 <= deltas[i] < 0 for i in range(len(deltas)))
#
#        if is_increasing or is_decreasing:
#            safe_reports_number += 1
#        elif is_decreasing is False and is_increasing is False:
#            for item in range(1,len(deltas)):
#                if (deltas[item] - deltas[item-1]) > 0 and not (0 < deltas[item] <=3):
#                    del deltas[item]
#                    break
#                if (deltas[item] - deltas[item-1]) < 0 and not (-3 < deltas[item] <=0):
#                    del deltas[item]
#                    break
#
#            is_increasing = all(deltas[i] < deltas[i + 1] for i in range(len(deltas) - 1))
#            is_decreasing = all(deltas[i] > deltas[i + 1] for i in range(len(deltas) - 1))
#            if is_increasing or is_decreasing:
#                safe_reports_number += 1
#
#    print(f"The safe reports number is : {safe_reports_number}")
#
#
#def get_data() -> list:
#    with open('inputs.txt', 'r') as file:
#        return [lines.strip() for lines in file]
#
#
#def changes_levels_type(report: str) -> list:
#    sub_list = report.split()
#    return [int(level.strip()) for level in sub_list]
#
#
#analyse_reports_for_problem_dampener()
