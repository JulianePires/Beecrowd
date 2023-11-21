# -*- coding: utf-8 -*-
INPUT = input().split(" ")
X = float(INPUT[0])
Y = float(INPUT[1])

if X == 0 and Y == 0:
  print("Origem")
elif X == 0:
  print("Eixo Y")
elif Y == 0:
  print("Eixo X")
elif X > 0 and Y > 0:
  print("Q1")
elif X < 0 and Y > 0:
  print("Q2")
elif X < 0 and Y < 0:
  print("Q3")
elif X > 0 and Y < 0:
  print("Q4")
