
# ============================================
# FUTURE INTERNS - MACHINE LEARNING INTERNSHIP
# TASK 1: SALES AND DEMAND FORECASTING
# ============================================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Create monthly sales data
data = {
    'Month': ['January', 'February', 'March',
              'April', 'May', 'June'],
    'Sales': [100, 120, 150, 140, 160, 180]
}

# Step 3: Convert data into a DataFrame
df = pd.DataFrame(data)

# Step 4: Display monthly sales data
print("\n========== MONTHLY SALES DATA ==========")
print(df.to_string(index=False))

# Step 5: Calculate average sales
average_sales = df['Sales'].mean()

print("\n========== SALES ANALYSIS ==========")
print("Average Monthly Sales:", round(average_sales, 2))

# Step 6: Estimate next month's sales
next_month_sales = average_sales

print("Estimated Sales for July:", round(next_month_sales, 2))

# Step 7: Draw sales graph using Matplotlib
plt.figure(figsize=(10, 5))

plt.plot(
    df['Month'],
    df['Sales'],
    marker='o',
    color='blue',
    linewidth=2,
    markersize=8,
    label='Monthly Sales'
)

# Add graph title and labels
plt.title('Monthly Sales and Demand Forecasting',
          fontsize=14)

plt.xlabel('Months', fontsize=12)
plt.ylabel('Sales', fontsize=12)

# Display grid
plt.grid(True)

# Display legend
plt.legend()

# Step 8: Save graph as PNG image
plt.savefig('sales_graph.png', dpi=300, bbox_inches='tight')

print("\nSales graph saved successfully as sales_graph.png")

# Step 9: Display graph
plt.show()

# ============================================
# PROJECT COMPLETED SUCCESSFULLY
# ============================================
