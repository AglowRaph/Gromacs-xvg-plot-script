Place the plot_xvg.py script in the same directory as your .xvg files.

Run the script:
```bash
python plot_xvg.py

## The script will:

Read all .xvg files in the current directory.
Extract and plot data for each file.
Apply appropriate x and y labels, including units (e.g., "Time (ps)" for time in picoseconds).
Save each plot as a .png file with the same name as the .xvg file.
Each plot file is saved in the same directory as the original .xvg file.
