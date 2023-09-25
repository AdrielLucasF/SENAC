n = int(input("Digite o valor que deseja: "))
soma = 0

while n >= 2:
    if n % 2 == 0:
        soma += n
    n -= 1

print("A soma dos números pares de 1 a", n, "é:", soma)
