x = ""
def pol_color(pol):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

    letter = pol[0]
    number = pol[1]

    if (letters.index(letter) + numbers.index(number)) % 2 == 0:
        return "black"
    else:
        return "white"

#enjoy

def cell_color(cell_number, cell_letter):
    if (cell_number % 2 == 0 and ord(cell_letter) % 2 == 0) or (cell_number % 2 != 0 and ord(cell_letter) % 2 != 0):
        return "черный"
    else:
        return "белый"

cell_number = int(input("Введите номер клетки (1-8): "))
cell_letter = input("Введите букву клетки (a-h): ")

if cell_number < 1 or cell_number > 8 or ord(cell_letter) < 97 or ord(cell_letter) > 104:
    print("Некорректные данные")
else:
    color = cell_color(cell_number, cell_letter)
    print(f"Цвет клетки {cell_letter}{cell_number} - {color}")


