a, b, c = map(int, input().split())

min_num = min(a,b,c)
# print(min_num)
if a == min_num :
    print('1',end=" ")
elif a != min_num :
    print('0', end=" ")

if a == b == c :
    print('1')
else:
    print('0')