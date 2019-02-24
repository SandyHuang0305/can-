#可否除掉？

num = int(input('請輸入一個數字:'))
if num%2 ==0:
    if num%3 ==0:
        print('你輸入的數字可以整除2和3')
    else:
        print('你輸入的數字可以整除2,但不能整除3')
else:
	if num%3 == 0:
		print('你輸入的數字可以整除3,但不能整除2')
	else:
	    print('你輸入的數字不能整除2和3')	