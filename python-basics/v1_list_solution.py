students = [
    ["Rahul", 78, 85, 90, 67, 72],
    ["Smeeta", 92, 88, 76, 95, 81],
    ["Amit", 55, 60, 45, 70, 65],
    ["Jaskeerat", 88, 91, 84, 79, 93],
    ["Niraj", 40, 52, 61, 73, 85]
]

# ----------------------------------
# 1. Find Topper and Lowest Scorer
# ----------------------------------

topper_name = ""
topper_avg = 0

lowest_name = ""
lowest_avg = 100

for student in students:
    total = 0

    # Marks start from index 1
    for i in range(1, len(student)):
        total += student[i]

    avg = total / 5

    if avg > topper_avg:
        topper_avg = avg
        topper_name = student[0]

    if avg < lowest_avg:
        lowest_avg = avg
        lowest_name = student[0]

print(f"Topper: {topper_name} (Avg: {topper_avg})")
print(f"Lowest: {lowest_name} (Avg: {lowest_avg})")


# ----------------------------------
# 2. Students scoring above 80
#    in at least 3 subjects
# ----------------------------------

eligible_students = []

for student in students:
    count = 0

    for i in range(1, len(student)):
        if student[i] > 80:
            count += 1

    if count >= 3:
        eligible_students.append(student[0])

print("Students with 3+ subjects above 80:", eligible_students)


# ----------------------------------
# 3. Bubble Sort by Average Marks
#    Descending Order
# ----------------------------------

sorted_students = students.copy()

n = len(sorted_students)

for i in range(n):

    for j in range(0, n - i - 1):

        avg1 = sum(sorted_students[j][1:]) / 5
        avg2 = sum(sorted_students[j + 1][1:]) / 5

        if avg1 < avg2:
            sorted_students[j], sorted_students[j + 1] = (
                sorted_students[j + 1],
                sorted_students[j]
            )

sorted_names = []

for student in sorted_students:
    sorted_names.append(student[0])

print("Sorted by average:", sorted_names)


# ----------------------------------
# 4. Improved in Last Subject
#    Using Negative Indexing
# ----------------------------------

print("\nImprovement Report")

for student in students:

    second_last = student[-2]
    last = student[-1]

    if last > second_last:
        status = "Yes"
    else:
        status = "No"

    print(f"{student[0]} -> {status}")
