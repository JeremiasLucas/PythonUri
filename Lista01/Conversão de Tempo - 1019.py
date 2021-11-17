si = (int(input()))
horas = si // 3600
minutos = si % 3600 // 60
segundos = si % 60
print("%d:%d:%d"%(horas, minutos, segundos))
