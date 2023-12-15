import os
import matplotlib.pyplot as plt

# Klasördeki tüm txt dosyalarını al
folder_path = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\falseValues'

file_names = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Her bir txt dosyasını oku ve ayrı ayrı çiz
for file_name in file_names:
    x_values = []
    y_values = []

    # Dosyadan veriyi oku
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as f:
        for line in f.readlines():
            x, y = map(float, line.split(','))
            x_values.append(x)
            y_values.append(y)

    # Ayrı ayrı çizgi olarak çizimi
    plt.plot(x_values, y_values, label=file_name)

# Grafik özellikleri
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')
plt.title('Her TXT Dosyasındaki Verilerin Ayrı Ayrı Grafikleri')
plt.legend()
plt.show()
