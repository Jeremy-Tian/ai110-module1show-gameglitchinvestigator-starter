# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1.the hints were backwards. 
2.hard has less range than normal. 
3.under Make a guess banner, the message is not aligned with the range and attempts allowed 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot as my primary AI coding assistant throughout this debugging project. Copilot helped me understand the codebase, identify potential issues, and generate fixes for the various bugs I encountered.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Copilot correctly suggested refactoring the game logic from app.py into logic_utils.py for better code organization. I verified this by successfully moving the functions, ensuring all imports worked, and confirming that the tests still passed after the refactoring.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Initially, Copilot suggested a complex try-except block for handling type comparisons in the check_guess function, but this led to a NameError when the variable scoping didn't work as expected. I discovered this through testing and had to simplify the approach by normalizing both values to the same type before comparison.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was truly fixed by running comprehensive tests - both the existing pytest suite and manual testing of the Streamlit app. If the app could run without errors, the specific bug behavior was eliminated, and all automated tests passed, then I considered the fix complete.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran pytest multiple times throughout the debugging process, which revealed that the initial tests were failing due to import issues. After adding __init__.py files to create proper Python packages, pytest ran successfully and showed that the core game logic was working correctly with all 4 tests passing.

- Did AI help you design or understand any tests? How?
Copilot helped me understand the existing test structure and suggested improvements to the test cases. When I added a new test for the hint message correctness, Copilot provided guidance on the test structure and assertions, helping me create a regression test that would catch if the hint logic broke again in the future.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because Streamlit reruns the entire script every time a user interacts with the app (like clicking a button). Without proper session state management, the secret number was being regenerated on every rerun instead of being stored and reused across interactions.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are like refreshing a web page - every time you click a button or change something, the entire Python script runs again from top to bottom. Session state is like browser cookies for your app - it lets you save data (like a secret number) between these reruns so your app remembers things from one interaction to the next.

- What change did you make that finally gave the game a stable secret number?
I added proper session state initialization using st.session_state to store the secret number, attempts, score, and game status. The key change was checking if the secret already existed in session state before generating a new one, and adding logic to detect difficulty changes to reset the game appropriately.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to continue using comprehensive testing and adding collaboration comments throughout my code. Running pytest after every major change and documenting the debugging process with comments helped me catch issues early and understand the codebase better when revisiting it later.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would test AI-generated code more thoroughly before assuming it's correct, and I would ask the AI to explain complex logic in simpler terms rather than accepting complex solutions that might have hidden issues.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can have subtle bugs that aren't immediately obvious, and that thorough testing and understanding of the underlying framework (like Streamlit) are crucial when working with AI assistance. I now approach AI-generated code more critically and focus on understanding the "why" behind each solution.
