def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

data = []
with open('input.txt', 'r') as file:
    for line in file:
        info = line.split()
        surname = info[0]
        class_name = info[1]
        grades = list(map(int, info[2:]))
        average_grade = calculate_average(grades)
        data.append((surname, average_grade))

with open('output.txt', 'w') as output_file:
    for surname, avg_grade in data:
        if avg_grade > 6:
            output_file.write(f"{surname}\n")
