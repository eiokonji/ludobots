import numpy as np
import matplotlib.pyplot as plt
import os

# get all the files containing data
files = os.listdir("FitnessData")
if len(files) == 0:
    print("NO DATA TO ANALYZE")
    exit()

# loop through the filenames
legend = []
for file in files:
    
    # get the metadata for the legend
    splitName = file.split("_")
    legend = f"Seed {splitName[2][0]}"
    
    # read the data in
    with open(f"FitnessData/{file}") as f:
        data = []
        for line in f:
            num = line.split("\n")[0]
            if num != '':
                data.append(float(num))
        plt.plot(data, label=legend)

# format and plot
plt.ylabel("Fitness")
plt.xlabel("Number of Generations")
plt.title("Evolution")
plt.legend()

# save the figure
figNumber = len(os.listdir("FitnessCurves")) + 1
plt.savefig(f"FitnessCurves/Curve{figNumber}.png")