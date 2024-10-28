import matplotlib.pyplot as plt
import numpy as np


def average(ls):
    if len(ls) == 0:
        return 0
    return sum(ls) / len(ls)

def prop_above(ls):
    filtered_ls = []
    for x in ls:
        if x != ' ':
            filtered_ls.append(x)
    if len(filtered_ls) == 0:
        return 0
    avg = average(filtered_ls)
    count_above = 0
    for x in filtered_ls:
        if x > avg:
            count_above += 1
    return count_above / len(filtered_ls) #no clue, got most of it from different examples I found. But it kind of works

def median(ls):
    sorted_ls = sorted(ls)
    n = len(sorted_ls)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        median_value = (sorted_ls[mid - 1] + sorted_ls[mid]) / 2
    else:
        median_value = sorted_ls[mid]
    return median_value

exercise_hours = []
file = open('StudentExercise.csv', 'r')
reader = file.readlines()

for row in reader:
    hr = row.split(',')
    pieces = hr[0]
    
    # Only process valid numbers and skip empty or '0' values
    if pieces != '':
        try:
            exercise_hours.append(float(pieces))
        except ValueError:
            print(f"Invalid data found in row: {pieces}")
file.close()


avg_exercise = average(exercise_hours)
prop_above_avg = prop_above(exercise_hours)
median_exercise = median(exercise_hours)

print(f"Average exercise hours: {avg_exercise:.2f}")
print(f"Proportion of students above average: {prop_above_avg:.2f}")
print(f"Median exercise hours: {median_exercise:.2f}")

if avg_exercise == median_exercise:
    print("The average and median are about the same")
else:
    print("The average and median differ") 

plt.hist(exercise_hours, bins=10, edgecolor='black')
plt.show()