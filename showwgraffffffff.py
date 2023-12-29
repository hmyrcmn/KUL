import os
import matplotlib.pyplot as plt

# Folder path where the text files are located
folder_path ='C:\\Users\\HÜMEYRA\\Documents\\GitHub\\KUL\\coordinateds2\\falseValues'

# Get the list of all .txt files in the folder
file_names = [filename for filename in os.listdir(folder_path) if filename.endswith('.txt')]

# Lists to store x and y values from all files
all_x_values = []
all_y_values = []

# Process each file
for file_name in file_names:
    x_values = []  # To store x values for each file
    y_values = []  # To store y values for each file

    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'r') as f:
        for line in f.readlines():
            x_values.append(float(line.split(',')[0]))
            y_values.append(float(line.split(',')[1]))

    # Append x_values and y_values to the lists
    all_x_values.append(x_values)
    all_y_values.append(y_values)

    # Do something with x_values and y_values, for example, print or process further
    #print(f"File: {file_name}, X Values: {x_values}, Y Values: {y_values}")

# Plot the data
plt.figure(figsize=(10, 6))
for x_values, y_values in zip(all_x_values, all_y_values):
    plt.plot(x_values, y_values, label=f'Data from {file_name}')

plt.title('Data Visualization')
plt.xlabel('X Values')
plt.legend()
plt.xlim(0, 1000)
plt.ylim(0, 250)
plt.ylabel('Y Values')
plt.show()
