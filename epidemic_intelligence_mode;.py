import matplotlib.pyplot as plt
import numpy as np

# Total population
N = 10000

# Initial values
S = 9900   # Susceptible
E = 50     # Exposed
I = 30     # Infectious (sharing)
R = 0      # Recovered (no longer sharing)
K = 20     # Skeptical (resistant)

beta = 0.5     # Transmission rate (S to E)
gamma = 0.02   # Rate of becoming skeptical (S to K)
delta = 0.2    # Rate of sharing (E to I)
rho = 0.05    # Recovery rate (I to R)

# Time steps
days = 60
time = np.arange(days + 1)

# Lists to store results
S_list, E_list, I_list, R_list, K_list = [S], [E], [I], [R], [K]

for t in range(days):
    new_exposed = beta * S * I / N
    new_skeptical = gamma * S
    new_infectious = delta * E
    new_recovered = rho * I
    
    S = max(0, S - new_exposed - new_skeptical)
    E = max(0, E + new_exposed - new_infectious)
    I = max(0, I + new_infectious - new_recovered)
    R = R + new_recovered
    K = K + new_skeptical
    
    # Save current values
    S_list.append(S)
    E_list.append(E)
    I_list.append(I)
    R_list.append(R)
    K_list.append(K)

# Plotting the results
plt.figure(figsize=(10,6))
plt.plot(time, S_list, 'b-', label='Susceptible')
plt.plot(time, E_list, 'y-', label='Exposed')
plt.plot(time, I_list, 'r-', label='Infectious')
plt.plot(time, R_list, 'g-', label='Recovered')
plt.plot(time, K_list, 'k-', label='Skeptical')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.title('Epidemic Intelligence Model Simulation')
plt.legend()
plt.grid(True)
plt.show()