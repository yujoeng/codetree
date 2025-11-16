a, b = input().split()
c, d = input().split()

age1 = int(a)
age2 = int(c)
gender1 = str(b)
gender2 = str(d)


# 첫 번째 줄에 두 사람중 한 사람이라도 19세 이상이면서 남자라면 1을 출력합니다
# 문제의 조건에 해당하지 않는다면 0을 출력합니다
# print(age, sex)
if age1 >= 19 and gender1 == 'M':
    print('1')
else: 
    print('0')