N_list = []

for i in range(10):
    N_list.append(int(input()))

cnt_three = 0
cnt_five = 0

for n in N_list :
    if ( n % 3 == 0 ) :
        cnt_three += 1
    if ( n % 5 == 0 ) :
        cnt_five += 1

print(cnt_three, cnt_five)