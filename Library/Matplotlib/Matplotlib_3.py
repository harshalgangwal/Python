import matplotlib.pyplot as plt
import numpy as np

sales = np.random.randint(10,1000, size=12)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

plt.figure(figsize=(10,6))
plt.title("Sales Data Visualization")
plt.xlabel("Months of 2023", fontsize=14)
plt.ylabel("Sales")
plt.grid(True)
plt.plot(months, sales, color='blue', marker='o',linewidth=2)
plt.legend(['Sales'])
plt.xticks(rotation=45)
plt.show()

import matplotlib.pyplot as plt

# Data for the pie chart
sizes = [25, 35, 20, 20]  # Percentages for each section
labels = ['Product A', 'Product B', 'Product C', 'Product D']  # Labels for each section
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']  # Colors for each section

# Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the aspect ratio to be equal so the pie is drawn as a circle
plt.axis('equal')

# Title of the pie chart
plt.title('Market Share of Products')

# Display the pie chart
plt.show()
