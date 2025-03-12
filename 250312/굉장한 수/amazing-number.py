N = int(input())

condition1 = ( N % 2 ) and ( N % 3 == 0 )
condition2 = ( N % 2 == 0 ) and ( N % 5 == 0 )

if condition1 or condition2 :
    print("true")
else :
    print("false")