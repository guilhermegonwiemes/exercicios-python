positivos = []
while True:
  num = float(input('Digite um número: '))
  if (num > 0):
    positivos.append(num)
  if(num == 0):
    break
print(f'\nForam digitados \33[32m{len(positivos)}\33[m números positivos.\n')