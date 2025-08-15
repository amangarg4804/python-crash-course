def compare_investment_outcomes(quantity, buy_price, percent_increase, selling_percent, percent_fall):
    """
    Compare Person A (partial profit booking) vs Person B (hold all) outcomes.
    """
    # Step 1 – Initial total value
    initial_value = quantity * buy_price

    # Step 2 – After price rise
    price_after_rise = buy_price * (1 + percent_increase / 100)

    # Step 3 – Person A sells part of total value
    total_value_after_rise = price_after_rise * quantity
    sell_value = (selling_percent / 100) * total_value_after_rise
    shares_sold = sell_value / price_after_rise
    remaining_shares_a = quantity - shares_sold
    cash_a = sell_value

    # Step 4 – Price falls
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
    print(f"Person A (sold {selling_percent}% at high):")
    print(f"  Final Value: {person_a_total:.2f}")
    print(f"  Return: {person_a_return_percent:.2f}%")

    print(f"Person B (didn't sell):")
    print(f"  Final Value: {person_b_total:.2f}")
    print(f"  Return: {person_b_return_percent:.2f}%")


# Example usage (your original example)
compare_investment_outcomes(
    quantity=1000,
    buy_price=100,
    percent_increase=100,
    selling_percent=10,
    percent_fall=25
)
