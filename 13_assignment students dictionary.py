students_scores={'Kamran':92,'Muneeb':88,'Islam':94}
student_name='Muneeb'
if student_name in students_scores:
    print(f'The score of {student_name} is: {students_scores[student_name]}')
else:
    print(f'Student {student_name} not found in the dictionary.')