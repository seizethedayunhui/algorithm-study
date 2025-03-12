Y = int(input())

condition = Y % 4

if not condition :
    if ( Y % 100 ==0 ) and ( Y % 400 ) :
        print("false")
    else :
        print("true")
else :
    print("false")