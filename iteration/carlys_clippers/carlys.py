# CS101: INTRODUCTION TO PROGRAMMING
# Carly's Clippers
# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go # through the lists of data that have been collected in the past couple of weeks. You will be calculating # some important metrics that Carly can use to plan out the operation of the business for the rest of the # month.
# 
# You have been provided with three lists:
# 
# hairstyles: the names of the cuts offered at Carly’s Clippers.
# prices: the price of each hairstyle in the hairstyles list.
# last_week: the number of purchases for each hairstyle type in the last week.
# Each index in hairstyles corresponds to an associated index in prices and last_week.
# 
# For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was # purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the # first index of their respective lists.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Carly wants to market cheapest haircuts. Take avg first
total_price = 0
for price in prices:
    total_price += price
average_price = round(total_price / len(prices), 2)

print("Average cut price: " + str(average_price))

# Use list comprehension to make a new list of prices
new_prices = [price - 5 for price in prices]
print(new_prices)



# Carly wants to know revenue
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] + last_week[i]

print("Total revenue: " + str(total_revenue))

average_daily_revenue = round(total_revenue / 7, 2)
print("Average daily revenue: " + str(average_daily_revenue))


# Carly wants a list of cuts under 30 schmeckles
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)