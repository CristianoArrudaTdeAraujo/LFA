total = 0
while total != 45:
    valor = int(input("Digite um valor: "))
    if valor == 10 or valor == 25:
        total += valor
    if total >= 45:
        print("Você recebeu uma Coca-cola")
        total = total - 45
    print("Total:", total)
