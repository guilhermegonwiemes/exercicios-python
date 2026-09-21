print(f'\n{10 * "=-"} Par ou Ímpar {10 * "-="}')

num = int(input('Digite um número (inteiro): '))

if (num % 2 == 0):
  print(f'{num} é par!')
else:
  print(f'{num} é ímpar!')