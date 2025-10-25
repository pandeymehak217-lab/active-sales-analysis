# Active Sales Analysis Using Python

This project analyzes online product sales data to determine **the busiest hours of the day** in terms of purchases. Using **Python, Pandas, and Matplotlib**, the script reads transaction data from a CSV file, calculates hourly sales, and visualizes the results in a line chart.

---

## Project Overview

Modern e-commerce platforms aim to optimize sales by understanding **customer activity patterns**. This project demonstrates how to:

- Load and process sales data using Pandas  
- Extract hours from transaction timestamps  
- Count purchases per hour  
- Visualize hourly sales trends using Matplotlib  

---

## Dataset

The project uses a CSV file containing transaction records. The CSV should have at least the following column:

- `Transaction Date` — the date and time of each transaction in `YYYY-MM-DD HH:MM:SS` format.

> **Note:** For privacy, a sample CSV is recommended instead of the full dataset. You can create a small sample with the same column names for testing.

Example CSV snippet:

| Transaction Date       |
|------------------------|
| 2025-10-25 09:15:23    |
| 2025-10-25 14:45:10    |
| 2025-10-25 21:05:55    |

---

## How to Run

1. Make sure you have Python 3 installed.  
2. Install required packages:

```bash
pip install pandas matplotlib numpy
