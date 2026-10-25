def calculate_telecom_tax(amount: float, tax_rate: float) -> float:
    """Return an amount after applying the given percentage tax rate."""
    tax_amount = amount * tax_rate / 100
    return amount + tax_amount
