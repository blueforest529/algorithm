student = [_ for _ in range(1, 31)]
for i in range(28):
    person = int(input())
    if person in student:
        student.remove(person)
        
print(*student, sep='\n')