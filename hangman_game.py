# import random
# import stages  # Make sure stages.py is in the same directory

# word_list = ["Ramdas","Roshani","Samiksha","Bhavini", "Janhvi","Arohi", "Hardhika"]
# lives = 6
# chosen_word = random.choice(word_list)
# print(f"Chosen word (for testing): ")#{chosen_word}"

# display = ['_' for _ in chosen_word]
# print(" ".join(display))

# game_over = False

# while not game_over:
#     guessed_letter = input("Guess a letter: ")#.lower()
#     correct_guess = False

#     for position in range(len(chosen_word)):
#         if chosen_word[position] == guessed_letter:
#             display[position] = guessed_letter
#             correct_guess = True

#     if not correct_guess:
#         lives -= 1
#         print(f"Incorrect! You have {lives} lives left.")
#         if lives == 0:
#             game_over = True
#             print("You Lose! The word was:", chosen_word)

#     print(" ".join(display))
#     print(stages.stage[lives])

#     if '_' not in display:
#         game_over = True
#         print("You win!! 🎉")

import random
import stages  # Make sure stages.py is in the same directory

def play_round(chosen_word):
    lives = 6
    display = ['_' for _ in chosen_word]
    print(f"\nNew word! ({len(chosen_word)} letters)")
    # print(f"(DEBUG) Chosen word: {chosen_word}")  # Uncomment for testing
    print(" ".join(display))

    while True:
        guessed_letter = input("Guess a letter: ").lower()
        correct_guess = False

        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
                correct_guess = True

        if not correct_guess:
            lives -= 1
            print(stages.stage[lives])
            print(f"Incorrect! You have {lives} lives left.")
            if lives == 0:
                print("You Lose! The word was:", chosen_word)
                return False  # Lost the round

        print(" ".join(display))

        if '_' not in display:
            print("You win!! 🎉")
            return True  # Won the round

def hangman_game():
    original_word_list = ["Ramdas","Roshani","Samiksha","Bhavini", "Janhvi","Arohi", "Hardhika"] # My Family member names 
    play_again = True
    total_wins = 0
    total_losses = 0

    while play_again:
        word_list = original_word_list.copy()
        random.shuffle(word_list)

        for word in word_list:
            result = play_round(word)
            if result:
                total_wins += 1
            else:
                total_losses += 1

        print("\n🎮 All words used in this round!")
        print(f"🏆 Total Wins: {total_wins}")
        print(f"💀 Total Losses: {total_losses}")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            play_again = False
            print("Thanks for playing! Bye 👋")

# Start the game
hangman_game()
