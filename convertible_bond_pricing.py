
import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1  # Maturity in years
N = 365  # Number of steps
dt = T / N  # Time step
S0 = 100  # Initial stock price
r0 = 0.05  # Initial interest rate
sigma = 0.2  # Volatility of the stock
theta = 0.05  # Long-term mean level for the interest rate
gamma = 0.5  # Speed of reversion for the interest rate
eta = 0.1  # Volatility of the interest rate
M = 10000  # Number of simulation paths
alpha = 5  # Conversion ratio
F = 100  # Assume a face value for the bond
rho = 0.3  # Assuming a correlation coefficient

np.random.seed(0)  # For reproducibility

S_paths_corr = np.zeros((N+1, M))
r_paths_corr = np.zeros((N+1, M))
S_paths_corr[0, :] = S0
r_paths_corr[0, :] = r0

for t in range(1, N+1):
    dB2 = np.sqrt(dt) * np.random.randn(M)
    dB1 = rho * dB2 + np.sqrt(1 - rho**2) * np.sqrt(dt) * np.random.randn(M)
    r_paths_corr[t, :] = r_paths_corr[t-1, :] + gamma * (theta - r_paths_corr[t-1, :]) * dt + eta * np.sqrt(r_paths_corr[t-1, :]) * dB2
    S_paths_corr[t, :] = S_paths_corr[t-1, :] * (1 + r_paths_corr[t-1, :] * dt + sigma * dB1)

y_avg = np.mean(r_paths_corr[-1, :])
P_tau_T = F * np.exp(-y_avg * (T - (N*dt)))
payoffs_realistic = np.maximum(P_tau_T, alpha * S_paths_corr[-1, :])

bond_price_estimate_realistic = np.mean(payoffs_realistic)
print(f"Estimated Convertible Bond Price: {bond_price_estimate_realistic}")

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

for i in range(10):
    ax[0].plot(S_paths_corr[:, i], lw=1)
ax[0].set_title('Sample Paths for Stock Price $S_t$')
ax[0].set_xlabel('Time Steps')
ax[0].set_ylabel('Stock Price')

for i in range(10):
    ax[1].plot(r_paths_corr[:, i], lw=1)
ax[1].set_title('Sample Paths for Interest Rate $r_t$')
ax[1].set_xlabel('Time Steps')
ax[1].set_ylabel('Interest Rate')

plt.tight_layout()
plt.show()
