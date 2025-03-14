arr1 = [ list(map(int, input().split())) for _ in range(3) ]
garbage = input()
arr2 = [ list(map(int, input().split())) for _ in range(3) ]

for i in range(3) :
    for j in range(3) :
        ans = arr1[i][j] * arr2[i][j]
        print(ans, end=" ")
    print()
