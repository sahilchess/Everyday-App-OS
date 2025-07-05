# Development Log - Everyday App OS

## Day: 1

Goals:
- Start up get momentum
- Make at least 2 apps
- Make it fun and visually interactive

What I Did:
- Created GitHub repo and codespace
- Created main menu to use input() to select the apps
- Implemented 3 apps that worked:
  - ✅ Calculator (with a visual layout and computationally valid functionality)
  - ✅ Password Generator (randomized with string and random)
  - ✅ Dice Roller (to roll a pair of custom dice for each user, per side of die)

Challenges:
- Figuring out how to make the calculator visually attractive only using print()

Next Steps:
- More apps: Quizzler, Hangman, Roman Numeral Converter
- Refactor code into a main loop so the user can return to the menu after every app is selected
- Improving the calculator to include floats, exponentiation (), and error handling for invalid entries
- Adding ASCII art/graphics to the Dice Roller for pizazz 🎲
- Consider changing this to a web app with Flask or PyScript in the future

---

## Day: 2

Goals:
- Add more interactive and logic-based apps
- Focus on fun, classic games and utilities
- Skip apps that felt too complex or uninteresting for now

What I Did:
- Implemented 3 new apps:
  - ✅ Quizzler (multiple-choice quiz with scoring and feedback)
  - ✅ Roman Numeral Converter (two-way conversion with validation)
  - ✅ Hangman (classic word game with letter tracking and win/loss logic)

Skipped 2 apps for now:
- ❌ Stock Price Checker (API setup too complex for now)
- ❌ Countdown Timer (less engaging than other ideas)

Challenges:
- Designing clean logic for Hangman and Roman numeral conversion
- Keeping the interface consistent and readable across all apps
- Avoiding feature creep while still making each app feel complete

Next Steps:
- Refactor the main menu into a loop so users can return after each app
- Add more creative or themed apps (e.g., typing test, mini RPG, weather fetcher)
- Add a "Credits" or "About" screen
- Explore turning this into a web app using Flask or PyScript

---

## Day: 3

Goals:
- Polish the user experience and interface consistency
- Implement proper application looping system
- Create comprehensive documentation for users
- Fix any remaining bugs and improve code organization

What I Did:
- Added consistent headers and professional formatting across all apps
- Implemented proper looping system allowing users to return to main menu
- Created comprehensive README.md with installation instructions and troubleshooting
- Fixed variable initialization, syntax errors, and restored missing calculator features
- Added function documentation and cleaned up formatting throughout

Challenges:
- Balancing feature completeness with code readability
- Managing the complexity of the looping system without breaking existing functionality
- Writing user-friendly documentation that works for all skill levels

Next Steps:
- Add more sophisticated applications (typing test, unit converter, file organizer)
- Implement data persistence (save high scores, user preferences)
- Consider adding colored output using libraries like `colorama`
- Plan migration to web-based interface using Flask or FastAPI
