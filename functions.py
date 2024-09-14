def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent /100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    #User Prompt for original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if final_price == original_price:
    print(f"No discount applied. The price remains : ${original_price:.2f}")
else:
    print(f"Discount applied! The final price is : ${final_price:.2f}")







