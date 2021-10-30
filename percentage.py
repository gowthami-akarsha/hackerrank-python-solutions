# Finding the percentage
n = int(input())
student_marks = {}
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
  query_name = input()
  student_marks[query_name]
  sum = 0
  for i in student_marks[query_name]:
    sum += i
    res =sum/len(student_marks[query_name])
    format_float = '{:.2f}'.format(res)
    print(format_float)


