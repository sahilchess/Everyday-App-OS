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
    aquestions = [
        "What is the capital of France?",
        "What is 2 + 2?",
        "What is the largest planet in our solar system?"
    ]
    questions = {
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "What is the largest planet in our solar system?": "jupiter"
    }
    score = 0
    for qnum, question in enumerate(aquestions, start=1):
        answer = input(f"Question #{qnum}: {question}\n").lower()
        if answer == questions[question]:
            score += 1
        else:
            print(f"Oh poop, you lost. womp womp. your final score was {score} and you got through {qnum} question(s).")
            return
    print(f"Congratulations, you won! horray! your final score was {score} and you got through all the question.")


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


roman_numerals = {
    1000: "M", 900: "CM", 500: "D", 400: "CD", 
    100: "C", 90: "XC", 50: "L", 40: "XL", 
    10: "X", 9: "IX",5: "V", 4: "IV", 1: "I"
}

def ar(arabic):
    result = ""
    for value in sorted(roman_numerals): 
        while arabic >= value:
            result = result + roman_numerals[value]
            arabic = arabic-value
    print(f"The roman numeral for {arabic} is: {result}")
    return result







def ra(roman):
    roman = roman.upper()
    total = 0
    prev_value = 0
    for char in roman:
        if char not in roman_numerals.values():
            print("Invalid Roman numeral")
            return
        value = next(key for key, val in roman_numerals.items() if val == char)
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    print(f"The Arabic numeral for {roman} is: {total}")
    return total
    





def roman_numeral_converter():
    print("Welcome to the Roman Numeral Converter!")

    decision = input("roman to arabic | or | arabic to roman? (ra/ar)")
    if decision == "ar":
        arabic_int = input(" what be the integer that you need to convert? ")
        if arabic_int.isdigit() and int(arabic_int) > 0:
            arabic_int = int(arabic_int)   
            ar(arabic_int)
        else:
            print("aye! enter a positve whole number or as some might call it, a real number.")
    elif decision == "ra":
        roman_str = input("what be the roman numeral that you need to convert? ")
        if isinstance(roman_str, str):
            ra(roman_str)
        else:
            print("aye! enter a valid roman numeral.")
    else:
        print("aye! enter a valid decision, either 'ar' or 'ra'.")










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