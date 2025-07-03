import random
import string



appnum = int(input("Welcome to Simple Project!" 
                   "Choose an application:\n"
                   "1. Calculator\n"
                   "2. Password Generator\n"
                   "3. Dice Roller Simulator\n"
                   "4. Quizzler\n"
                   "5. Stock Price Checker\n"
                   "6. Hangman\n"
                   "7. Roman Numeral Converter\n\n"))


def calculator():
    print("╔═══════════════════════════════╗")
    print("║         PythonCalc 1.0        ║")
    print("╠═══════════════════════════════╣")
    print("║                               ║")
    print("║                               ║")
    print("║                               ║")
    print("╠═══════╦═══════╦═══════╦═══════╣")
    print("║   7   ║   8   ║   9   ║   /   ║")
    print("╠═══════╬═══════╬═══════╬═══════╣")
    print("║   4   ║   5   ║   6   ║   *   ║")
    print("╠═══════╬═══════╬═══════╬═══════╣")
    print("║   1   ║   2   ║   3   ║   -   ║")
    print("╠═══════╬═══════╬═══════╬═══════╣")
    print("║   0   ║   .   ║   =   ║   +   ║")
    print("╚═══════╩═══════╩═══════╩═══════╝")
    print("\n\n")

    onum= int(input("enter the first number"))
    tnum= int(input("enter the second number"))
    operation= str(input("enter the operation")) 
    if operation not in ["+", "-", "*", "/", "%"]:
        print("Invalid operation. Please enter one of +, -, *, /, %.")
        return
    print("\n\n")
    if operation == "+":
        print(onum + tnum)
    elif operation == "-":
        print(onum - tnum)
    elif operation == "*":
        print(onum * tnum)
    elif operation == "/":
        print(onum / tnum)
    elif operation == "%":
        print(onum % tnum)
    else:
        print("oops, something went wrong")
def password_generator():

    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    
    if length < 4:
        print("Password length should be at least 4 characters.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    print(f"Generated Password: {password}")
def dice_roller():

    print("Welcome to the Dice Roller Simulator!")
    num_dice = int(input("Enter the number of dice to roll: "))
    num_sides = int(input("Enter the number of sides on each die: "))
    rolls = [random.randint(1, num_sides) for dice in range(num_dice)]
    print(f"Rolling {num_dice} {num_sides}-sided dice...")
    print("Results:", rolls)
    print("Total:", sum(rolls))



def quizzler():
