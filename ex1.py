# Prompt the user for revenue (float) and cost (float).

revenue = float(input("Enter the revenue: "))
cost = float(input("Enter the cost: "))





if revenue > 0: 
    profit = revenue - cost
    margin = (profit / revenue) * 100 
    
    print(f"Profit: ${profit:.2f} | Margin: {margin:.2f}%")
else:
    print("Revenue must be greater than zero to calculate margin.")

# Print the results formatted nicely, e.g., "Profit: $X.XX | Margin: Y.YY%" (round margin to 2 decimals using round or f-string formatting).
# Handle division carefully (no zero division needed beyond check).