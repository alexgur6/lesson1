melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}

# Отфильтровать словарь для получения только оксидов
oxid = {compound: temperature for compound, temperature in melt.items() if 'O' in compound}

# Получить температуры плавления оксидов в виде строки, разделенной пробелами
melt_temp = ' '.join(map(str, oxid.values()))

print(melt_temp)
