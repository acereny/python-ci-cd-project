def calculate_telecom_tax(amount, tax_rate):
    tax_amount = amount * tax_rate / 100
    total_amount = amount + tax_amount
    return total_amount