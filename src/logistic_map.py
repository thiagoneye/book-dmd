import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(x, beta):
    return beta * x * (1 - x)

# Parameters
beta_values = np.linspace(2.5, 4.0, 500)  # Range of beta values
x0 = 0.5  # Initial value of x

# Set up the figure for plotting
plt.figure(figsize=(10, 7))

# Iterate over a range of beta values
for beta in beta_values:
    x = x0
    # Iterate the logistic map for many iterations to allow the system to settle
    for _ in range(1000):
        x = logistic_map(x, beta)
    
    # After a long time, collect the next 100 points as the attracting set
    attractor_points = []
    for _ in range(100):
        x = logistic_map(x, beta)
        attractor_points.append(x)

    # Plot the attractor points for this value of beta
    plt.plot(attractor_points, [beta] * len(attractor_points), '.k', alpha=0.5)  # Vertical lines

# Add labels and title
plt.title("Attracting Sets of the Logistic Map for Varying β")
plt.xlabel("β (Control Parameter)")
plt.ylabel("Attracting Set Values (x)")
plt.show()