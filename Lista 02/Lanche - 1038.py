codigo,quantidade= map(int, input().split())
xsalada=float(4.50*quantidade)
xbacon=float(5.00*quantidade)
torrada=float(2.00*quantidade)
cachorroqnt=float(4.00*quantidade)
refri=float(1.50*quantidade)
xsalada_formatado ="{:.2f}".format(xsalada)
xbacon_formatado ="{:.2f}".format(xbacon)
torrada_formatado ="{:.2f}".format(torrada)
cachorroqnt_formatado ="{:.2f}".format(cachorroqnt)
refri_formatado ="{:.2f}".format(refri)
if (codigo==1):
  print("Total: R$",(cachorroqnt_formatado))
if (codigo==2):
    print("Total: R$",(xsalada_formatado))
if (codigo==3):
    print("Total: R$",(xbacon_formatado))
if (codigo==4):
    print("Total: R$",(torrada_formatado))
if (codigo==5):
  print("Total: R$",(refri_formatado))
