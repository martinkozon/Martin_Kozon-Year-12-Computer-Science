#input two numbers, compare them and print the larger one
number1 = int(input("First number: ")) #first number choice
number2 = int(input("Second number: ")) #second number choice

#if the number1 is greater than number2, return number1
#otherwise return number2
if number1 > number2:
    print(str(number1))
else:
    print(str(number2))
# end if

#TEST DATA:
# Input -1, 1 -> output 1
# Input 5, 988 -> output 988
# Input 745, 744 -> output 745


## - ACS Excellent work
## Might be worth putting your test data in at the end of the program e.g.
## Inoput 12, 156 -> output 156.

# 27.9.19 EDIT - test data added