# Desc: You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.
# List of toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# List of prices ()
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = []
for index, topping in enumerate(toppings):
    pizza_and_prices.append([prices[index], topping])


pizza_and_prices.sort()


print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
pizza_and_prices.pop()
print(pizza_and_prices)
pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)