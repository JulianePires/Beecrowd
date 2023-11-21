def sortLen(val):
  return len(val)


TEST_CASES = int(input())
for _ in range(TEST_CASES):
  STRING = input()
  words = STRING.split(" ")
  words.sort(key=sortLen, reverse=True)
  print(" ".join(words))
