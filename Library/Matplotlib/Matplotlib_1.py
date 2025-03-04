"""
Line Graph: Temperature Variation
Problem: Draw a line graph showing the temperature variation over a week in your city.
         The x-axis should represent the days of the week (Monday to Sunday),
         and the y-axis should represent the temperature in degrees Celsius.
Goal: Demonstrate a trend of increasing or decreasing temperatures
      using different colors for highs and lows."""

import matplotlib.pyplot as plt
import numpy as np

Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']
temp = np.random.randint(20, 40, size=7)
plt.figure(figsize=(12, 16))
plt.title("Temperature Variation")
plt.xlabel("Days of the week", color='darkblue')
plt.ylabel("Temperature in degree celsius", color='darkblue')
plt.grid(True)
plt.legend(['temp'])
for i in range(len(temp)):
    if temp[i] == max(temp):
        plt.plot(Days[i], temp[i], marker='o', color='green')
    elif temp[i] == min(temp):
        plt.plot(Days[i], temp[i], marker='o', color='red')

    else:
        plt.plot(Days[i], temp[i], marker='o', color='blue')
plt.plot(Days, temp, color='blue')
plt.xticks(rotation=45)
plt.show()