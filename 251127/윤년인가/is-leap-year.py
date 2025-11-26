# 자연수 Y 를 입력받아 
y = int(input())
# y가 윤년인지 아닌지 판단하는 프로그램

'''
# 4로 나누어 떨어지는 해는 윤년 
if y % 4 == 0:
    print('true')
# 4로 나누어 떨어지지 않는 해 평년 
else:
    # 예외적으로 100으로 나누어 떨어지지만, 400으로 나눠지지 않는 해는 평년
    if y % 100 == 0 and y % 400 == 0 :
        print('true')
    elif y % 100 == 0 and y % 400 != 0 :
        print('false')
'''
    
# 4로 나누어 떨어지지 않는 해는 평년
if y % 4 != 0:
    print('false')
else: 
    if y % 100 == 0 and y % 400 == 0 :
        print('true')
    elif y % 100 == 0 and y % 400 != 0 :
        print('false')