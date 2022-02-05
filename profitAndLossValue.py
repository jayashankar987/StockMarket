from tracemalloc import stop


print("Enter Buy Or Sell: B - Buy ::::: S - Sell")

buyOrSell = input("Buy or Sell ? :")
target = 0.0
stoploss = 0.0
currentPrice = float(input("Enter current price(LTP): "))
profitPercentage = int(input("Enter Targetted Profit(Eg: 10 --- 100%):  "))
lossPercentage = int(input("Enter StopLoss Percentage(Eg: 100 ---- 10%):  "))

if (buyOrSell == "B" or buyOrSell == "b"): 
        target = currentPrice + (currentPrice *  profitPercentage * 0.01)
        stoploss = currentPrice - (currentPrice * lossPercentage * 0.01)
elif(buyOrSell == "S" or buyOrSell =="s"): 
        target = currentPrice - (currentPrice * profitPercentage * 0.01)
        stoploss = currentPrice + (currentPrice * lossPercentage * 0.01)
else:
        print("Invalid Input")
        exit

print("Target Price: ", target)
print("StopLoss Price", stoploss)

