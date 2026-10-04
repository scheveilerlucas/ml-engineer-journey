prices = [85, 120, 95, 150, 110, 95, 200, 130, 90, 125]
print(min(prices), max(prices), len(prices))
# print(sum(prices) / len(prices))

total = 0
for price in prices: 
    total = total + price

print(total / len(prices))


copy_prices = sorted(prices[:])
print(copy_prices)
print(sum(prices[4] + prices[5]))

total_price = 0
moyenne = sum(prices) / len(prices)
for price in prices:
    total_price = total_price +(price - moyenne) ** 2 

print(total_price)

variance = total_price / len(prices)
ecart_type = variance ** 0.5
ecart_type_arrondis = round(ecart_type,2)

print(f"L'écart type est de {ecart_type_arrondis}")
print(f"La variance est de {variance}")


print(f"Les trois nuits les moins chères sont à : {copy_prices[0:3]}")


