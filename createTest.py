import matplotlib.pyplot as plt
y_values = []
x_values = []

# read the data from the text file
with open('smooth2001txt', 'r') as f:
        for l in f.readlines() :
                y_values.append(float(l.split(',')[1]))
                x_values.append(float(l.split(',')[0]))
y_values2=y_values
# plot the data
plt.plot(y_values)
print(y_values)
# show the plot
#plt.show()

import random 

# Rastgele 5 indeks seç
selected_indices = random.sample(range(len(y_values)), 100)

# Her bir seçilen indeks için değeri mevcut değerinden 2 farklı bir şekilde değiştir
for index in selected_indices:
    current_value = y_values[index]
    new_value = current_value + random.uniform(-3, 3) #random.choice([-0.3, 0.3])
    y_values[index] = new_value

# Değiştirilmiş y_values dizisini yazdır
print("Değiştirilmiş y_values:", y_values)


plt.plot(y_values)
plt.show()