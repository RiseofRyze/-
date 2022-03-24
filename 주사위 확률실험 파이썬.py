import random as r   
def test(a,b,c):  #a 는 주사위 면의 갯수 b는 던질 횟수 c는 나오는 확률이 궁금한 수 ex)정육면체 주사위를 10번 던져서 6이 나올 확률이 궁금하다
     T = 0        #ex)6개의 면을 가진 주사위를 10번 던져서 3이 나올 확률이 궁금하다 => a에 6,b에 10,c에 3입력
     t = 0
     for i in range(b):
         t = t+1
         m = r.randint(1,a)
         if m==c:
             T=T+1
         P =T/t
         print("%d 번째 주사위 나온 값은 %d, %d(은)는 %d 번 던져 %d 번 나왔으니 %d분의 %d 즉 %f1 퍼센트의 확률로 나왔습니다" % (i+1,m,c,t,T,t,T,P*100))
         print("%d(이)가 나올 확률(%f) 곱하기 면의 갯수(%d)는 %f 퍼센트" %(c,P*100,a,P*a*100))   
     return P
test(6,1000,1)

