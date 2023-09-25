n = int(input("Digite o valor que deseja: "))
soma = 0

numero = 1
while numero <= n:
    if numero % 2 == 0:
        soma += numero
    numero += 1

print("A soma dos números pares de 1 a", n, "é:", soma)

