
try:
    order_amount = int(input("Enter order amount: "))

except ValueError:
    print("Error: Please enter a valid numeric order amount.")
    exit()

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

print("\nOrder Amount:", order_amount)
print("Discount:", discount_percent, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)