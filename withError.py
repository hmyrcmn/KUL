import os
import random

# Klasördeki tüm txt dosyalarını al
folder_path = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\coordinateds2'
error_folder = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\falseValues5'

# İfadesiyle belirtilen klasörü oluştur
os.makedirs(error_folder, exist_ok=True)

file_names = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

for i in range(10000):
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
        
        # Rastgele 5 indeks seç
        error_num = random.randint(0, 50)#kac hata lı deger olsun 
        selected_indices = random.sample(range(len(y_values)), error_num)

        # Her bir seçilen indeks için y değeri rastgele bir şekilde değiştir
        for index in selected_indices:
            current_y_value = y_values[index]
            error_lim = random.randint(5,10)

            new_y_value = current_y_value + random.uniform(-error_lim, error_lim)
            y_values[index] = new_y_value
        
        # Dosya adını güncelle
        file_name = f"{file_name[:-4]}_{i}.txt"

        # Hatalı dosyayı aynı adla "errors" klasörüne kaydet
        error_file_path = os.path.join(error_folder, file_name)
        
        with open(error_file_path, 'w') as error_file:
            for x, y in zip(x_values, y_values):
                error_file.write(f'{x},{y}\n')

        print(f"Hatalı dosya kaydedildi: {error_file_path}")
