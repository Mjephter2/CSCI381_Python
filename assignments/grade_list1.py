print("Enter done to exit.")

num_students = 0
class_total_grade = 0

while True:
    student_name = input("Please enter name: ")
    if student_name == 'done':
        break
    num_students += 1
    student_midterm = float(input("Please enter midterm: "))
    student_final = float(input("Please enter final: "))

    student_average = (student_midterm + student_final) / 2
    class_total_grade += student_average

    print("Name:", student_name, "Midterm:", student_midterm,
          "Final:", student_final, "Average:", student_average)

print("The class average is:", class_total_grade / num_students)
