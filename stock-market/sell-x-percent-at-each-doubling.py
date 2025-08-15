def simulate_doubling_then_fall(
    buy_price: float,
    quantity: float,
    num_doubles: int,
    sell_percent: float,
    percent_fall_after: float,
    sell_basis: str = "current",  # "current" = % of current holdings; "original" = % of original qty
    verbose: bool = True
):
    """
    Strategy:
      - Start at buy_price with 'quantity' shares.
      - For num_doubles steps: price doubles each step.
      - At each doubling, Person A sells 'sell_percent' based on 'sell_basis'.
      - After the last doubling, price drops by 'percent_fall_after'% from the peak.
      - Compare Person A (trimmed) vs Person B (never sells).

    Parameters
    ----------
    buy_price : float
    quantity : float
    num_doubles : int              # e.g., 1 -> 2x, 2 -> 4x, 3 -> 8x, ...
    sell_percent : float           # e.g., 10 means sell 10% each doubling
    percent_fall_after : float     # applied from the final (peak) price AFTER the last doubling
    sell_basis : str               # "current" or "original"
    verbose : bool                 # print timeline and summary

    Returns
    -------
    dict with final results and timeline.
    """
    assert sell_basis in ("current", "original"), "sell_basis must be 'current' or 'original'"
    assert 0 <= percent_fall_after <= 100, "percent_fall_after must be between 0 and 100"

    initial_value = buy_price * quantity
    price = buy_price

    # Person A state
    shares_a = float(quantity)
    cash_a = 0.0
    original_qty = float(quantity)

    history = []

    for step in range(1, num_doubles + 1):
        # Price doubles
        price *= 2.0

        # Decide how many shares to sell
        if sell_basis == "current":
            sell_shares = shares_a * (sell_percent / 100.0)
        else:  # sell % of original quantity each doubling
            sell_shares = original_qty * (sell_percent / 100.0)

        # Don't sell more than we have
        sell_shares = min(sell_shares, shares_a)

        proceeds = sell_shares * price
        shares_before = shares_a
        shares_a -= sell_shares
        cash_a += proceeds

        history.append({
            "event": f"Double {step}",
            "peak_price": price,
            "shares_before": shares_before,
            "sold_shares": sell_shares,
            "sale_proceeds": proceeds,
            "shares_after": shares_a,
            "cash_after": cash_a,
            "person_a_total_at_peak": cash_a + shares_a * price
        })

    # Apply the fall from the peak after last doubling
    post_fall_price = price * (1.0 - percent_fall_after / 100.0)

    # Final totals
    person_a_total = cash_a + shares_a * post_fall_price
    person_b_total = quantity * post_fall_price

    person_a_abs = person_a_total - initial_value
    person_b_abs = person_b_total - initial_value

    person_a_pct = (person_a_abs / initial_value) * 100.0
    person_b_pct = (person_b_abs / initial_value) * 100.0

    diff_value = person_a_total - person_b_total
    diff_pct_points = (diff_value / initial_value) * 100.0  # advantage of A over B in percentage points

    if verbose:
        print(f"Initial: price={buy_price:.2f}, quantity={quantity}, initial_value={initial_value:.2f}")
        print(f"At each doubling, sell {sell_percent}% of "
              f"{'CURRENT holdings' if sell_basis=='current' else 'ORIGINAL quantity'}")
        print(f"After the last doubling, price falls by {percent_fall_after}% from the peak.\n")

        print("--- Timeline ---")
        print("Step       | Peak Price | Shares→Sold→Remain |   Cash After | Person A Total @ Peak")
        for i, h in enumerate(history, 1):
            print(f"{i:<10} | {h['peak_price']:>10.2f} | "
                  f"{h['shares_before']:.6g}→{h['sold_shares']:.6g}→{h['shares_after']:.6g} | "
                  f"{h['cash_after']:>11.2f} | {h['person_a_total_at_peak']:>21.2f}")

        print("\n--- After Fall ---")
        print(f"Post-fall price: {post_fall_price:.2f}")

        print("\nPerson A (trims each double):")
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


# -------------------------
# Example: your earlier scenario
# Buy at 100, qty 1000, one doubling (to 200),
# sell 10% of ORIGINAL quantity at the double,
# then a 25% fall from the peak → compare with not selling.
# -------------------------
simulate_doubling_then_fall(
    buy_price=100,
    quantity=1000,
    num_doubles=10,
    sell_percent=10,
    percent_fall_after=25,   # fall from peak (200 → 150)
    sell_basis="original",   # set to "current" to sell % of current holdings instead
    verbose=True
)
