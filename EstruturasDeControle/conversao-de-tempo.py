N = int(input())


def convert(n):
  min, sec = divmod(n, 60)
  hour, min = divmod(min, 60)
  return f"{hour}:{min}:{sec}"


print(convert(N))
