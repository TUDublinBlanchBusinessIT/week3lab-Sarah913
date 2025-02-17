#Sarah Forde
#17/02/2025
#findFirstFourPNs.py

#Write a program here that finds the first four perfect numbers.

#The pseudocode in the README.md file will help you write this program.

from perfectNumber import isPerfectNumber

def findFisrtFourNumbers ():
    count = 0
    num = 1
    while count < 4:
        if isPerfectNumber (num):
            print(f"{num} is a perfect number!")
            count += 1
        num += 1    


findFisrtFourNumbers ()
