weight = float(input("Enter package weight: "))
shipping_method = ''
correct_selection = False
flat_charge = 0
weight_factor = 0
# Keep asking for the correct value until given
while not correct_selection:
    print("Enter shipping method. \n")
    shipping_method = input("G for Standard Ground, P for Premium Ground and D for Drone shipping: ").casefold()
    # Check case insensitive match here
    if shipping_method.casefold() == 'g' or shipping_method.casefold() == 'p' or shipping_method.casefold() == 'd':
        correct_selection = True

# Does python have switch case?
# Get flat charge for shipping method
if shipping_method == 'g':
    flat_charge = 20
elif shipping_method == 'p':
    flat_charge = 125
else:
    flat_charge = 0

# get weight factor
if shipping_method == 'p':
    weight_factor = 0
if shipping_method == 'g':
    if weight <= 2:
        weight_factor = 1.5
    elif weight <= 6:
        weight_factor = 3
    elif weight <= 10:
        weight_factor = 4
    else:
        weight_factor = 4.75
if shipping_method == 'd':
    if weight <= 2:
        weight_factor = 4.50
    elif weight <= 6:
        weight_factor = 9
    elif weight <= 10:
        weight_factor = 12
    else:
        weight_factor = 14.25
shipping_cost = weight * weight_factor + flat_charge
print("weight: " + str(weight))
print("weight_factor: " + str(weight_factor))
print("flat_charge: " + str(flat_charge))
print("The cost to ship your package is: $" + str(shipping_cost))





