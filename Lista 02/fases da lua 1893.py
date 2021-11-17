valor_1,valor_2 = input().split()
valor_1 = int(valor_1)
valor_2 = int(valor_2)
if(valor_2 <= 2 and valor_1 >= 0):
    print("nova")
elif(valor_2 <= 100 and valor_2 >= 97):
    print("cheia")
elif(valor_2 > valor_1):
    print("crescente")
else:
    print("minguante")
