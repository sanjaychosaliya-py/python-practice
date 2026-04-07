# Q6 — Given a list of student names and marks, write them to a CSV file and read them back
import csv
students = [
    ["Sanjay", 95],
    ["Raj", 87],
    ["Priya", 92]
]
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Marks"])
    writer.writerows(students)
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
