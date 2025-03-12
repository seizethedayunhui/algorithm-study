N_list = []

N_list = list(map(int, input().split()))

for i in range(2, 10) :
    N = N_list[i-2] + N_list[i-1]
    N_list.append(N % 10)

for n in N_list :
    print(n, end=" ")
