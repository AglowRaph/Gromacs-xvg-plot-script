import numpy as np
import matplotlib.pyplot as plt
import os
import random

# Property labels with units
property_labels = {
    'bond': 'Bond (kJ/mol)',
    'angle': 'Angle (kJ/mol)',
    'proper-dih': 'Proper-Dih. (kJ/mol)',
    'ryckaert-bell': 'Ryckaert-Bell. (kJ/mol)',
    'lj-14': 'LJ-14 (kJ/mol)',
    'coulomb-14': 'Coulomb-14 (kJ/mol)',
    'lj-(sr)': 'LJ-(SR) (kJ/mol)',
    'disper.-corr.': 'Dispersion Correction (kJ/mol)',
    'coulomb-(sr)': 'Coulomb-(SR) (kJ/mol)',
    'coul.-recip.': 'Coulomb Reciprocal (kJ/mol)',
    'position-rest.': 'Position Restraint (kJ/mol)',
    'potential': 'Potential Energy (kJ/mol)',
    'kinetic-en.': 'Kinetic Energy (kJ/mol)',
    'total-energy': 'Total Energy (kJ/mol)',
    'conserved-en.': 'Conserved Energy (kJ/mol)',
    'temperature': 'Temperature (K)',
    'pres.-dc': 'Pressure DC (bar)',
    'pressure': 'Pressure (bar)',
    'constr.-rmsd': 'Constraint RMSD (nm)',
    'box-x': 'Box-X Dimension (nm)',
    'box-y': 'Box-Y Dimension (nm)',
    'box-z': 'Box-Z Dimension (nm)',
    'volume': 'Volume (nm^3)',
    'density': 'Density (g/L)',
    'pv': 'pV (kJ/mol)',
    'enthalpy': 'Enthalpy (kJ/mol)',
    'gyrate': 'Radius of Gyration (nm)',
    'rmsd': 'RMSD (nm)',
    'energy': 'Energy (kJ/mol)',
}

# Color palette for the plots
color_palette = [
    'b', 'g', 'r', 'c', 'm', 'y', 'k', '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFA1'
]

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

def get_labels(filename):
    """
    Determines the y-axis label based on keywords in the filename.
    Defaults to 'X-axis' and 'Y-axis' if no keyword matches.
    """
    # Check each key in property_labels to see if it appears in the filename
    for key, label in property_labels.items():
        if key in filename.lower():
            return "Time (ps)", label
    # Default labels if none match
    return "X-axis", "Y-axis"

def plot_and_save_xvg(x_data, y_data, filename):
    """
    Plots the data from an .xvg file and saves it as an image.
    """
    xlabel, ylabel = get_labels(filename)
    
    # Plot random color selection
    color = random.choice(color_palette)
    
    # Plot data with selected color
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"Plot of {filename}")
    plt.grid(True)

    # Save plot as image
    output_filename = f"{filename.split('.')[0]}.png"  # Save as .png
    plt.savefig(output_filename)
    plt.close()  # Close plot to avoid display and free memory
    print(f"Saved plot as {output_filename}")

# Locate all .xvg files in the current directory
current_directory = os.getcwd()
xvg_files = [file for file in os.listdir(current_directory) if file.endswith('.xvg')]

# Process each .xvg file
for filename in xvg_files:
    print(f"Processing {filename}...")
    x_data, y_data = read_xvg(filename)
    plot_and_save_xvg(x_data, y_data, filename)
