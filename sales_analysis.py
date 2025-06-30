# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load CSV file
# Replace 'sales_data.csv' with your actual file name or URL
df = pd.read_csv('sales_data.csv')

# Step 3: Preview the data (first 5 rows)
print("Preview of Data:")
print(df.head())

# Step 4: Group data by 'Product' and sum the 'Sales' column
sales_by_product = df.groupby('Product')['Sales'].sum()

# Step 5: Display total sales by product
print("\nTotal Sales by Product:")
print(sales_by_product)

# Step 6: Plot the total sales by product
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to fit labels
plt.show()