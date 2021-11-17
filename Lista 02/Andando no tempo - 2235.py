a,b,c = map(int,input().split())
if a + b == c or a == b + c or b == a + c or a == b or a == c or b == c:
    print("S")
else:
    print("N")
