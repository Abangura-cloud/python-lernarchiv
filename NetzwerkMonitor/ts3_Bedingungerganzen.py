zahlen = [1, 2, 3, 4, 5]
gerade_quadrate = []
for zahl in zahlen:
    if zahl % 2 == 0:
        gerade_quadrate.append(zahl ** 2)
        print(gerade_quadrate)
print("======================")
gerade_quadrate = [zahl ** 2 for zahl in zahlen if zahl % 2 == 0]
print(gerade_quadrate)
