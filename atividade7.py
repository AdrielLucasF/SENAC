numero = int(input("Digite um número para calcular o fatorial: "))

if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    fatorial = 1
    i = 2
    while i <= numero:
        fatorial *= i
        i += 1
    print(numero, "!", " = ", fatorial)
