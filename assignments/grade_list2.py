print("Enter done to exit.")

student_names = []
student_midterms = []
student_finals = []
student_averages = []

while True:
    student_name = input("Please enter name: ")
    if student_name == 'done':
        break
    student_names.append(student_name)
    student_midterm = float(input("Please enter midterm: "))
    student_midterms.append(student_midterm)
    student_final = float(input("Please enter final: "))
    student_finals.append(student_final)

    student_average = (student_midterm + student_final) / 2
    student_averages.append(student_average)

class_average = sum(student_averages) / len(student_names)
for i in range(len(student_names)):
    print("Name:", student_names[i], "Midterm:", student_midterms[i],
          "Final:", student_finals[i], "Average:", student_averages[i], "---",
          format(abs(student_averages[i] - class_average), "2.2f"), 
          (student_averages[i] - class_average >= 0) * "above class average",
          (student_averages[i] - class_average < 0) * "below class average")

print("The class average is:", format(class_average, "2.2f"))
