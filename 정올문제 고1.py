def ans():
    o = []
    T = int(input())
    z = []
    for i in range(T):
        z.append(str(input()))
    for i in range(T):
        N, M, k, D = str(z[i]).split()
        N = int(N) #지역리그의 갯수
        M = int(M) #지역리그 팀의 갯수
        k = int(k) #지역리그 팀당 경기수 = k * 다른 지역리그 팀과의 경기수
        D = int(D) #경기 수 제한
        R=[]
        for B in range(1000):
            B = B+1
            A = B*k
            h = N*(M*(M-1)*A)/2
            a = (M*((N-1)*M*N)*B)/2
            R.append(h+a)
            if B==1:
                d = h+a
            for c in R:
                if int(c)<=D:
                    r = c
        print(R)
        if d>D:
            r = -1
        else:
            r= int(r)
        o.append(r)
    for l in o:
        print(int(l))
ans()
