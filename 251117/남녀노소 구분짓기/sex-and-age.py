a = int(input())
b = int(input())


# 남자는 0 여자는 1 
# 19세 이상은 성인 

if a == 1: # 여자일 경우 
    if b >= 19: # 성인
        print('WOMAN')
    else: 
        print('GIRL')
if a != 1: # 남자일 경우 
    if b >= 19: # 성인
        print('MAN')
    else: 
        print('BOY')