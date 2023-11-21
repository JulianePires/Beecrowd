LINE_REF = int(input())
OP = input()
M = []
SUM = 0

for i in range(12):
  line = []
  for j in range(12):
    NUM = float(input())
    line += [NUM]
    if (i == LINE_REF):
      SUM += NUM
  M += [line]

if (OP == "S"):
  print("{:.1f}".format(SUM))
elif (OP == "M"):
  print("{:.1f}".format(SUM / 12))
