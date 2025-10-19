from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


para_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_raw.csv")  # read csv
para_xlsx = Path(__file__).parent.parent.joinpath("data", "paralympics_all_raw.xlsx")  # read excel

para_csv_read = pd.read_csv(para_csv)
para_xlsx_read_sheet1 = pd.read_excel(para_xlsx, sheet_name=0)  # read sheet 1 of excel, 0 indexed
para_xlsx_read_sheet2 = pd.read_excel(para_xlsx, sheet_name=1)  # read sheet 2


def data_summary(file):
    # summary function of data frame
    print(file.shape)
    print(file.head())
    print(file.columns)


missing_rows = para_csv_read[para_csv_read.isna().any(axis=1)]
print(missing_rows)

# Clear any existing plots
plt.clf()

# Histogram
plt.figure(figsize=(10, 6))
para_csv_read.hist()
plt.title("Histogram of Paralympics Data")
plt.tight_layout()
plt.show()

# Clear for next plot
plt.clf()

# Box Plot
plt.figure(figsize=(10, 6))
para_csv_read.boxplot()
plt.title("Box Plot of Paralympics Data")
plt.tight_layout()
plt.show()

# PLOTTING DATA
# Sample DataFrame
df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [4, 3, 2, 1]})

# Using pandas.plot directly creates the figure, axes and allows for some customisation
# matplotlib examples typically split this into separate commands defining fig and ax then adding customisation
ax = df.plot(title="Sample Plot", xlabel="X-axis Label", ylabel="Y-axis Label")


# Show the plot
plt.show()

# linting = checking code for errors and style issues
# to lint in VS code, install pylint extension and it will automatically lint your code
# or run pylint in terminal with "pylint <file_name>.py"

# To format code in VS code, right click and select "Format Document" or use the shortcut Shift + Alt + F
