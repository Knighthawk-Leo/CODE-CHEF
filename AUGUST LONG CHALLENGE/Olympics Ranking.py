# cook your dish her
t=int(input())
for x in range (t):
    a=list(map(int,input().split()))
    te1=a[0]+a[1]+a[2]
    te2=a[3]+a[4]+a[5]
    if(te1>te2):
        print('1')
    else:
        print('2')
