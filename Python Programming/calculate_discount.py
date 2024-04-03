def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount = price * discount_percent / 100
    final_price = price - discount
  else:
    final_price = price

  return final_price

# Get user input for price and discount
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage (0-100): "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price after discount: ${final_price:.2f}")
