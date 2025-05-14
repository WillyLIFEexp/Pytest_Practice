# ecom_utils.py
def apply_discount(price, discount):
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)
