# -*- coding: utf-8 -*-
INPUT = input().split(" ")
A = float(INPUT[0])
B = float(INPUT[1])
C = float(INPUT[2])

if (A + B) <= C or (A + C) <= B or (B + C) <= A:
  AREA = (A + B) * C / 2
  print(f"Area = {AREA:.1f}")
else:
  PERIMETRO = A + B + C
  print(f"Perimetro = {PERIMETRO:.1f}")
