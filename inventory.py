import random
import matplotlib.pyplot as plt

# Generate random consumption data
consumption_data = [random.randint(1, 30) for _ in range(30)]

# Initialize variables
inventory = 100
order = 0
inventory_data = [inventory]
order_data = [0]

# Simulate inventory management
for consumption in consumption_data:
    if inventory < 50:
        order = 100
        inventory += order
    else:
        order = 0
    inventory -= consumption
    inventory_data.append(inventory)
    order_data.append(order)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(inventory_data, label='Inventory')
plt.plot(consumption_data, label='Consumption')
plt.plot(order_data, 'ro', label='Order')
plt.xlabel('Day')
plt.ylabel('Quantity')
plt.title('Inventory Management System')
plt.legend()
plt.grid(True)
plt.show()
