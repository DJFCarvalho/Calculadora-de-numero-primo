"""        Calculadora de números primos      
Autor: DJFCarvalho
"""
print("Essa calculadora tem como objetivo verificar se um número é primo ou não, dentro de um intervalo de números definido pelo usuário, informando a quantidade e os números primos encontrados nesse intervalo.")
print()
num1 = int(input("Digite o primeiro número do intervalo: "))
num2 = int(input("Digite o segundo número do intervalo: "))
vetor = []
qtd = int(0)

while num1 <= num2:
  if num1 < 2:
    num1 = num1 + 1
  else:
    is_prime = True
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0:
            is_prime = False
            break
    if is_prime:
        vetor.append(num1)
        num1 = num1 + 1
        qtd = qtd + 1
    else:
        num1 = num1 + 1
print(f"A quantidade de números primos encontrados no intervalo é: {qtd} e são eles: {vetor}")
