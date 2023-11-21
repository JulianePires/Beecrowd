# -*- coding: utf-8 -*-
while True:
  try:
    caracteres = input().strip()
    contador = 0
    correto = True
    for c in caracteres:
      if (c == '('):
        contador += 1
      elif (c == ')'):
        if (contador == 0):
          correto = False
          break
        else:
          contador -= 1
    correto = correto and contador == 0

    print("correct" if correto else "incorrect")
  except EOFError:
    break
