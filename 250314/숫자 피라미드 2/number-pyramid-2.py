N = int(input())

row = 1
i = 1

while ( row <= N ) :
    for _ in range(row) :
        print(i, end=" ")
        i += 1
    row += 1
    print
    print()