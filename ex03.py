print(f'\n\n{10 * "=-"} Calculadora de Área de Círculo {10 * "=-"}')

raio = float(input("\nDigite o raio do círculo (cm): "))
area = 3.14159 * (raio ** 2)
print(f"A área do círculo de raio {raio} é: {area:.2f} cm².")