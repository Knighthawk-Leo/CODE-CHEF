# cook your code here
t=int(input())
for x in range (t):
    r=int(input())
    if(r<1600):
        print('3')
    elif(1600<=r and r<2000):
        print('2')
    elif(r>=2000):
        print('1')
