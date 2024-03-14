def calculate_discount(price, discount_percent):
    try:
        price = float(price)
        discount_percent = float(discount_percent)
        if discount_percent >= 20:
            return price * (1 - discount_percent / 100)
        else:
            return price
    except ValueError:
        print("Error: Please enter valid numeric values for price and discount percentage.")

try:
    price, discount_percent = input("Enter the original price of an item and the discount percentage separated by space: ").split()
    discounted_price = calculate_discount(price, discount_percent)
    print("Discounted price:", discounted_price)
except ValueError:
    print("Error: Please enter two values separated by space.")
