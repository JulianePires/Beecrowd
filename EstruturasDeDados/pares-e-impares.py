qtd = int(input())
pares = []
impares = []

for _ in range(qtd):
  n = int(input())
  if (n % 2 == 0):
    pares.append(n)
  else:
    impares.append(n)

pares.sort()
impares.sort(reverse=True)

for p in pares:
  print(p)

for i in impares:
  print(i)
