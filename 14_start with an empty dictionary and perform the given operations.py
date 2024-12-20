students_scores={}
students_scores['Muneeb']=90
students_scores['Ahmad']=88
students_scores['Islam']=95
print('After adding 3 students:',students_scores)

students_scores['Ahmad']=96
print("After updating Ahmad's score:",students_scores)
del students_scores['Muneeb']
print('After removing charlie:',students_scores)
score=students_scores.get('Ahmad','Not found')
print("Ahmad's score:",score)
score_non_existant=students_scores.get('Muneeb','Not found')
print("Muneeb's score:",score_non_existant)