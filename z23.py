def my_filter(a):
    result = ' '.join(map(str, [int(x) * 10 for x in a]))
    return result

input_list = input("Введите числа через пробел: ").split()
output_string = my_filter(input_list)
print(output_string)
