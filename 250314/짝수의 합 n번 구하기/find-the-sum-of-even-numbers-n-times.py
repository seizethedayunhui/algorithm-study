N = int(input())

for i in range(N) :

    a, b = map(int, input().split())
    sum = 0
    for n in range(a, b+1) :
        if not n % 2 :
            sum += n
    print(sum)