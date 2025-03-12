A_score1, A_score2 = map(int, input().split())
B_score1, B_score2 = map(int, input().split())

if ( A_score1 > B_score1 ) and ( A_score2 > B_score2 ):
    print(1)
else :
    print(0)