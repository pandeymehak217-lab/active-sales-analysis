# active_sales_analysis.py
# Author: Mehek Pandey
# Project: Active Product Sales Analysis using Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# -----------------------------
# Step 1: Ask user for CSV path
# -----------------------------
csv_path = input("Enter the full path to your CSV file (e.g., /Users/.../Order_details.csv): ")

# Check if file exists
if not os.path.isfile(csv_path):
    print(f"Error: File not found at {csv_path}")
    sys.exit(1)

# Load the dataset
try:
    Order_Details = pd.read_csv(csv_path)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    sys.exit(1)

# -----------------------------
# Step 2: Convert Transaction Date to datetime and extract hour
# -----------------------------
if 'Transaction Date' not in Order_Details.columns:
    print("Error: 'Transaction Date' column not found in CSV.")
    sys.exit(1)

Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date'], errors='coerce')
Order_Details = Order_Details.dropna(subset=['Time'])  # remove invalid dates
Order_Details['Hour'] = Order_Details['Time'].dt.hour

# -----------------------------
# Step 3: Calculate busiest hours
# -----------------------------
timemost = Order_Details['Hour'].value_counts()
hours_sorted = list(range(0, 24))  # 0-23 hours
purchase_counts = timemost.sort_index().reindex(hours_sorted, fill_value=0).tolist()

# Display results
print("\n Hour Of Day\tCumulative Number of Purchases")
for hour, count in zip(hours_sorted, purchase_counts):
    print(f"{hour}\t\t{count}")

# -----------------------------
# Step 4: Data Visualization
# -----------------------------
plt.figure(figsize=(20, 10))
plt.title('Sales Happening Per Hour (Spread Throughout The Week)',
          fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)
plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(hours_sorted, purchase_counts, color='m', marker='o')
plt.xticks(hours_sorted)
plt.grid(True)
plt.show()
