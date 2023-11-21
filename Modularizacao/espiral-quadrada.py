from math import floor


def imprime_matriz(matriz):
  for i in matriz:
    print("".join(i))
  print("@")


def espiral_quadrada(N):
  MATRIZ = [['O' for i in range(N)] for j in range(N)]
  AUX = [['O' for i in range(N)] for j in range(N)]
  x, y = int(floor(N / 2)), int(floor(N / 2))
  dir = 'direita'  #direita, cima, esquerda, baixo

  MATRIZ[int(floor(N / 2))][int(floor(N / 2))] = "X"
  AUX[int(floor(N / 2))][int(floor(N / 2))] = "X"

  for _ in range(N * N):
    imprime_matriz(MATRIZ)
    MATRIZ[x][y] = "O"
    if dir == 'direita':
      if y + 1 <= N - 1:
        y += 1
        if AUX[x - 1][y] == "O":
          dir = 'cima'
      else:
        dir = 'cima'
    elif dir == 'cima':
      if x >= 0:
        x -= 1
        if AUX[x][y - 1] == "O":
          dir = 'esquerda'
      else:
        dir = 'esquerda'
    elif dir == 'esquerda':
      if y >= 0:
        y -= 1
        if AUX[x + 1][y] == "O":
          dir = 'baixo'
      else:
        dir = 'baixo'
    else:
      if x <= N - 1:
        x += 1
        if AUX[x][y + 1] == "O":
          dir = 'direita'
      else:
        dir = 'direita'

    MATRIZ[x][y] = 'X'
    AUX[x][y] = 'X'


while True:
  N = int(input())
  if N == 0:
    break
  elif N == 1:
    print("X\n@")
  else:
    espiral_quadrada(N)
