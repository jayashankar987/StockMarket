import string
from typing import Final
from colorama import Fore, Back, Style
import os

INVALID: Final = -1
LONG_POSITION: Final = 1
SHORT_POSITION: Final = 2


def showError(msg: string):
        print(Fore.WHITE + Back.RED + "**********************    {msg}    **********************", msg)

def getEntryType() -> int:
        buyOrSell = INVALID
        try:
                buyOrSell = float(showInput("Enter 1 for BUY Or 2 for SELL"))
                if (buyOrSell != 1 and buyOrSell != 2) :
                        showError("INVALID TRADE TYPE INPUT!!!")
                        return getEntryType()
                else:
                        return buyOrSell
        except:
                showError("INVALID TRADE TYPE INPUT!!!")
                return getEntryType()


def getLastTradedPrice() -> float:
        try:
                currentPrice = float(showInput("Enter LTP of the Stock: "))
                if(currentPrice <= 0):
                        showError("INVALID LTP INPUT!!!")
                        return getLastTradedPrice()
                return currentPrice
        except:
                showError("INVALID LTP INPUT!!!")
                return getLastTradedPrice()

        

def getTargetProfitPercentage() -> float :
        
        try:
                profitPercentage = float(showInput("Enter TARGET PROFIT Raning from 1.....100"))
                if (profitPercentage <= 0):
                        showError("EXPECTING A TARGET PERCENTAGE in RANGE of 1, 2, 3, .... 100")
                        return getTargetProfitPercentage()
                return profitPercentage
        except:
                showError("INVALID TARGET INPUT!!!")
                return getTargetProfitPercentage()

def getStopLossPercentage() -> float :
        
        try:
                stopLossPercentage = float(showInput("Enter STOP LOSS Raning from 1.....100"))
                if (stopLossPercentage <= 0):
                        showError("EXPECTING A STOP LOSS PERCENTAGE in RANGE of 1, 2, 3, .... 100")
                        return getTargetProfitPercentage()
                return stopLossPercentage
        except:
                showError("INVALID STOPLOSS INPUT!!!")
                return getStopLossPercentage()

def showInput(message: string) -> input:
        print(Style.RESET_ALL)
        return input(message + ": ")

os.system('cls' if os.name == 'nt' else 'clear')
tradeEntryType = getEntryType()
currentPrice = getLastTradedPrice()
expectedProfitPercentage = getTargetProfitPercentage()
expectedStoplossPercentage = getStopLossPercentage()
target = stopLoss = float(INVALID)

if (LONG_POSITION == tradeEntryType):
        target = currentPrice + (currentPrice *  expectedProfitPercentage * 0.01)
        stoploss = currentPrice - (currentPrice * expectedStoplossPercentage * 0.01)
elif(SHORT_POSITION == tradeEntryType): 
        target = currentPrice - (currentPrice * expectedProfitPercentage * 0.01)
        stoploss = currentPrice + (currentPrice * expectedStoplossPercentage * 0.01)
else:
        showError("INVALID INPUTS")
        exit

print(Fore.WHITE + Back.GREEN + "Expected TARGET Price: ", target)
print(Fore.WHITE + Back.RED + "Expected STOPLOSS Price", stoploss)

