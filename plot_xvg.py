import numpy as np
import matplotlib.pyplot as plt
import os

def read_xvg(filename):
    """
    Reads a GROMACS .xvg file and returns the data as numpy arrays.
    Skips lines starting with `@` or `#` (header or comment lines).
    """
    x_data = []
    y_data = []

    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(('@', '#')):
                # Split the line into columns and convert to float
                columns = line.split()
                x_data.append(float(columns[0]))  # x-axis (e.g., time)
                y_data.append(float(columns[1]))  # y-axis (e.g., RMSD, energy)
                
    return np.array(x_data), np.array(y_data)

def plot_xvg(x_data, y_data, filename, xlabel="Time (ps)", ylabel="Value"):
    """
    Plots the data from an .xvg file and saves it as an image.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, label=ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"Plot of {filename}")
    plt.legend()
    plt.grid(True)
    plt.show()

# Locate all .xvg files in the current directory
current_directory = os.getcwd()
xvg_files = [file for file in os.listdir(current_directory) if file.endswith('.xvg')]

# Process each .xvg file
for filename in xvg_files:
    print(f"Processing {filename}...")
    x_data, y_data = read_xvg(filename)
    plot_xvg(x_data, y_data, filename, xlabel="Time (ps)", ylabel="RMSD (nm)")
