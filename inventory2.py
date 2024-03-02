import random
import matplotlib.pyplot as plt
import time

# Generate random consumption data
consumption_data = [random.randint(1, 30) for _ in range(30)]

# Initialize variables
inventory = 100
order = 0
inventory_data = [inventory]
order_data = [0]

# Simulate inventory management
plt.figure(figsize=(10, 6))
plt.ion()  # Turn on interactive mode
plt.xlabel('Day')
plt.ylabel('Quantity')
plt.title('Inventory Management System')
plt.grid(True)

for i in range(30):
    if inventory < 50:
        order = 100
        inventory += order
    else:
        order = 0
    inventory -= consumption_data[i]
    inventory_data.append(inventory)
    order_data.append(order)

    if i == 0:
        plt.plot(inventory_data, label='Inventory', color='blue')
        plt.plot(consumption_data[:i+1], label='Consumption', color='orange')
        plt.plot(order_data[:i+1], 'ro', label='Order', color='green')
    else:
        plt.plot(inventory_data, color='blue')
        plt.plot(consumption_data[:i+1], color='orange')
        plt.plot(order_data[:i+1], 'ro', color='green')
    plt.legend()
    plt.draw()
    plt.pause(1)  # Pause for 1 second

plt.ioff()  # Turn off interactive mode
plt.show()