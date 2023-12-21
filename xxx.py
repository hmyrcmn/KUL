import numpy as np
import matplotlib.pyplot as plt

# Define the paths to your text files
true1 = '/content/KUL/trueValues5/smooth2001_150.txt'
false1 = '/content/KUL/falseValues6/smooth20010_103.txt'

# Load data from the first text file
data1 = np.genfromtxt(true1, delimiter=',')
y_values1 = data1[:, 1]

# Load data from the second text file
data2 = np.genfromtxt(false1, delimiter=',')
y_values2 = data2[:, 1]

# Plot the data from both files on the same graph
plt.plot(y_values1, label='true1')
plt.plot(y_values2, label='false1')

# Add labels and title
plt.xlabel('Data Point Index')
plt.ylabel('Y Values')
plt.title('Data from Two Text Files')
plt.legend()
plt.show()
