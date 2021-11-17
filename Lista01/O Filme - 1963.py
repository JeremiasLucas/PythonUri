a,b = input().split()
a = float(a)
b = float(b)
aumento = ((b * 100) / a) - 100.00
aumento_formatado = "{:.2f}".format(aumento)
print(aumento_formatado,"%",sep="")
