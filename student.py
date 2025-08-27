# Leia uma linha com o número do cartão
numero = input()
impares = []
for i in numeros numeros[-1::-2]:
  impares.append(int(1))
pares = []
for i in numeros[-2::-2]:
  if 2*int(i) < 10:
    pares.append(2*int(i))
  else:
    pares.append(2*int(i)-10+1)
soma = sum(pares) + sum(impares)
if int(soma/10) == soma/10:
  print("Cartão válído")
else:
  print("Cartão inválido")

