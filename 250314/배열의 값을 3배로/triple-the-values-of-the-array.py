N_list = [list(map(int, input().split())) for i in range(3)]

for i in range(3) :
    for j in range(3) :
        print( 3 * N_list[i][j], end = " ")
    print()