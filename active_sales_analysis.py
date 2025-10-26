import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
csv_path = input("Enter the full path to your CSV file (e.g., /Users/.../Order_details.csv): ")
if not os.path.isfile(csv_path):
    print(f"Error: File not found at {csv_path}")
    sys.exit(1)
try:
    Order_Details = pd.read_csv(csv_path)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    sys.exit(1)

if 'Transaction Date' not in Order_Details.columns:
    print("Error: 'Transaction Date' column not found in CSV.")
    sys.exit(1)

Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date'], errors='coerce')
Order_Details = Order_Details.dropna(subset=['Time']) 
Order_Details['Hour'] = Order_Details['Time'].dt.hour
timemost = Order_Details['Hour'].value_counts()
hours_sorted = list(range(0, 24))  
purchase_counts = timemost.sort_index().reindex(hours_sorted, fill_value=0).tolist()
print("\n Hour Of Day\tCumulative Number of Purchases")
for hour, count in zip(hours_sorted, purchase_counts):
    print(f"{hour}\t\t{count}")
plt.figure(figsize=(20, 10))
plt.title('Sales Happening Per Hour (Spread Throughout The Week)',
          fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)
plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(hours_sorted, purchase_counts, color='m', marker='o')
plt.xticks(hours_sorted)
plt.grid(True)
plt.show()
