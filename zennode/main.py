# Products
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Fees
shipping_fee_per_package = 5
units_per_package = 10


grand_total = 0
total_quantity = 0

discounts = []


# Main function
def main():
    global grand_total
    global total_quantity
    
    for product_name in products:
        quantity = int(input(f"Enter the quantity of {product_name}: "))
        gift_wrap = input(f"Wrap {product_name} as a gift? (yes/no): ").lower() == "yes"
        
        total = product_total(product_name, quantity, gift_wrap)
        grand_total += total
        total_quantity += quantity

        if grand_total > 200:
            discounts.append(("flat_10_discount", flat_10_discount()))

        if quantity > 10:
            discounts.append(("bulk_5_discount", bulk_5_discount(total)))

        if total_quantity > 20:
            discounts.append(("bulk_10_discount", bulk_10_discount()))

        if total_quantity > 30 and quantity > 15:
            discounts.append(("tiered_50_discount", tiered_50_discount(product_name, quantity)))

        print("products:", product_name)
        print("Quantity:", quantity)
        print("amount of product:", total)
        print("subtotal:", grand_total)
        print('shipping fee',calculate_shipping_fee(total_quantity))
        
        print()


    # Sort the discounts and find the highest discount
    if discounts:
        sorted_discounts = sorted(discounts, key=lambda x: x[1], reverse=True)
        highest_discount = sorted_discounts[0]
        print("Discount Applied: {} (Amount: ${})".format(highest_discount[0], highest_discount[1]))
        print("Total with Highest Discount: $", grand_total - highest_discount[1])
    else:
        print("No discount applied.")


# Calculate the total price for a product
def product_total(product_name, quantity, gift_wrap):
    gift_wrap_total=0
    gift_wrap_fee=1
    price = products[product_name]
    if gift_wrap:
        total = (price * quantity) + (gift_wrap_fee * quantity)
        gift_wrap_total += gift_wrap_fee * quantity
        print('wrap charges',gift_wrap_total)
    else:
        total = price * quantity

    return total

# Apply a flat $10 discount
def flat_10_discount():
    discount_amount = 10
    print("Discount Applied: Flat $10")
    return discount_amount

# Apply a 5% discount 
def bulk_5_discount(total):
    discount = total * 0.05
    print("Discount Applied: Bulk 5%")
    return discount

# Apply a 10% discount 
def bulk_10_discount():
    discount = grand_total * 0.1
    print("Discount Applied: Bulk 10%")
    return discount

# Apply a 50% discount 
def tiered_50_discount(product_name, quantity):
    price = products[product_name]
    discount = (quantity - 15) * price * 0.5
    print("Discount Applied: Tiered 50%")
    return discount

def calculate_shipping_fee(total_quantity):
    num_packages = total_quantity // units_per_package
    if total_quantity % units_per_package != 0:
        num_packages += 1
    shipping_fee = num_packages * shipping_fee_per_package
    return shipping_fee


main()
