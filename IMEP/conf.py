import numpy as np
import os
import scipy.stats

# Klasörlerin yolları
true_klasor_yolu = "/content/KUL/BigData/TrueValues/"
false_klasor_yolu = "/content/KUL/BigData/FalseValues/"

# Korelasyon matrislerini saklamak için boş matrisler oluşturma
pearson_matrisi = np.zeros((len(os.listdir(true_klasor_yolu)), len(os.listdir(false_klasor_yolu))))
spearman_matrisi = np.zeros((len(os.listdir(true_klasor_yolu)), len(os.listdir(false_klasor_yolu))))
kendall_matrisi = np.zeros((len(os.listdir(true_klasor_yolu)), len(os.listdir(false_klasor_yolu))))

say=0
say2=0
while(say<5):
        say+=1
                # Her True ve False dosya çifti için korelasyon katsayılarını hesaplama
        for i, true_dosya_adi in enumerate(os.listdir(true_klasor_yolu)):
                for j, false_dosya_adi in enumerate(os.listdir(false_klasor_yolu)):
                        while(say2<5):
                                say2+=1
                                        # True ve False dosyalarından veri okuma
                                true_data = np.genfromtxt(os.path.join(true_klasor_yolu, true_dosya_adi), delimiter=',')[:, 1:]
                                false_data = np.genfromtxt(os.path.join(false_klasor_yolu, false_dosya_adi), delimiter=',')[:, 1:]

                                # Korelasyon katsayılarını hesaplama
                                pearson_corr = np.corrcoef(true_data, false_data)[0, 1]
                                spearman_corr = scipy.stats.spearmanr(true_data, false_data)[0]
                                kendall_corr = scipy.stats.kendalltau(true_data, false_data)[0]


                                # Korelasyon matrislerine kaydetme
                                pearson_matrisi[i, j] = pearson_corr
                                spearman_matrisi[i, j] = spearman_corr
                                kendall_matrisi[i, j] = kendall_corr
                                print("1:",pearson_matrisi)


# Korelasyon matrislerini yazdırma
print("Pearson Korelasyon Matrisi:")
print(pearson_matrisi)

print("Spearman's Rank Korelasyon Matrisi:")
print(spearman_matrisi)

print("Kendall Tau Korelasyon Matrisi:")
print(kendall_matrisi)
