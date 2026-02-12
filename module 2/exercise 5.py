talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))
#convert everything to lots
total = talents * 20 * 32 + pounds * 32 + lots
#convert lots to grams
total_lots = talents * 20 * 32 + pounds * 32 + lots
grams = total_lots * 13.3
#convert grams to kilograms and grams
kilograms = int(grams // 1000)
remaining_grams = grams % 1000
print (f"the weight is {kilograms} kilograms and {grams : .2f} grams ")2