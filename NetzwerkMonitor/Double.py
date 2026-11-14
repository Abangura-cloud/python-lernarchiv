prices = [10, 20, 30, 40]
doubled_high_prices = []
for x in prices:
    if x > 15:
        doubled_high_prices.append(x * x)
doubled_high_prices = [x * 2 for x in prices if x > 15]
print(doubled_high_prices)