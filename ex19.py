num = int(input('Digite um número: '))
fatorial = 1
for i in range(1, num + 1):
  fatorial *= i
print(f'O fatorial de \33[32m{num}\33[m é \33[32m{fatorial}\33[m')
# Queria ter feito com recursividade, mas a questão pede com for.. Se fosse com recursividade teria feito assim:
# def fatorial(num):
#   if(num == 0 or num == 1):
#     return 1
#   else:
#     return  num * fatorial(num - 1)

# num = int(input('Digite um numero: '))
# print(fatorial(num))