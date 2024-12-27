""""
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid
"""

amount: int = int(input("purcahsed amount: "))

if amount >= 50000:
    purchase = amount - (amount * 0.3)
    print(
        "discount:30%",
        "\nthe discout amount",
        int((amount * 0.30)),
        "\nthe purchase amount bill",
        int(purchase),
    )

elif amount >= 40000 and amount <= 49999:
    print(
        "discount:25%\n",
        "\bthe discount amount",
        amount,
        "\nthe discout amount",
        int((amount * 0.25)),
    )

    purchase = amount - (amount * 0.25)
    print(f"the purchase amount bill: {int(purchase)}")
elif amount >= 30000 and amount <= 39999:
    print(
        "discount:20%\n",
        "\bthe discount amount",
        amount,
        "\nthe discout amount",
        int((amount * 0.20)),
    )
    purchase = amount - (amount * 0.20)
    print(f"the purchase amount bill: {purchase}")
elif amount >= 10000 and amount <= 29999:
    print(
        "discount:10%\n",
        "\bthe discount amount",
        amount,
        "\nthe discout amount",
        int((amount * 0.1)),
    )
    purchase = amount - (amount * 0.1)
    print(f"the purchase amount bill: {purchase}")
else:
    print("discount 0%")
    print(amount)
    print(f"no discount and purchase amount bill:  {amount}")
