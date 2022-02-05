indexStopLoss = float(input("Enter Index stop loss value: "))
indexTarget = float(input("Enter targetted index value: "))
entryPrice = float(input("Enter entry price entered with: "))
currntIndex = float(input("Enter entry index value: "))
deltaValue = float(input("Enter delta of the index strike: "))

peOrCE = int(input("Enter 1 for CE and 2 for PE Trade"))
ce = 1
pe = 2
if (peOrCE == ce):
    targetPoints = indexTarget - currntIndex
    stoplossPoints = currntIndex - indexStopLoss
else :
    targetPoints = currntIndex - indexTarget
    stoplossPoints = indexStopLoss - currntIndex

optionsTargetPrice = entryPrice + (targetPoints * deltaValue)
optionsStopLossPrice = entryPrice - (stoplossPoints * deltaValue)


print("Your Target for entry of option is: ", optionsTargetPrice)
print("Your stoploss for the entry of option is ", optionsStopLossPrice)