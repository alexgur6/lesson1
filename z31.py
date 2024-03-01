#




























































def write(filename, data):
    file = open(filename, 'w')
    for time, value in data:
        file.write(f"{time}\t{value}\n")
    file.close()

# Пример использования:
filename = "1.txt"
data = [(1, 20), (2, 30), (3, 40), (4, 35), (5, 22), (6, 10)]

write(filename, data)
