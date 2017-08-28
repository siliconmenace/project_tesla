#!/usr/bin/python3

# Example 2: A Python program from the Raspberry Pi User Guide
from decimal import Decimal


goAgain = 1
while goAgain == 1:
    firstNumber = float(input("Type the first number: " ))
    secondNumber = float(input("Type the second number: "))

    print ("%1d + %1d = %1d" % (firstNumber, secondNumber, firstNumber + secondNumber))
    
    print ("%1d - %1d = %1d" % (firstNumber, secondNumber, firstNumber - secondNumber))

    print ("%1d * %1d = %1d" % (firstNumber, secondNumber, firstNumber * secondNumber))

    print ("%1d ^ %1d = %.2E" % (firstNumber, secondNumber, Decimal(firstNumber ** secondNumber)))

    if(secondNumber != 0):
     mod = firstNumber % secondNumber
     print ("%1d / %1d = %1f" % (firstNumber, secondNumber, firstNumber / secondNumber))
     print ("%1d %% %1d = %1d" % (firstNumber, secondNumber, mod))

    goAgain = int(input("Type 1 to enter more numbers, or any other number to quit: "))
                                                                                            
