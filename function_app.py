def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount if discount_percent >= 20.
           Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price



def main():
    import sys


    # Prompt the user for input
    try:
        price = float(input("Enter the original price of the item ($): "))
        discount_percent = float(input("Enter the discount percentage (%): "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        
        if discount_percent >= 20:
            print(f"\nGreat news! Your new price is: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied. Your price remains: ${price:.2f}")

    except ValueError:
        print("\nInvalid input! Please enter valid numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()
