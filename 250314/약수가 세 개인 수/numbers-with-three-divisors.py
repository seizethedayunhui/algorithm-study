start, end = map(int, input().split())

ans = 0

for n in range(start, end+1 ) :
    cnt = 0
    for i in range(1, n+1) :
        if not n % i :
            cnt += 1
    if cnt == 3 :
        ans += 1
print( ans )
