print(f'\n{10 * "=-"} Calculadora de Preços {10 * "-="}')

preco = float(input('Preço do item: '))
quantidade = int(input('Quantidade do item: R$'))
total = preco * quantidade

print(f'Ao comprar {quantidade} produtos de R${preco}, você gasta um total de R${total:.2f}')