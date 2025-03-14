n = int(input())
arr = [[0 for col in range(n)] for row in range(n)]

# 열기준 작성
for i in range(n) :

    # 짝수열일 때 그대로 작성
    if not i % 2 :
      for j in range(n) :
        arr[j][i] =  j + 1
    else :
      for j in range(n-1, -1, -1) :
        arr[n-j-1][i] = j + 1
    

for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end="")
    print()
    
