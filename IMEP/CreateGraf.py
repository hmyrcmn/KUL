from matplotlib.ticker import AutoMinorLocator
from matplotlib.widgets import Button
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import os  # Import the os module for file operations

fig, ax = plt.subplots()
coordinates = []

# Create the 'coordinateds' folder if it doesn't exist
folder_path = 'coordinateds9'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Get the existing TXT files in the 'coordinateds' folder
file_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.txt')]

global num
num = 1

def on_key(event):
    plt.cla()
    draw_coordinates(event, coordinates)
    print(f"Key pressed: {event.key}")
    #showgraf()
    cid = fig.canvas.mpl_connect('button_press_event', on_click)


def plot_graph(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
        x = [float(line.split()[0].replace(',', '')) for line in data]
        y = [float(line.split()[1].replace(',', '')) for line in data]

    plt.plot(x, y, label=file_path)
def showgraf():
    plt.cla()

    # Plot the graphs
    for file_path in file_paths:
        plot_graph(file_path)

    # Move the legend outside the plot
    # plt.legend(bbox_to_anchor=(0.85, 0.2), loc='upper left')
    
    plt.grid(True, which="both")
    ax.minorticks_on()
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    plt.xlim(0, 1000)
    plt.ylim(0, 250)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.title('Verilere Ait Grafikler')
    plt.show()

def on_click(event):
    global num
    x, y = event.xdata, event.ydata
    coordinates.append((x, y))
    ax.scatter(x, y)
    plt.draw()
def draw_coordinates(event, coordinates):
    global file_paths
    x_values, y_values = zip(*coordinates)

    # Print the original values
    print("Original x_values:", x_values)

    # Remove duplicates while preserving the order
    unique_indices = sorted(set(range(len(x_values))), key=x_values.__getitem__)
    x_values = [x_values[i] for i in unique_indices]
    y_values = [y_values[i] for i in unique_indices]

    # Print the updated values
    print("Updated x_values:", x_values)

    try:
        spl = make_interp_spline(x_values, y_values, k=3)
        x_line = np.linspace(min(x_values), max(x_values), 1000)
        y_line_smooth = spl(x_line)

        num = len([name for name in file_paths if 'smooth200' in name]) + 1
        file_name = os.path.join(folder_path, f'smooth200{num}.txt')
        print("file_name:", file_name)
        num += 1

        with open(file_name, 'w') as f:
            x_positions = np.linspace(min(x_values), max(x_values), 1000)
            for x_pos in x_positions:
                f.write('{}, {}\n'.format(x_pos, spl(x_pos)))

        file_paths.append(file_name)
        coordinates.clear()
        showgraf()
    except Exception as e:
        print("Error:", e)


# connect the event handlers to the figure
cid_key = fig.canvas.mpl_connect('key_press_event', on_key)
cid = fig.canvas.mpl_connect('button_press_event', on_click)

showgraf()
