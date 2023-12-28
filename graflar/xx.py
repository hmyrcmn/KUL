import numpy as np
import matplotlib.pyplot as plt

# Dosya yollarını tam olarak belirt
bir = 'C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\graflar\\norm\\s1.txt'
iki = "C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\graflar\\norm\\s2.txt"
uc = "C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\graflar\\norm\\sen1.txt"
dort = "C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\graflar\\norm\\sen2.txt"
# bes="C:\\Users\\HÜMEYRA\\Documents\\GitHub\KUL\\graflar\\norm\\s1.txt"
# alti="C:\\Users\\HÜMEYRA\\Documents\\GitHub\KUL\\graflar\\norm\\s2.txt"
# İlk metin dosyasından veriyi yükle
data1 = np.genfromtxt(bir, delimiter=',')
y_values1 = data1[:, 1]

# İkinci metin dosyasından veriyi yükle
data2 = np.genfromtxt(iki, delimiter=',')
y_values2 = data2[:, 1]

data3 = np.genfromtxt(uc, delimiter=',')
y_values3 = data3[:, 1]

data4 = np.genfromtxt(dort, delimiter=',')
y_values4 = data4[:, 1]

# data5 = np.genfromtxt(dort, delimiter=',')
# y_values5 = data5[:, 1]
# data6 = np.genfromtxt(dort, delimiter=',')
# y_values6 = data6[:, 1]

# İki dosyadan gelen veriyi aynı grafik üzerine çiz
# plt.plot(y_values1, label='EBS SEL-1 ON /OF ')
plt.plot(y_values2, label='EBS SEL-2 ON /OF ')
# plt.plot(y_values3, label='EBS SEN-1 VOLT ')
# plt.plot(y_values4, label='EBS SEN-3 VOLT')
# plt.plot(y_values5, label='s1')
# plt.plot(y_values6, label='s2')

# plt.plot(y_values5, label='atm basınc')
 # ebs bascın,
 # ebs sel1,  on of 
 #ebs sel2 , sen1,sen2( volt ),sen3,sen4,(bar )
 #input(bar) vol ,on-of , current1 current2 


# Etiket ve başlık ekle
plt.xlabel('EBS SEL- ')
plt.ylabel('ON -OFF ')
# Izgara ekle
plt.grid(True)
plt.title('EBS SEL-2')
plt.legend()
plt.show()
