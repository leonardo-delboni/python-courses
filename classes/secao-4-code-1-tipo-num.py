# SEÇÃO 4 - TIPO NUMÉRICO

# PARA SABER O TIPO DA VARÍAVEL -> type(variavel)
# OBS: CTRL + L limpa o console

print("Insira dois números à sua escolha.")
print("Primeiro número:")
num1 = int(input())
print("Segundo número:")
num2 = int(input())

soma = num1 + num2
print("A soma é de {0}".format(soma))
diferenca = num1 - num2
print("A diferença é de {0}".format(diferenca))
multiplicacao = num1*num2
print("A multiplicação é de {0}".format(multiplicacao))
divisao_float = num1/num2
print("A divisão (tipo float) é de {0}".format(divisao_float))
divisao_int = num1//num2
print("A divisão (tipo int) é de {0}".format(divisao_int))
resto_divisao = num1 % num2
print("O resto da divisão é de {0}".format(resto_divisao))
potencia = num1 ** num2
print("A potência é de {0}".format(potencia))

print("Somando 1 ao valor do primeiro input por dois métodos diferentes:")
aux1 = num1
aux2 = num1
aux1 = aux1 + 1 # 1º Método
print(aux1)
aux2 += 1       # 2º Método
print(aux2)

print("Subtraindo 1 ao valor do primeiro input por dois métodos diferentes:")
aux3 = num1
aux4 = num1
aux3 = aux3 - 1 # 1º Método
print(aux3)
aux4 -= 1       # 2º Método
print(aux4)

print("Multiplicando ambos os inputs por dois métodos diferentes:")
aux5 = num1
aux6 = num1
aux5 *= num2    # 1º Método
print(aux5)
aux6 = aux6 * num2
print(aux6)

print("Dividindo ambos os inputs por dois métodos diferentes:")
aux7 = num1
aux8 = num1
aux7 //= num2    # 1º Método
print(aux7)
aux8 = aux8 // num2
print(aux8)

# PARA SABER O TIPO DA VARÍAVEL -> type(variavel)
aux9 = type(num1)
aux10 = type(num2)
print("O tipo do primeiro input é {0} e o do segundo é {1}".format(aux9, aux10))
