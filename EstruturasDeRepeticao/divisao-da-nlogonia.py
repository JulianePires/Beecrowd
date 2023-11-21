# -*- coding: utf-8 -*-
N = int(input())

while N != 0:
  divisas = [int(n) for n in input().split(" ")]
  divisaX = divisas[0]
  divisaY = divisas[1]
  for i in range(N):
    coordenadas = [int(n) for n in input().split(" ")]
    X = coordenadas[0]
    Y = coordenadas[1]
    if divisaX == X or divisaY == Y:
      print("divisa")
    elif divisaX > X and divisaY < Y:
      print("NO")
    elif divisaX > X and divisaY > Y:
      print("SO")
    elif divisaX < X and divisaY > Y:
      print("SE")
    else:
      print("NE")
  N = int(input())
