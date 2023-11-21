O = input()
SUM = 0

for i in range(12):
  for j in range(12):
    NUM = float(input())
    if (j > i):
      SUM += NUM

if (O == "S"):
  print("{:.1f}".format(SUM))
else:
  print("{:.1f}".format(SUM / 66))
