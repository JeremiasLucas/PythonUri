x,y = map(int,input().split())
l1,h1 = map(int,input().split())
l2,h2 = map(int,input().split())
if (l1+l2<=x and h1<=y and h2<=y):
    print("S")
elif (h1+l2<=x and l1<=y and h2<=y):
    print("S")
elif (h1+h2<=x and l1<=y and l2<=y):
    print("S")
elif (l1+h2<=x and h1<=y and l2<=y):
    print("S")
elif (l1+l2<=y and h1<=x and h2<=x):
    print("S")
elif (h1+l2<=y and l1<=x and h2<=x):
    print("S")
elif (h1+h2<=y and l1<=x and l2<=x):
    print("S")
elif (l1+h2<=y and h1<=x and l2<=x):
    print("S")
else:
    print("N")
