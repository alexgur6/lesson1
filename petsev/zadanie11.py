melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455,'Si': 1415, 'Be': 1287}

element1 = input()
element2 = input()
temperature_diff = melt[element1] - melt[element2]

print(abs(temperature_diff))