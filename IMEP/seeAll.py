import os
import matplotlib.pyplot as plt

# Dosyaların bulunduğu klasör yolu
true_klasor_yolu = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\BigData\\newData\\trueVal'
false_klasor_yolu = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\BigData\\newData\\falseVal'

# Klasördeki tüm .txt dosyalarının listesini al
true_dosya_isimleri = [dosya_adi for dosya_adi in os.listdir(true_klasor_yolu) if dosya_adi.endswith('.txt')]
false_dosya_isimleri = [dosya_adi for dosya_adi in os.listdir(false_klasor_yolu) if dosya_adi.endswith('.txt')]

# Tüm dosyalardan x ve y değerlerini saklamak için listeler
tum_true_x_degerleri = []
tum_true_y_degerleri = []
tum_false_x_degerleri = []
tum_false_y_degerleri = []

# Her dosyayı işle
for dosya_adi in true_dosya_isimleri:
    x_degerleri = []  # Her dosya için x değerlerini saklamak için
    y_degerleri = []  # Her dosya için y değerlerini saklamak için

    dosya_yolu = os.path.join(true_klasor_yolu, dosya_adi)

    with open(dosya_yolu, 'r') as f:
        for satir in f.readlines():
            x_degerleri.append(float(satir.split(',')[0]))
            y_degerleri.append(float(satir.split(',')[1]))

    # x_degerleri ve y_degerleri'ni listelere ekle
    tum_true_x_degerleri.append(x_degerleri)
    tum_true_y_degerleri.append(y_degerleri)

# Her dosyayı işle
for dosya_adi in false_dosya_isimleri:
    x_degerleri = []  # Her dosya için x değerlerini saklamak için
    y_degerleri = []  # Her dosya için y değerlerini saklamak için

    dosya_yolu = os.path.join(false_klasor_yolu, dosya_adi)

    with open(dosya_yolu, 'r') as f:
        for satir in f.readlines():
            x_degerleri.append(float(satir.split(',')[0]))
            y_degerleri.append(float(satir.split(',')[1]))

    # x_degerleri ve y_degerleri'ni listelere ekle
    tum_false_x_degerleri.append(x_degerleri)
    tum_false_y_degerleri.append(y_degerleri)

# Verileri çiz
plt.figure(figsize=(10, 6))

# True verileri çiz
for x_degerleri, y_degerleri in zip(tum_true_x_degerleri, tum_true_y_degerleri):
    plt.plot(x_degerleri, y_degerleri, label=f'{dosya_adi} dosyasından veri (Doğru)')

# False verileri çiz
for x_degerleri, y_degerleri in zip(tum_false_x_degerleri, tum_false_y_degerleri):
    plt.plot(x_degerleri, y_degerleri, label=f'{dosya_adi} dosyasından veri (Yanıltma)')

plt.title('Veri Görselleştirme Yanıltma Testi')
plt.xlabel('X Değerleri')
plt.ylabel('Y Değerleri')
plt.xlim(0, 1000)
plt.ylim(0, 250)
plt.legend()
plt.show()
