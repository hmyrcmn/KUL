import os
import matplotlib.pyplot as plt

# Klasör yolu tanımlamaları
true_path = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\BigData\\newData\\trueVal'
false_path = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\BigData\\newData\\falseVal'

# Gerçeklerin ve yanlışların dosya isimlerini listeleme
true_files = [filename for filename in os.listdir(true_path) if filename.endswith('.txt')]
false_files = [filename for filename in os.listdir(false_path) if filename.endswith('.txt')]

# Tüm x ve y değerlerini saklamak için listeler
true_x_values = []
true_y_values = []
false_x_values = []
false_y_values = []

# Gerçek verileri okuma
for file_name in true_files:
    x_values = []
    y_values = []

    file_path = os.path.join(true_path, file_name)

    with open(file_path, 'r') as f:
        for line in f.readlines():
            x_values.append(float(line.split(',')[0]))
            y_values.append(float(line.split(',')[1]))

    true_x_values.append(x_values)
    true_y_values.append(y_values)

# Yanlış verileri okuma
for file_name in false_files:
    x_values = []
    y_values = []

    file_path = os.path.join(false_path, file_name)

    with open(file_path, 'r') as f:
        for line in f.readlines():
            x_values.append(float(line.split(',')[0]))
            y_values.append(float(line.split(',')[1]))

    false_x_values.append(x_values)
    false_y_values.append(y_values)

# Veriyi çizme
plt.figure(figsize=(10, 6))

# Gerçekleri mavi renkte çizme
for x_values, y_values in zip(true_x_values, true_y_values):
    plt.plot(x_values, y_values, color='blue', label='True Data')

# Yanlışları kırmızı renkte çizme
for x_values, y_values in zip(false_x_values, false_y_values):
    plt.plot(x_values, y_values, color='red', label='False Data')

plt.title('Gerçek ve Yanlış Verilerin Görselleştirilmesi')
plt.xlabel('X Değerleri')
plt.ylabel('Y Değerleri')
plt.xlim(0, 1000)
plt.ylim(0, 250)
plt.grid(True)
# plt.legend()
plt.show()
