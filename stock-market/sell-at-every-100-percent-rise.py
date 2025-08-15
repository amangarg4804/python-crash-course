def simulate_percent_rise_then_fall(
    buy_price: float,
    quantity: float,
    rise_interval_percent: float,  # e.g., 100 means sell after every +100% rise from buy price
    total_rise_percent: float,     # total rise from buy price before final fall
    sell_percent: float,
    percent_fall_after: float,
    sell_basis: str = "current",   # "current" = % of current holdings; "original" = % of original qty
    verbose: bool = True
):
    """
    Strategy:
      - Start at buy_price with 'quantity' shares.
      - Price rises from buy_price to buy_price * (1 + total_rise_percent/100).
      - At each multiple of 'rise_interval_percent' increase from buy_price, Person A sells.
      - After final rise, price falls by 'percent_fall_after'% from peak.
      - Compare Person A (trims) vs Person B (never sells).
    """

    assert sell_basis in ("current", "original"), "sell_basis must be 'current' or 'original'"
    assert 0 <= percent_fall_after <= 100

    initial_value = buy_price * quantity
    price = buy_price

    shares_a = float(quantity)
    cash_a = 0.0
    original_qty = float(quantity)
    history = []

    target_price = buy_price
    peak_price = buy_price * (1 + total_rise_percent / 100)

    # Go through each rise checkpoint
    step = 0
    while True:
        target_price += buy_price * (rise_interval_percent / 100)
        if target_price > peak_price:
            break

        price = target_price
        step += 1

        # Decide shares to sell
        if sell_basis == "current":
            sell_shares = shares_a * (sell_percent / 100.0)
        else:
            sell_shares = original_qty * (sell_percent / 100.0)

        sell_shares = min(sell_shares, shares_a)
        proceeds = sell_shares * price
        shares_before = shares_a
        shares_a -= sell_shares
        cash_a += proceeds

        history.append({
            "event": f"Sell {step}",
            "price": price,
            "shares_before": shares_before,
            "sold_shares": sell_shares,
            "sale_proceeds": proceeds,
            "shares_after": shares_a,
            "cash_after": cash_a,
            "person_a_total_at_checkpoint": cash_a + shares_a * price
        })

    # Final rise to peak (if not already there)
    price = peak_price

    # Apply the fall after peak
    post_fall_price = price * (1 - percent_fall_after / 100.0)

    # Final totals
    person_a_total = cash_a + shares_a * post_fall_price
    person_b_total = quantity * post_fall_price

    person_a_abs = person_a_total - initial_value
    person_b_abs = person_b_total - initial_value

    person_a_pct = (person_a_abs / initial_value) * 100.0
    person_b_pct = (person_b_abs / initial_value) * 100.0

    diff_value = person_a_total - person_b_total
    diff_pct_points = (diff_value / initial_value) * 100.0

    if verbose:
        print(f"Initial: price={buy_price:.2f}, qty={quantity}, initial_value={initial_value:.2f}")
        print(f"Sell {sell_percent}% of "
              f"{'CURRENT holdings' if sell_basis=='current' else 'ORIGINAL quantity'}")
        print(f"Sell triggered at every +{rise_interval_percent}% from buy price.")
        print(f"Total rise before fall: {total_rise_percent}%, then {percent_fall_after}% fall from peak.\n")

        print("--- Timeline ---")
        print("Step | Price     | Shares→Sold→Remain | Cash After | Person A Total @ Checkpoint")
        for i, h in enumerate(history, 1):
            print(f"{i:<4} | {h['price']:>9.2f} | "
                  f"{h['shares_before']:.6g}→{h['sold_shares']:.6g}→{h['shares_after']:.6g} | "
                  f"{h['cash_after']:>10.2f} | {h['person_a_total_at_checkpoint']:>27.2f}")

        print("\n--- After Fall ---")
        print(f"Post-fall price: {post_fall_price:.2f}")

        print("\nPerson A (trims each checkpoint):")
        print(f"  Shares: {shares_a:.6g}, Cash: {cash_a:.2f}")
        print(f"  Total:  {person_a_total:.2f}  |  Return: {person_a_abs:.2f} ({person_a_pct:.2f}%)")

        print("\nPerson B (never sells):")
        print(f"  Shares: {quantity:.6g}, Cash: 0.00")
        print(f"  Total:  {person_b_total:.2f}  |  Return: {person_b_abs:.2f} ({person_b_pct:.2f}%)")

        print("\n=== Comparison ===")
        print(f"Person A − Person B (₹): {diff_value:.2f}")
        print(f"Advantage of A over B (pct-pts vs initial): {diff_pct_points:.2f} pts")

    return {
        "final_price_after_fall": post_fall_price,
        "person_a": {
            "shares": shares_a,
            "cash": cash_a,
            "total_value": person_a_total,
            "abs_return": person_a_abs,
            "pct_return": person_a_pct,
        },
        "person_b": {
            "shares": quantity,
            "cash": 0.0,
            "total_value": person_b_total,
            "abs_return": person_b_abs,
            "pct_return": person_b_pct,
        },
        "difference": {
            "value": diff_value,
            "pct_points_vs_initial": diff_pct_points
        },
        "timeline": history
    }


# Example usage:
simulate_percent_rise_then_fall(
    buy_price=157,
    quantity=195,
    rise_interval_percent=100,  # sell at every +100% rise from buy price
    total_rise_percent=1000,     # final peak is +300% (price = 400)
    sell_percent=10,
    percent_fall_after=40,      # fall 25% from peak
    sell_basis="current",      # or "current"
    verbose=True
)

#When trimming actually wins
# The stock drops heavily after the peak (e.g., 70–90% crash).

# The rise is moderate (e.g., 100–300%), so the benefit of holding fewer shares is smaller 
# compared to the loss protection.

# You reinvest the sold cash into other winners — your simulation here keeps it as idle cash, 
# so it ignores the reinvestment benefit (which is the real power in a portfolio strategy).