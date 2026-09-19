orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0

print("\nOrder Amount\tDiscount %\tFinal Amount")
print("-" * 45)

for order_amount in orders:

    if order_amount >= 2000:
        discount_percent = 15
    elif order_amount >= 1500:
        discount_percent = 10
    elif order_amount >= 1000:
        discount_percent = 7
    else:
        discount_percent = 0

    discount_amount = order_amount * discount_percent / 100
    final_amount = order_amount - discount_amount

    total_revenue = total_revenue + final_amount

    print(
        order_amount,
        "\t\t",
        discount_percent,
        "%\t\t",
        final_amount
    )

print("-" * 45)
print("Total Revenue After Discounts:", total_revenue)