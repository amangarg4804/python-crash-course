def compare_investment_outcomes(quantity, buy_price, percent_increase, selling_percent_quantity, percent_fall):
    """
    Compare Person A (sells % of original quantity) vs Person B (holds all).
    
    quantity: total shares bought initially
    buy_price: price per share at purchase
    percent_increase: % rise in price before selling
    selling_percent_quantity: % of initial quantity sold after the rise
    percent_fall: % drop from the high price after selling
    """
    # Step 1 – Initial total value
    initial_value = quantity * buy_price

    # Step 2 – Price after rise
    price_after_rise = buy_price * (1 + percent_increase / 100)

    # Step 3 – Person A sells part of the original quantity
    shares_sold = (selling_percent_quantity / 100) * quantity
    cash_a = shares_sold * price_after_rise
    remaining_shares_a = quantity - shares_sold

    # Step 4 – Price after fall
    price_after_fall = price_after_rise * (1 - percent_fall / 100)

    # Step 5 – Final values
    person_a_share_value = remaining_shares_a * price_after_fall
    person_a_total = person_a_share_value + cash_a
    person_a_return_percent = ((person_a_total - initial_value) / initial_value) * 100

    person_b_total = quantity * price_after_fall
    person_b_return_percent = ((person_b_total - initial_value) / initial_value) * 100

    # Step 6 – Print results
    print(f"Initial Price: {buy_price}, Quantity: {quantity}")
    print(f"Price after rise ({percent_increase}%): {price_after_rise:.2f}")
    print(f"Price after fall ({percent_fall}% from high): {price_after_fall:.2f}\n")

    print("=== Results ===")
    print(f"Person A (sold {selling_percent_quantity}% of original quantity at high):")
    print(f"  Final Value: {person_a_total:.2f}")
    print(f"  Return: {person_a_return_percent:.2f}%")

    print(f"Person B (didn't sell):")
    print(f"  Final Value: {person_b_total:.2f}")
    print(f"  Return: {person_b_return_percent:.2f}%")


# Example usage (your case: 1 share at 100, +25%, sell 10% quantity, -25% fall)
compare_investment_outcomes(
    quantity=1000,
    buy_price=100,
    percent_increase=500,
    selling_percent_quantity=10,
    percent_fall=40
)

#in short:

# Small sales + small drops = tiny benefit (your example).
# Bigger sales or bigger drops = significant difference.
# The “keep booking profits” advice is more about reducing risk and locking gains during volatile markets 
# than about always beating buy-and-hold in rising markets.

# "Smart investing is at every 100% rise, keep exiting 5-10 percent of your position. 
# Over time your portfolio will automatically get concentrated. 
# Winners will win so much that other stock's percentages will come down. "
# Ah — that’s a different angle than just “booking profits to protect from falls.”

# What you’ve read is more like **position concentration through partial selling** rather than purely “locking gains.” me break that down in plain terms:


## 1. The idea

# * Every time a stock **doubles** (100% rise from your buy price or last sell checkpoint), sell **5–10% of your original position**.
# * The sold cash can be **reinvested into new opportunities** or held for diversification.
# * You’re **not trying to predict tops** — you’re systematically trimming.
# * Over time, your portfolio naturally **concentrates in the best performers** because:
# 
#   * The **winners keep growing faster than you trim**.
#   * The weaker stocks’ weightage drops (because they don’t rise as much, or you sell them completely if they stagnate).
# 
# ---
# 
# 2. Why it works mathematically
# 
# Let’s say you buy 10 stocks equally (₹10k each = ₹100k total).
# 
# If one stock grows 4× in 5 years, and others grow slower:
# 
# * You’ll have sold some of it at each doubling, but even after trims, the compound growth makes it dominate the portfolio.
# * The poor performers keep shrinking as % of portfolio because they grow slower or stagnate.
# 
# In other words, **winners win by growing out of proportion**, not because you “bet big” on them initially — you let them earn that weight.
# 
# 3. The hidden benefit
# 
# * Reduces **single-stock blowup risk** (if a star performer crashes after being very overweight).
# * Gives you **cash flow** to buy new high-potential stocks without adding new capital.
# * Acts as a **systematic discipline** (removes emotional decision-making).
# 
# ---
# 
# 4.  Why it doesn’t “feel” huge in a single example
# 
# If you test it on **one stock, one rise, one fall**, the % difference between selling vs not selling might be small.
# But over **years and many stocks**, the benefit comes from:
# 
# * Lower risk of catastrophic loss in a single name.
# * Increasing position sizes in the true multibaggers without chasing.
# * Recycling capital into new ideas.
# 
