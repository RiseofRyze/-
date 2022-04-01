def quadratic_formula(a,b,c):  #a는 x제곱의 계수,b는 x의 계수,c는 상수항
    D = b**2-4*a*c
    d = D**0.5
    r1 =(-b+d)/2*a
    r2 =(-b-d)/2*a
    print(r1,r2)
    if D==0:
        print("이 식은 중근을 가지고, 근은 %s입니다." %(r1))
    elif D>0:
        print("이 식은 서로 다른 두 근을 가지고, 근은 %s와 %s입니다." %(f"{r1:.2f}",f"{r2:.2f}"))
    else:
        print("이 식은 허근을 가지고, 근은 %s와 %s입니다." %(f"{r1:.2f}",f"{r2:.2f}"))
quadratic_formula(8,2,8)