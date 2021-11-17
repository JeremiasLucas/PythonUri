andar_1 = int (input())
andar_2 = int (input())
andar_3 = int (input())
tempo_1 = andar_1*0 + andar_2*2 + andar_3*4
tempo_2 = andar_1*2 + andar_2*0 + andar_3*2
tempo_3 = andar_1*4 + andar_2*2 + andar_3*0
if(tempo_1<=tempo_2):
  menor = tempo_1
else:
  menor = tempo_2
if(menor >= tempo_3):
  menor = tempo_3
print (menor)
