students_scores={'Muneeb':(85,90,88),'Kamran':(78,85,92),'Shahid':(92,94,90),'Saqib':(70,75,73)}
def calculate_averages(students_scores):
    for student,scores in students_scores.items():
        total_score=0
        subject_count=0
        for score in scores :
            total_score+=score
            subject_count+=1
        average_score=total_score/subject_count
        print(f"{student}'s average_score:{average_score:.2f}")
def highest_average_score(sudents_scores):
    highest_avg=-1
    top_student=""
    for student,scores in students_scores.items():
        total_score=0
        subject_count=0
        for score in scores:
            total_score+=score
            subject_count+=1
        average_score=total_score/subject_count
        if average_score>highest_avg:
            highest_avg=average_score
            top_student=student
    return top_student,highest_avg
print('Average Scores of Students:')
calculate_averages(students_scores)
top_student,highest_avg=highest_average_score(students_scores)
print(f"\nThe student with the hiighest average score is {top_student} with an average of {highest_avg:.2f}")
