def analyse_reports():
    safe_reports_number = 0
    reports = get_data()

    for report in reports:
        cleaned_report = changes_levels_type(report)
        deltas = [cleaned_report[i] - cleaned_report[i - 1] for i in range(1, len(cleaned_report))]

        is_increasing = all(0 < deltas[i] <= 3 for i in range(len(deltas)))
        is_decreasing = all(-3 <= deltas[i] < 0 for i in range(len(deltas)))
        if is_increasing or is_decreasing:
            safe_reports_number += 1
            print(reports.index(report), report)

    print(f"The safe reports number is : {safe_reports_number}")


def get_data() -> list:
    with open('inputs.txt', 'r') as file:
        return [lines.strip() for lines in file]


def changes_levels_type(report: str) -> list:
    newlist = report.split()
    return [int(level.strip()) for level in newlist]


analyse_reports()
