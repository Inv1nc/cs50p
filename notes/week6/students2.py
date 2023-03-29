students = []
with open("student.csv","r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name;
        student["house"] = house;
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")