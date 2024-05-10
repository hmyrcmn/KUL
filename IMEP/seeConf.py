import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
# Dosyaların bulunduğu klasör yolu
true_klasor_yolu = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\BigData\\TrueValues'
false_klasor_yolu = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\BigData\\FalseValues'

# Klasördeki tüm .txt dosyalarının listesini al
true_dosya_isimleri = [dosya_adi for dosya_adi in os.listdir(true_klasor_yolu) if dosya_adi.endswith('.txt')]
false_dosya_isimleri = [dosya_adi for dosya_adi in os.listdir(false_klasor_yolu) if dosya_adi.endswith('.txt')]

# Korelasyon matrisini saklamak için
korelasyon_matrisi = np.zeros((len(true_dosya_isimleri), len(false_dosya_isimleri)))

# Her dosya çifti için korelasyon katsayısını hesapla
for i, true_dosya_adi in enumerate(true_dosya_isimleri):
    for j, false_dosya_adi in enumerate(false_dosya_isimleri):
        # True ve False dosyalarından veri okuma
        true_data = np.genfromtxt(os.path.join(true_klasor_yolu, true_dosya_adi))
        false_data = np.genfromtxt(os.path.join(false_klasor_yolu, false_dosya_adi))

        # Korelasyon katsayısını hesapla
        korelasyon = np.corrcoef(true_data, false_data)[0, 1]

        # Korelasyon matrisine kaydet
        korelasyon_matrisi[i, j] = korelasyon

# Korelasyon matrisini görselleştir (opsiyonel)
sns.heatmap(korelasyon_matrisi, annot=True)
plt.show()

import seaborn as sns

# Korelasyon matrisini görselleştir
sns.heatmap(korelasyon_matrisi, annot=True)

# Başlık ekle
plt.title('Korelasyon Matrisi')

# Eksen etiketleri ekle
plt.xlabel('True Dosyaları')
plt.ylabel('False Dosyaları')

# Renk çubuğu ekle
plt.colorbar()

# Görselleştirmeyi göster
plt.show()
