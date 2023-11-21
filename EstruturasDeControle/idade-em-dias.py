# -*- coding: utf-8 -*-
N = int(input())

anos, meses = divmod(N, 365)
meses, dias = divmod(meses, 30)

print("%i ano(s)" % anos)
print("%i mes(es)" % meses)
print("%i dia(s)" % dias)
