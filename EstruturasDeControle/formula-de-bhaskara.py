# -*- coding: utf-8 -*-
INPUT = input().split(" ")
A = float(INPUT[0])
B = float(INPUT[1])
C = float(INPUT[2])

delta = B**2 - 4 * A * C

if 2 * A == 0 or delta < 0:
  print("Impossivel calcular")
else:
  x1 = (-B + (delta**0.5)) / (2 * A)
  x2 = (-B - (delta**0.5)) / (2 * A)
  print("R1 = %.5f" % x1)
  print("R2 = %.5f" % x2)
