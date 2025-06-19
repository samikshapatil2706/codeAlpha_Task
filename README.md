🎮 CodeAlpha Task: Hangman Game
📝 Project Overview
Hangman Game is a simple and interactive command-line Python game designed especially for beginner programmers. The main objective is to guess a hidden word, one letter at a time, within a limited number of attempts, also known as lives.

🧠 Game Concept
🎯 A word is randomly selected from a list of family member names:
"Ramdas", "Roshani", "Samiksha", "Bhavini", "Janhvi", "Arohi", and "Hardhika".

❓ The word is initially hidden and displayed as blank underscores (_), one for each letter.

👤 The player guesses one letter per turn:

✅ If the letter is correct, it’s revealed in its correct position(s).

❌ If the letter is wrong, the player loses a life.

🪓 The game visually shows progress using ASCII art, stored in a separate Python file called stages.py, which represents the hangman figure depending on remaining lives.

🏆 The player wins if they guess all the letters correctly before lives run out.

💀 The player loses if they use all their lives, and the correct word is revealed.

🔁 Extended Features
This version includes a more advanced structure using a hangman_game() function, which allows:

🔄 Multiple rounds of play using all words in the list.

📊 Tracking total wins and losses across rounds.

🗨️ Prompting the user if they wish to play again after each round.

🛠️ Python Concepts Used
This project helps reinforce important Python programming concepts:

🔁 Loops (while, for)

📦 Functions and modular code (def, import)

🔡 String and list operations

📥 User input and output handling

🧪 Conditional statements (if, else)

🧩 Customization
You can easily extend or customize this game:

➕ Add more words to the list

🎨 Modify the ASCII art in stages.py

🛡️ Add features like difficulty levels or hints

