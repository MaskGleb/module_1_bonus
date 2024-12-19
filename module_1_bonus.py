grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
average=grades
a=list(sorted(students))
for i in range(0,5):
    average[i]=sum(grades[i]) / len(grades[i])
teacher_dict=dict(zip(a,average))
print(teacher_dict)