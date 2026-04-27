# If condition

purchase_amount = float(input("Enter the Purchase Amount this month :"))

if purchase_amount < 2000:
    print("5% Discount is ", purchase_amount * 0.05)
    print(
        "Total Amount include 5 % Discount is ",
        purchase_amount - (purchase_amount * 0.05),
    )

elif purchase_amount >= 2000 and purchase_amount < 6000:
    print("20 % Discount is ", purchase_amount * 0.20)
    print(
        "Total Amount include 20 % Discount is ",
        purchase_amount - (purchase_amount * 0.20),
    )

else:
    print(
        "Total Amount include 50 % Discount is ",
        purchase_amount - (purchase_amount * 0.50),
    )
