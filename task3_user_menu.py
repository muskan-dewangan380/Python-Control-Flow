orders = []

while True:

    print("\n===== ORDER MENU =====")
    print("1 - Add order amount")
    print("2 - Show all orders and totals after applying discounts")
    print("q - Quit")

    choice = input("Enter your choice: ").strip().lower()


    if choice == "q":
        print("Program ended.")
        break

    
    elif choice == "1":

        try:
            order_amount = int(input("Enter order amount: "))

        except ValueError:
            print("Error: Please enter a valid numeric order amount.")
            continue

        if order_amount < 0:
            print("Error: Order amount cannot be negative.")
            continue

        orders.append(order_amount)
        print("Order added successfully.")

        continue

    
    elif choice == "2":

        if len(orders) == 0:
            print("No orders have been added yet.")
            continue

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

        continue
    else:
        print("Invalid choice. Please enter 1, 2, or q.")
        continue
