# -*- coding: utf-8 -*-
N = int(input())

for _ in range(N):
  testeCases = [int(n) for n in input().split(" ")]
  X = min(testeCases)
  Y = max(testeCases)
  sum = 0
  for j in range(X + 1, Y):
    if j % 2 != 0:
      sum += j
  print(sum)
