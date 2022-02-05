from ast import Return
from locale import currency

from typing import Final
from colorama import Fore, Back, Style


LONG_POSITION: Final = 1
SHORT_POSITION: Final = 2
CE:Final = 1
PE: Final = 2
INVALID: Final = -1

globallongOrShortPosition = peOrCe = INVALID
currntIndex = indexStopLoss = indexTarget = IentryPrice = deltaValue = targetPoints = stoplossPoints = float(INVALID)


def getTradeType():
    global longOrShortPosition
    global peOrCe

    longOrShortPosition = int(input(Fore.WHITE + Back.GREEN + "Enter 1 for Long(buy) and 2 for short(sell): "))
    peOrCe = int(input(Fore.WHITE + Back.GREEN + "Enter 1 for CE and 2 for PE Trade: "))
    if(longOrShortPosition != 1 and longOrShortPosition != 2 and peOrCe != 1 and peOrCe != 2):
        print(Fore.WHITE + Back.RED + "**********************  Enter Valid Inputs **********************")
        getTradeType()
        return
    getCurrentIndex()


def getCurrentIndex():
    global currntIndex
    currntIndex = float(input(Fore.WHITE + Back.GREEN + "Enter current INDEX value: "))
    getTradeDetails() 


def getTargetIndex():
    global indexTarget
    indexTarget = float(input(Fore.WHITE + Back.GREEN + "Enter TARGET INDEX value: "))
    if (longOrShortPosition == LONG_POSITION):
        if(CE == peOrCe and indexTarget < currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A LONG CALL OPTION: ITS ADVISED TO SELECT A HIGHER TARGET INDEX POINT THAN CURRENT INDEX **********************")
            getTargetIndex()
            return
        elif (PE == peOrCe and indexTarget > currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A LONG PUT OPTION: ITS ADVISED TO SELECT A LOWER TARGET INDEX POINT THAN CURRENT INDEX **********************")
            getTargetIndex()
            return

    elif (longOrShortPosition == SHORT_POSITION):
        if (CE == peOrCe and indexTarget > currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A SHORT CALL OPTION: ITS ADVISED TO SELECT A LOWER TARGET INDEX POINT THAN CURRENT INDEX **********************")
            getTargetIndex()
            return
        elif (PE == peOrCe and indexTarget < currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A SHORT PUT OPTION: ITS ADVISED TO SELECT A HIGHER TARGET INDEX POINT THAN CURRENT INDEX **********************")
            getTargetIndex()
            return
    getStopLossIndex()

    
def getStopLossIndex():
    global indexStopLoss
    indexStopLoss = float(input(Fore.WHITE + Back.RED + "Enter STOPLOSS INDEX value: "))
    if (longOrShortPosition == LONG_POSITION):
        if (CE == peOrCe and indexStopLoss > currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A LONG CALL OPTION STOP LOSS: ITS ADVISED TO SELECT LOWER INDEX POINT THAN CURRENT INDEX **********************")
            getStopLossIndex()
            return
        elif (PE == peOrCe and indexStopLoss < currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A LONG PUT OPTION STOP LOSS: ITS ADVISED TO SELECT HIGHER INDEX POINT THAN CURRENT INDEX **********************")
            getStopLossIndex()
            return
    elif (longOrShortPosition == SHORT_POSITION):
        if (CE == peOrCe and indexStopLoss < currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A SHORT CALL OPTION STOP LOSS: ITS ADVISED TO SELECT HIGHER INDEX POINT THAN CURRENT INDEX **********************")
            getStopLossIndex()
            return
        elif (PE == peOrCe and indexStopLoss > currntIndex):
            print(Fore.WHITE + Back.RED + "********************** FOR A SHORT PUT OPTION STOP LOSS: ITS ADVISED TO SELECT LOWER INDEX POINT THAN CURRENT INDEX **********************")
            getStopLossIndex()
            return
    evaluate()


def getDeltaValue():
    global deltaValue
    deltaValue = abs(float(input(Fore.WHITE + Back.GREEN 
        + "Enter DELTA of the INDEX SELECTED: if unware of delta check in sensi bull [[[https://web.sensibull.com/option-chain?expiry=2022-02-10&tradingsymbol=NIFTY]]] ")))
    getTargetIndex()


def getTradeDetails():
    global entryPrice
    entryPrice = float(input(Fore.WHITE + Back.GREEN + "Enter ENTRY PRICE for selected INDEX: "))
    if(entryPrice < 0 or ()):
        print(Fore.WHITE + Back.RED + "********************** POTENTIAL 100% LOSS DETECTED **********************")
        getTradeDetails()
        return
    getDeltaValue()


def evaluate():
        global targetPoints
        global stoplossPoints

        if (CE == peOrCe):
            targetPoints = indexTarget - currntIndex
            stoplossPoints = currntIndex - indexStopLoss
        elif (PE == peOrCe) :
            targetPoints = currntIndex - indexTarget
            stoplossPoints = indexStopLoss - currntIndex
        else:
            print(Fore.WHITE + Back.RED + "********************** INVALID PE(Put Option) or CE(Call Option) INPUT **********************")
            getTradeType()

    
    
getTradeType()

if (LONG_POSITION == longOrShortPosition):
    optionsTargetPrice = entryPrice + (targetPoints * deltaValue)
    optionsStopLossPrice = entryPrice - (stoplossPoints * deltaValue)
elif(SHORT_POSITION == longOrShortPosition):
    optionsTargetPrice = entryPrice - (targetPoints * deltaValue)
    optionsStopLossPrice = entryPrice + (stoplossPoints * deltaValue)

print(Fore.WHITE + Back.GREEN + "Your TARGET for entry of option is: ", optionsTargetPrice)
print(Fore.WHITE + Back.RED + "Your STOPLOSS for the entry of option is ", optionsStopLossPrice)
print(Style.RESET_ALL)