


def evalueteIncrementPercentage():
    oldSalary = float(input("Enter old salary:  "))
    newSalary = float(input("Enter new salary:  "))

    diff = newSalary - oldSalary
    increment = (diff/oldSalary)*100
    print("Salary incremented percentage = ", increment)


def newSalaryForGivenPercentage():
    currentSalary = float(input("Enter the current salary:  "))
    percentageIncrement = float(input("Enter the percentage increment:  "))

    newSalary = currentSalary + (currentSalary * (percentageIncrement / 100))
    print("New salary after ${percentageIncrement} percentege increment = ", newSalary)

option = int(input("Enter 1 to show increment percentage from new salary \n Enter 2 to show new salary for percentage increment"))
if(option == 1) :
    evalueteIncrementPercentage()
else:
    newSalaryForGivenPercentage()
