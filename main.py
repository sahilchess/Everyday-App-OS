import random
import string



def calculator():
    print("\n" + "=" * 40)
    print("           PYTHONCALC 1.0")
    print("=" * 40)
    
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
    print()

    try:
        onum = int(input("Enter the first number: "))
        tnum = int(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        if operation not in ["+", "-", "*", "/"]:
            print("❌ Invalid operation. Please enter one of +, -, *, /.")
            return
        
        print("\n" + "-" * 30)
        print("RESULT:")
        
        if operation == "+":
            result = onum + tnum
            print(f"{onum} + {tnum} = {result}")
        elif operation == "-":
            result = onum - tnum
            print(f"{onum} - {tnum} = {result}")
        elif operation == "*":
            result = onum * tnum
            print(f"{onum} * {tnum} = {result}")
        elif operation == "/":
            if tnum == 0:
                print("❌ Error: Cannot divide by zero!")
                return
            result = onum / tnum
            print(f"{onum} / {tnum} = {result}")
        print("-" * 30)
        
    except ValueError:
        print("❌ Error: Please enter valid numbers!")









def password_generator():
    print("\n" + "=" * 40)
    print("        PASSWORD GENERATOR")
    print("=" * 40)
    
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("❌ Password length should be at least 4 characters.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        
        print("\n" + "-" * 40)
        print("🔐 GENERATED PASSWORD:")
        print(f"   {password}")
        print("-" * 40)
        print(f"✅ Password length: {len(password)} characters")
        
    except ValueError:
        print("❌ Error: Please enter a valid number!")








def dice_roller():
    print("\n" + "=" * 40)
    print("       DICE ROLLER SIMULATOR")
    print("=" * 40)
    
    try:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides on each die: "))
        
        if num_dice <= 0 or num_sides <= 0:
            print("❌ Please enter positive numbers for dice and sides!")
            return
        
        rolls = [random.randint(1, num_sides) for dice in range(num_dice)]
        
        print(f"\n🎲 Rolling {num_dice} {num_sides}-sided dice...")
        print("-" * 30)
        print(f"Results: {rolls}")
        print(f"Total: {sum(rolls)}")
        print("-" * 30)
        
    except ValueError:
        print("❌ Error: Please enter valid numbers!")








def quizzler():
    print("\n" + "=" * 40)
    print("            QUIZZLER")
    print("=" * 40)
    
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
    total_questions = len(aquestions)
    
    print(f"Welcome! You have {total_questions} questions to answer.")
    print("-" * 40)
    
    for qnum, question in enumerate(aquestions, start=1):
        print(f"\nQuestion #{qnum}/{total_questions}:")
        print(f"📝 {question}")
        answer = input("Your answer: ").lower().strip()
        
        if answer == questions[question]:
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! The correct answer was: {questions[question].title()}")
            print(f"\n🎯 Final Score: {score}/{qnum}")
            print(f"You answered {qnum} question(s) before getting one wrong.")
            print("Better luck next time! 🍀")
            return
    
    print(f"\n🎉 CONGRATULATIONS! 🎉")
    print(f"🏆 Perfect Score: {score}/{total_questions}")
    print("You answered all questions correctly! 🌟")








def hangman():
    print("\n" + "=" * 40)
    print("            HANGMAN")
    print("=" * 40)
    
    # Hangman ASCII art stages
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
     |
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

    topic = random.choice(hangman_topics)
    word = random.choice(hangman_words[topic])
    guessed_letters = []
    current_stage = 0
    
    print(f"📂 Topic: {topic.replace('_', ' ').title()}")
    print(f"🎯 Word length: {len(word)} letters")
    print("-" * 40)
    print("Guess the word:")
    print("_ " * len(word))
    print()
    
    while current_stage < len(hangman_stages) - 1:
        guess = input("Enter a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue
        elif guess in guessed_letters:
            print("❌ You already guessed that letter!")
            continue
        elif guess in word:
            guessed_letters.append(guess)
            print("✅ Good guess!")
        else:
            guessed_letters.append(guess)
            current_stage += 1
            print("❌ Wrong guess!")
        
        print(hangman_stages[current_stage])
        current_word = ''.join([letter if letter in guessed_letters else '_ ' for letter in word])
        print(f"Current word: {current_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Wrong guesses left: {len(hangman_stages) - 1 - current_stage}")
        print("-" * 30)
        
        if '_ ' not in current_word:
            print("🎉 Congratulations! You've guessed the word:", word.upper())
            return
    
    print("💀 Game Over! You've run out of attempts!")
    print(f"The word was: {word.upper()}")





def roman_numeral_converter():
    print("\n" + "=" * 40)
    print("      ROMAN NUMERAL CONVERTER")
    print("=" * 40)
    
    print("Choose conversion type:")
    print("1. Arabic to Roman (ar)")
    print("2. Roman to Arabic (ra)")
    print("-" * 40)
    
    # Roman Numeral Conversion Data
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 
        100: "C", 90: "XC", 50: "L", 40: "XL", 
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }



    def ar(arabic):
        """Convert Arabic number to Roman numeral"""
        original_num = arabic
        result = ""
        for value in sorted(roman_numerals.keys(), reverse=True): 
            while arabic >= value:
                result += roman_numerals[value]
                arabic -= value
        
        print(f"✅ The Roman numeral for {original_num} is: {result}")
        return result

    def ra(roman):
        """Convert Roman numeral to Arabic number"""
        roman = roman.upper()
        total = 0
        prev_value = 0
        
        # Validate input
        for char in roman:
            if char not in roman_numerals.values():
                print(f"❌ Invalid Roman numeral character: {char}")
                return None
        
        # Convert to Arabic
        for char in roman:
            value = next(key for key, val in roman_numerals.items() if val == char)
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
        
        print(f"✅ The Arabic numeral for {roman} is: {total}")
        return total

    decision = input("Enter your choice (ar/ra): ").lower().strip()
    
    if decision == "ar":
        try:
            arabic_int = input("Enter the integer to convert: ").strip()
            if arabic_int.isdigit() and int(arabic_int) > 0:
                arabic_int = int(arabic_int)   
                ar(arabic_int)
            else:
                print("❌ Please enter a positive whole number!")
        except ValueError:
            print("❌ Please enter a valid number!")
            
    elif decision == "ra":
        roman_str = input("Enter the Roman numeral to convert: ").strip()
        if roman_str:
            ra(roman_str)
        else:
            print("❌ Please enter a valid Roman numeral!")
    else:
        print("❌ Invalid choice! Please enter 'ar' or 'ra'.")


def devlog_formatter():
    print("\n" + "=" * 40)
    print("        DEVLOG FORMATTER")
    print("=" * 40)
    
    a = input("Enter the title of the devlog: ")
    b = input("Enter the subtitle of the devlog (optional): ")
    c = input("Enter the body/description of the devlog: ")
    d = input("Enter the attachment of the devlog (Use #cdn; optional): ")
    e = input("Enter the author of the devlog: ")
    f = input("Enter the date of the devlog (YYYY-MM-DD): ")

    print("\n" + "=" * 40)
    print("Formatted Devlog:")
    print("=" * 40)
    print(f"Title: {a}")
    if b:
        print(f"Subtitle: {b}")
    print(f"Description: {c}")
    if d:
        print(f"Attachment: {d}")
    print(f"Author: {e}")
    print(f"Date: {f}")
    


















# Main menu and application selection
print("=" * 50)
print("         WELCOME TO EVERYDAY APP OS")
print("=" * 50)

continue_choice = "y"

while continue_choice == "y":
    print("Choose an application:")
    print("1. Calculator")
    print("2. Password Generator") 
    print("3. Dice Roller Simulator")
    print("4. Quizzler")
    print("5. Hangman")
    print("6. Roman Numeral Converter")
    print("7. Devlog Formatter ")
    print("=" * 50)

    appnum = int(input("Enter your choice (1-7): "))
    print(f"\nYou have selected application number: {appnum}")
    print("=" * 50)



    # Application Router
    print("\n" + "=" * 50)
    print("            STARTING APPLICATION...")
    print("=" * 50)



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
        case 7:  # Placeholder for future app
            devlog_formatter()
        case 8:  # Placeholder for future app
            print("🚧 This application is under construction! Please check back later. 🚧")
        case 9:  # Placeholder for future app
            print("🚧 This application is under construction! Please check back later. 🚧")
        case 10:  # Placeholder for future app
            print("🚧 This application is under construction! Please check back later. 🚧")
        case _:  # Default case
            print("❌ Invalid application number! Please choose 1-6.")
    
    continue_choice = input("\n\nDo you want to use a different app? (y/n): ").lower().strip()
    while continue_choice not in ["y", "n"]:
        continue_choice = input("❌ Invalid answer. Please enter 'y' or 'n': ").lower().strip()


print("\n" + "=" * 50)
print("       THANK YOU FOR USING EVERYDAY APP OS!")
print("=" * 50)