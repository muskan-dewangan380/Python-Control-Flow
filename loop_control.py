
daily_sales = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily_sales:

    if sale == -1:
        print("Corrupted data found. Stopping processing.")
        break

   
    if sale == 0:
        print("No sales for this day. Skipping.")
        continue

    
    if sale > 0:
        total_sales = total_sales + sale
        print("Sale:", sale, "| Running Total:", total_sales)

print("\nFinal Total Sales:", total_sales)
              