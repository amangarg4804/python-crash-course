import pandas as pd

# Function to simulate stock price changes based on EPS growth and P/E changes
def simulate_price(start_eps, start_pe, eps_growth_rate, pe_change_rate, years):
    data = []
    eps = start_eps
    pe = start_pe
    start_price = start_eps * start_pe  # Price in year 0

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
            "CAGR %": round(cagr * 100, 2)
        })
        # grow EPS and change PE for next year
        eps *= (1 + eps_growth_rate)
        pe *= (1 + pe_change_rate)

    return pd.DataFrame(data)

# Example simulation parameters
start_eps = 10.0       # starting EPS
start_pe = 30.0        # starting P/E
eps_growth_rate = 0.15 # 15% annual EPS growth
pe_change_rate = -0.05 # P/E multiple contracts by 5% per year
years = 5              # simulate 5 years

# Run simulation
df = simulate_price(start_eps, start_pe, eps_growth_rate, pe_change_rate, years)

# Display the results
print(df)

# Optional: save to CSV
df.to_csv("pe_eps_cagr_simulation.csv", index=False)
