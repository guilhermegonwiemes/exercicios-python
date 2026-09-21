media = float(input('Digite a média de nota do seu estudante: '))

if(media < 4):
  print('O estudante está reprovado!')
elif(media < 6):
  print('O estudante está em recuperação!')
else:
  print('O estudante está aprovado!')