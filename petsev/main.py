room = int(input())
podezd=1
etaj = room
while etaj > 8:
    etaj = etaj - 8
    podezd += 1
else:
    print(etaj)
print(podezd)
