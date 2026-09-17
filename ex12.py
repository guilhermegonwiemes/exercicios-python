lista = []
while True:
  num = int(input('Digite um número: '))
  if(num != 0):
    lista.append(num)
  else:
    break

print(f'A soma total é: {sum(lista)}')