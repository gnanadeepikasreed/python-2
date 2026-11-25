
# Progressive Electricity Billing

months = []
bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    # Calculate slab charges
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charge
    fixed_charge = 50

    # Surcharge
    surcharge = bill * 0.05

    # Rebate for low consumption
    if units <= 100:
        rebate = bill * 0.10
    else:
        rebate = 0

    # Final bill
    total_bill = bill + fixed_charge + surcharge - rebate

    months.append(month)
    bills.append(total_bill)

    print("Electricity Bill:", round(total_bill, 2))

# Compare monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print(months[i], ":", round(bills[i], 2))

# Identify unusual increases
print("\n--- Unusual Bill Increases ---")

for i in range(1, n):
    increase = bills[i] - bills[i - 1]

    if increase > bills[i - 1] * 0.20:
        print(months[i], "has an unusual increase of",
              round(increase, 2))
    else:
        print(months[i], "has no unusual increase")

print("\nElectricity Billing Analysis Completed.")
