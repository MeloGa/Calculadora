
conta = input("Digite a operacao desejada (soma, sub, mult, div): ")

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if conta == "soma":
	resultado = int(numero1) + int(numero2)
if conta == "sub":
	resultado = int(numero1) - int(numero2)
if conta == "mult":
	resultado = int(numero1) * int(numero2)
if conta == "div":
	resultado = int(numero1) / int(numero2)
    
print("O resultado da conta é: " + str(resultado))