
# Convertible Bond Pricing via Monte Carlo Simulation

This repository contains a Python script for simulating the pricing of a convertible bond using the Monte Carlo method. The simulation incorporates correlated paths for both the underlying stock price and the interest rate, employing the Geometric Brownian Motion (GBM) model for the stock and the Cox-Ingersoll-Ross (CIR) model for the interest rate.

## Overview

The script simulates the dynamics of a stock price and interest rate over time, then calculates the price of a convertible bond based on these simulated paths. The bond's payoff considers both the bond's value and the option to convert into stock, making use of a simplified approach for bond valuation under varying interest rates.

## Key Parameters

- Maturity: 1 year
- Daily time steps
- Initial stock price: $100
- Initial interest rate: 5%
- Stock volatility: 20%
- CIR model parameters for interest rate simulation
- Conversion ratio: 5
- Bond face value: $100
- Correlation between stock and interest rate: 0.3

## Usage

To run the simulation, ensure you have Python and Matplotlib installed. Execute the script to generate the estimated price of the convertible bond and visualize sample paths for both the stock price and interest rate.

## Output

The script outputs the estimated price of the convertible bond and displays plots for sample paths of the stock price and interest rate.

