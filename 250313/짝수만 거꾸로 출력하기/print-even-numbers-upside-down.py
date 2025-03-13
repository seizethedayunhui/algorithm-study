N = int(input())

N_list = list(map(int, input().split()))

for i in range(N-1,-1,-1) :
    if( N_list[i] % 2 == 0 ) :
        print(N_list[i], end=' ')