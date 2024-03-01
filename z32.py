#












































































































def low_pass_filter(filename, threshold):
    with open(filename, 'r') as file:
        lines = file.readlines()

    filtered_freqs = []

    for line in lines:
        freqs = [float(freq) for freq in line.strip().split(';')]
        filtered_freqs.extend([f for f in freqs if f >= threshold])

    result_str = ' '.join(map(str, filtered_freqs))
    return result_str

# Пример использования:
threshold = 11.0
filtered_output = low_pass_filter('freqs.txt', threshold)
print(filtered_output)
