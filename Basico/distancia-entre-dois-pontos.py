import math

linhaDado1 = input().split(" ")
linhaDado2 = input().split(" ")

x1 = float(linhaDado1[0])
y1 = float(linhaDado1[1])
x2 = float(linhaDado2[0])
y2 = float(linhaDado2[1])

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("{:.4f}".format(distancia))
