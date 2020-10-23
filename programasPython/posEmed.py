y = 0
media = 0
for i in range(6):
    x = float(input())
    if x > 0:
        y = y + 1
        media = media + x
mediaf = media / y
print("{} valores positivos".format(y))
print("{:.1f}".format(mediaf))
