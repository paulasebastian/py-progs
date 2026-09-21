
def get_marks():
    students = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        num_subjects = int(input(f"\nEnter the number of subjects for Student {i+1}: "))
        marks = []
        for j in range(num_subjects):
            mark = int(input(f"Enter mark {j+1}: "))
            marks.append(mark)
        students.append({"id": i + 1, "marks": marks})
        print(f"Marks for student {i + 1} : {marks}")
    return students

def get_total(marks):
    return sum(marks)

def get_average(marks):
    return sum(marks) / len(marks)

def get_highest(marks):
    return max(marks)

def get_lowest(marks):
    return min(marks)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


print("=== Student Performance Analysis System ===\n")
student_data = get_marks()

print("\n=== Individual Performance Report ===")
for student in student_data:
    sid = student["id"]
    m = student["marks"]
    
    total = get_total(m)
    avg = get_average(m)
    highest = get_highest(m)
    lowest = get_lowest(m)
    grade = get_grade(avg)
    
    print(f"\nStudent {sid} Report:")
    print(f"Marks: {m}")
    print(f"Total: {total} | Average: {avg:.2f}")
    print(f"Highest Mark: {highest} | Lowest Mark: {lowest}")
    print(f"Grade: {grade}")

sorted_students = sorted(student_data, key=lambda s: get_total(s["marks"]), reverse=True)

print("\n=== Students Sorted by Total Marks (Highest to Lowest) ===")
for student in sorted_students:
    print(f"Student {student['id']} -> Total Marks: {get_total(student['marks'])}")