# P p ('') '' : $  {} _ "" ("")

import random

def get_difficulty():
    print("\nChoose Difficulty:")
    print(" 1 - Easy ($1 - $100, 10 guesses)")
    print(" 2 - Medium ($1 - $500, 8 guesses)")
    print(" 3 - Hard ($1 - $1000, 6 guesses)")

    while True:
        choice = input("Enter 1, 2 or 3" ).strip()
        if choice == "1":
            return 1, 100, 10
        elif choice == "2":
            return 2, 500, 8
        elif choice == "3":
            return 3, 1000, 6
        else:
            print("Enter Difficulty 1, 2 or 3" )

#Session accumulators
total_score = 0
total_win = 0
games_played = 0

print("=== Trade Guess Game===")

while True:
    difficulty, upper, max_guesses = get_difficulty()
    secret = random.randint(1, upper)
    guesses = 0
    won = False

    print(f"\nWe've got a secret P&L between $1 and ${upper}.")
    print(f"You have {max_guesses} guesses.\n")

    while True:
        remaining = max_guesses - guesses
        print(f"[{remaining} left]", end = " ")

        guess = int(input("Your guess: $"))
        guesses += 1

        if guess == secret:
            won = True
            break
        if guesses >= max_guesses:
            break

        direction = "Try a lower number" if guess > secret else "Try a higher number"
        diff = abs(secret - guess)
        threshold = upper * 0.04
        hint = "Hot" if diff <= threshold else "Warm" if diff <= threshold * 2 else "Cold"
        print(f"{hint}, {direction}")

    games_played += 1

    if won:
        score = max(1, max_guesses - guesses + 1)
        total_score += score
        total_win += 1
        print(f"\nCorrect! P&L was ${secret}")
        print(f"Score: {score}/{max_guesses}, Session Total: {total_score}")

    else:
        print(f"\nYou are out of guesses. P&L was ${secret}")

    if input("\nPlay again? (y/n):").lower() != "y":
        print(f"\n=== Session Summary ===")
        print(f"Games: {games_played}")
        print(f"Wins: {total_win}/{games_played}({total_win/games_played:.0%})")
        print(f"Score: {total_score}")
        break
