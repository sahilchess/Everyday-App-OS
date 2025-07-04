import random
import string


appnum = int(input("Welcome to Simple Project!" 
                   "Choose an application:\n"
                   "1. Calculator\n"
                   "2. Password Generator\n"
                   "3. Dice Roller Simulator\n"
                   "4. Quizzler\n"
                   "5. Hangman\n"
                   "6. Roman Numeral Converter\n\n"))
print("\n\nYou have selected application number:", appnum , "\n\n")

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

    onum= int(input("enter the first number: "))
    tnum= int(input("enter the second number: "))
    operation= str(input("enter the operation (+, -, *, /, %): ")) 
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
    print("Welcome to the Quizzler!")
    questions = {
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "What is the largest planet in our solar system?": "jupiter"
    }
    score = 0
    qnum=1
    for a in range(len(questions)):
        answer = input(f"Question #{qnum}: {questions[a]} ").lower()     


def hangman():
    man1 = """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---
    """
    man2 = """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |
    ---
    """
    man3 = """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |
    ---
    """
    man4 = """
     ------
     |    |
     |    O
     |   /|
     |   
     |
    ---
    """
    man5 = """
     ------
     |    |
     |    O
     |    |
     |   
    ---
    ---
    """
    man6 = """
     ------
     |    |
     |    O
     |   
     |   
     |
    ---
    """
    man7 = """
     ------
     |    |
     |    
     |   
     |   
     |
    ---
    """
    hangman_stages = [man1, man2, man3, man4, man5, man6, man7]
    hangman_topics = ["coding_langs", "sports", "animals", "food", "colors"]
    hangman_words = {
        "coding_langs": ["python", "javascript", "java", "csharp", "ruby"],
        "sports": ["soccer", "basketball", "tennis", "cricket"],
        "animals": ["elephant", "giraffe", "kangaroo", "dolphin"],
        "food": ["pizza", "sushi", "burger", "pasta"],
        "colors": ["red", "blue", "green", "yellow"]
    }
    print("Welcome to Hangman!")

    # Game logic goes here

    topic = random.choice(hangman_topics)
    print(f"Topic: {topic}")
    word = random.choice(hangman_words[topic])
    guessed_letters = []
    attempts = len(word)
    current_stage = 0
    print("Guess the word:")
    print("_ " * len(word))
    while hangman_stages[current_stage] != man7:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("enter a singlt letter")
        elif guess in guessed_letters:
            print("you already entered that lettter, enter a different one")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            current_stage += 1
            print("Wrong guess!")
        print(hangman_stages[current_stage])
        current_word = ''.join([letter if letter in guessed_letters else '_ ' for letter in word])
        print("Current word:", current_word)
        if '_ ' not in current_word:
            print("Congratulations! You've guessed the word:", word)
            return
        if current_stage == len(hangman_stages) - 1:
            print("You've run out of attempts!")
            break

def roman_numeral_converter():
    print("Welcome to the Roman Numeral Converter!")
    roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
        40: "XL", 50: "L", 90: "XC", 100: "C",
        400: "CD", 500: "D", 900: "CM", 1000: "M"
    }
    
    def int_to_roman(num):
        result = ""
        for value in sorted(roman_numerals.keys(), reverse=True):
            while num >= value:
                result += roman_numerals[value]
                num -= value
        return result
    
    number = int(input("Enter an integer to convert to Roman numeral: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        roman_numeral = int_to_roman(number)
        print(f"Roman numeral for {number} is {roman_numeral}")







match appnum:
    case 1:
        calculator()
    case 2:
        password_generator()
    case 3:
        dice_roller()
    case 4:
        quizzler()
    case 5:
        hangman()
    case 6:
        roman_numeral_converter()
    case _:  # Default case
        print("Invalid application number")