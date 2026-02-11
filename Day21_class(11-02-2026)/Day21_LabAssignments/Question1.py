import matplotlib.pyplot as plt
import seaborn as sns

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]


# Matplotlib Line Chart

plt.plot(months, sales, marker='o')

plt.title("Monthly Sales Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()


# Seaborn Bar Plot

sns.barplot(x=months, y=sales)

plt.title("Monthly Sales Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()
