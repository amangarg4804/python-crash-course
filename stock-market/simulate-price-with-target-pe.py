import pandas as pd

def simulate_price_with_target_pe(start_eps, start_pe, target_pe, eps_growth_rate, years):
    # Calculate yearly P/E change rate from start_pe to target_pe over 'years'
    pe_change_rate = (target_pe / start_pe) ** (1 / years) - 1

    data = []
    eps = start_eps
    pe = start_pe
    start_price = start_eps * start_pe

    for year in range(years + 1):
        price = eps * pe
        if year == 0:
            cagr = 0.0
        else:
            cagr = (price / start_price) ** (1 / year) - 1  # CAGR formula
        
        data.append({
            "Year": year,
            "EPS": round(eps, 2),
            "P/E": round(pe, 2),
            "Price": round(price, 2),
            "CAGR %": round(cagr * 100, 2),
            "P/E Change Rate %": round(pe_change_rate * 100, 2)  # same for all years
        })

        # Update EPS and P/E for next year
        eps *= (1 + eps_growth_rate)
        pe *= (1 + pe_change_rate)

    return pd.DataFrame(data)

# ==== Example parameters ====
start_eps = 14.7         # Starting EPS
start_pe = 32.6          # Starting P/E
target_pe = 51         # Target P/E at the end of period
eps_growth_rate = 0.10   # EPS growth rate per year (15% = 0.15)
years = 1                # Number of years to reach target P/E

# Run simulation
df = simulate_price_with_target_pe(start_eps, start_pe, target_pe, eps_growth_rate, years)

# Display results
print(df)

# Optional: Save to CSV
df.to_csv("pe_eps_targetpe_simulation.csv", index=False)
