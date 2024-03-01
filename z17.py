def pol_color(pol):
    column, row = pol[0], int(pol[1])
    
   
    if (ord(column) - ord('a') + row) % 2 == 0:
        return "black"
    else:
        return "white"

# Пример использования:
pol = input()
color = pol_color(pol)
print(color)
