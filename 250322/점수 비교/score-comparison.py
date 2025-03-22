a=input().split()
b=input().split()

a_math_score=int(a[0])
a_english_score=int(a[1])
b_math_score=int(b[0])
b_english_score=int(b[1])

if a_math_score>b_math_score and a_english_score>b_english_score:
    print(1)
else:
    print(0)