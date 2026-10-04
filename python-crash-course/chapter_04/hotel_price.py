prices = [85, 120, 95, 150, 110, 95, 200, 130, 90, 125]
print(min(prices), max(prices), len(prices))
# print(sum(prices) / len(prices))

total = 0
for price in prices: 
    total = total + price

print(total / len(prices))


copy_prices = sorted(prices[:])
print(copy_prices)
print(prices[4] + prices[5])

sum_squared_deviations = 0
moyenne = sum(prices) / len(prices)
for price in prices:
    sum_squared_deviations = sum_squared_deviations +(price - moyenne) ** 2 

print(sum_squared_deviations)

variance = sum_squared_deviations / len(prices)
ecart_type = variance ** 0.5
ecart_type_arrondi = round(ecart_type, 2)

print(f"L'écart-type est de {ecart_type_arrondi}")
print(f"La variance est de {variance}")


print(f"Les trois nuits les moins chères sont à : {copy_prices[0:3]}")


