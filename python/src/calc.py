#! /usr/bin/env python

# Example 2: A Python program from the Raspberry Pi User Guide

goAgain = 1
while goAgain == 1:
    firstNumber = float(raw_input("Type the first number: " ))
    secondNumber = float(raw_input("Type the second number: "))

    print "{0} + {1} = {2}" .format(firstNumber, secondNumber, firstNumber + secondNumber)
    
    print "{0} - {1} = {2}" .format(firstNumber, secondNumber, firstNumber - secondNumber)

    print "{0} * {1} = {2}" .format(firstNumber, secondNumber, firstNumber * secondNumber)

    if(secondNumber != 0):
        print "{0} / {1} = {2}" .format(firstNumber, secondNumber, firstNumber / secondNumber)
        print "{0} % {1} = {2}" .format(firstNumber, secondNumber, firstNumber % secondNumber)

    goAgain = int(raw_input("Type 1 to enter more numbers, or any other number to quit: "))
    
                  
        
                                                                                            
