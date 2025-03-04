"""Problem: Draw a bar chart to compare the sales of four different products
           (A, B, C, and D) for three consecutive months. The x-axis represents the products,
           and the y-axis represents the sales in units.
Goal: Visualize sales growth or decline for each product over the months"""

# import matplotlib.pyplot as plt
# import numpy as np
#
# products = ['A','B','C','D']
# months = ['MARCH','APRIL','MAY']
# sales = np.random.randint(200,400, size=(3,4))
#
# bar_width = 0.25
# index = np.arange(len(products))
# plt.figure(figsize=(10,6))
# plt.title("compared each product Sales")
# plt.xlabel("Products")
# plt.ylabel("Sales")
# plt.bar(x='products',y='sales')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Product names
products = ['A', 'B', 'C', 'D']

# Sales data for 3 months
sales_month1 = [150, 200, 250, 300]  # Sales in Month 1
sales_month2 = [180, 220, 230, 310]  # Sales in Month 2
sales_month3 = [170, 210, 240, 290]  # Sales in Month 3

# Set up the bar width and the positions of the bars
bar_width = 0.25
index = np.arange(len(products))

# Create a figure
plt.figure(figsize=(10, 6))

# Plotting the bars for each month
plt.bar(index, sales_month1, width=bar_width, color='blue', label='Month 1')
plt.bar(index + bar_width, sales_month2, width=bar_width, color='green', label='Month 2')
plt.bar(index + 2 * bar_width, sales_month3, width=bar_width, color='orange', label='Month 3')

# Labeling the axes and the title
plt.xlabel('Products', fontsize=12, color='darkblue')
plt.ylabel('Sales (units)', fontsize=12, color='darkblue')
plt.title('Sales Comparison of Products Over 3 Months', fontsize=14)

# Add the product names on the x-axis
plt.xticks(index + bar_width, products)

# Show the legend
plt.legend()

# Display the grid and plot
plt.grid(True)
plt.show()
