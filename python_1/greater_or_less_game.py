import random

# Function: Play a single round of the game
def play_round(current_number: int) -> tuple:
    """
    Handles a single round of the game.
    Returns the new number and the score change based on player's guess.
    """
    print(f"Current number: {current_number}")
    player_guess = input("Will the next number be (g)reater, (l)ess, or (q)uit? ").lower()

    if player_guess == 'q':
        return None, 0  # Signal to quit

    if player_guess not in ('g', 'l'):
        print("Invalid input. Please enter 'g', 'l', or 'q'.")
        return current_number, 0  # No score change, repeat with same number

    next_number = random.randint(1, 100)
    print(f"Next number: {next_number}")

    if player_guess == 'g' and next_number > current_number:
        print("✅ Correct guess!")
        return next_number, 1
    elif player_guess == 'l' and next_number < current_number:
        print("✅ Correct guess!")
        return next_number, 1
    elif next_number == current_number:
        print("😐 It's the same number. No points.")
        return next_number, 0
    else:
        print("❌ Wrong guess!")
        return next_number, -1


# Main function: Starts and manages the game loop
def start_game():
    """
    Starts the Greater or Less Than game and tracks score and history.
    """
    player_score = 0
    number_history = []  # List to store the sequence of generated numbers
    current_number = random.randint(1, 100)

    print("🎮 Welcome to the Greater or Less Than Game!")
    print("Try to guess if the next number is greater or less than the current number.\n")

    while True:
        number_history.append(current_number)  # Store each number in the history list
        current_number, score_change = play_round(current_number)

        if current_number is None:  # If player chose to quit
            break

        player_score += score_change
        print(f"Current score: {player_score}\n")

    # After game ends
    print("📊 Game Over!")
    print(f"Your final score: {player_score}")
    print(f"Numbers you played with: {number_history}")


# Start the game
start_game()

