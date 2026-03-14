# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose:**  
  The Game Glitch Investigator is a number guessing game built with Streamlit where players try to guess a secret number within a range determined by difficulty level (Easy: 1-20, Normal: 1-100, Hard: 1-1000). Players receive hints ("Go HIGHER!" or "Go LOWER!") and earn points based on how quickly they guess correctly, with limited attempts per difficulty.

- [x] **Detail which bugs you found:**  
  1. **Secret number instability** - The secret number kept resetting/changing on every button click due to improper Streamlit session state management  
  2. **Backwards hints** - When guess was too high, it said "Go HIGHER!" instead of "Go LOWER!" (and vice versa)  
  3. **Incorrect difficulty scaling** - Hard difficulty had smaller range (1-50) than Normal (1-100), making it easier instead of harder  
  4. **Difficulty change issues** - Switching difficulty levels didn't reset the secret number or game state  
  5. **Unbalanced attempt limits** - Hard had fewer attempts (5) than Normal (8), despite needing more guesses for larger range  
  6. **Hardcoded range message** - Always showed "Guess between 1 and 100" regardless of actual difficulty range  
  7. **Type comparison errors** - Runtime NameError when secret was sometimes converted to string, causing type mismatches in comparisons  
  8. **Testing infrastructure** - Pytest failed with ModuleNotFoundError due to missing Python package structure

- [x] **Explain what fixes you applied:**  
  1. **Session state management** - Added proper initialization and persistence of secret number, attempts, score, and game status in Streamlit session state  
  2. **Hint logic correction** - Fixed comparison operators so "Too High" shows "Go LOWER!" and "Too Low" shows "Go HIGHER!"  
  3. **Difficulty range balancing** - Set Easy: 1-20, Normal: 1-100, Hard: 1-1000 for proper difficulty progression  
  4. **Difficulty change detection** - Added logic to detect difficulty changes and automatically reset secret number, attempts, score, and status  
  5. **Attempt limit scaling** - Balanced to Easy: 6, Normal: 8, Hard: 15 attempts based on range size  
  6. **Dynamic range display** - Changed hardcoded message to show actual range: "Guess between {low} and {high}"  
  7. **Type safety improvements** - Simplified check_guess function to normalize both guess and secret to same type (int or str) before comparison  
  8. **Package structure** - Added __init__.py files to make project a proper Python package, enabling pytest imports

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![alt text](image.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
