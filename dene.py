import numpy as np
import matplotlib.pyplot as plt

# Define the paths to your text files
true = 'C:\\Users\\HÜMEYRA\Documents\\GitHub\KUL\data\\trueValues\\smooth2001_0.txt'
false = 'C:\\Users\\HÜMEYRA\Documents\\GitHub\KUL\data\\falseValues\\smooth2001_0.txt'
true1 = 'C:\\Users\\HÜMEYRA\Documents\\GitHub\KUL\data\\trueValues\\smooth2001_10.txt'
false1 = 'C:\\Users\\HÜMEYRA\Documents\\GitHub\KUL\data\\falseValues\\smooth2001_10.txt'

# Load data from the first text file
data1 = np.genfromtxt(true, delimiter=',')
y_values1 = data1[:, 1]

# Load data from the second text file
data2 = np.genfromtxt(false, delimiter=',')
y_values2 = data2[:, 1]


# Load data from the first text file
data3 = np.genfromtxt(true1, delimiter=',')
y_values3 = data3[:, 1]

# Load data from the second text file
data4 = np.genfromtxt(false1, delimiter=',')
y_values4 = data4[:, 1]

# Plot the data from both files on the same graph
plt.plot(y_values1, label='true')
plt.plot(y_values2, label='false')
# plt.plot(y_values3, label='true1')
# plt.plot(y_values4, label='false1')

# Add labels and title
plt.xlabel('Data Point Index')
plt.ylabel('Y Values')
plt.title('Data from Two Text Files')
plt.legend()
plt.show()
