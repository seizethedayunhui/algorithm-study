A, B = input().split()

flag = len(A) - len(B)

if flag > 0 :
    print(A, len(A))
elif flag < 0 :
    print(B, len(B))
else :
    print("same")
