n = int(input())
s = set(map(int, input().split()))
N = int(input())
sum = 0
for i in range(N):
    temp = input().split(' ')
    if temp[0] == 'pop':
        s.pop()
    elif temp[0] == 'discard':
        s.discard(int(temp[1]))
    elif temp[0] == 'remove':
        s.remove(int(temp[1]))
for i in s:
    sum += i
print(sum)
