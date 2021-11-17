X = (int(input()))
Y = (float(input()))
Y_formatado =(float ("{:.1f}".format(Y)))
cm = (float(X/Y_formatado))
cm_formatado = "{:.3f}".format(cm)
print(cm_formatado,"km/l")
     
