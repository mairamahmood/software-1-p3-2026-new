import math

def unit_price(diameter_cm, price_eur):
    """Return the unit price of pizza in euros per square meter."""
    radius_m = (diameter_cm / 100) / 2  # convert cm to meters and get radius
    area = math.pi * radius_m ** 2      # area in square meters
    return price_eur / area

# Main program
diam1 = float(input("Enter diameter of pizza 1 in cm: "))
price1 = float(input("Enter price of pizza 1 in euros: "))
diam2 = float(input("Enter diameter of pizza 2 in cm: "))
price2 = float(input("Enter price of pizza 2 in euros: "))

unit1 = unit_price(diam1, price1)
unit2 = unit_price(diam2, price2)

print(f"Pizza 1 unit price: {unit1:.2f} €/m²")
print(f"Pizza 2 unit price: {unit2:.2f} €/m²")

if unit1 < unit2:
    print("Pizza 1 provides better value for money.")
elif unit2 < unit1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same unit price.")