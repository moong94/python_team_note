n = int(input())

student = []

for _ in range(n):
    name, score = map(str,input().split())
    student.append((name,int(score)))

student.sort(key=lambda x:x[1])

for i in student:
    print(i[0], end=" ")
