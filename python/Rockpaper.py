import random

def rps_tournament():
    choices = ["rock", "paper", "scissors"]
    player_stats = {"rock": 0, "paper": 0, "scissors": 0}
    player_score = 0
    ai_score = 0
    rounds = 5

    print("Rock Paper Scissors Tournament")
    print("Best of 5 rounds")
    print("Enter: rock, paper, or scissors")

    for round_no in range(1, rounds + 1):
        print(f"\nRound {round_no}")
        player = input("Your move: ").lower()
        
        if player not in choices:
            print("Invalid move. Try again.")
            continue

        player_stats[player] += 1

        # AI Strategy: counter player's most frequent move
        most_common = max(player_stats, key=player_stats.get)
        if most_common == "rock":
            ai = "paper"
        elif most_common == "paper":
            ai = "scissors"
        else:
            ai = "rock"

        # Small randomness to avoid predictability
        if random.random() < 0.3:
            ai = random.choice(choices)

        print("AI chose:", ai)

        if player == ai:
            print("Result: Draw")
        elif (player == "rock" and ai == "scissors") or \
             (player == "paper" and ai == "rock") or \
             (player == "scissors" and ai == "paper"):
            print("Result: You win this round")
            player_score += 1
        else:
            print("Result: AI wins this round")
            ai_score += 1

        print("Score -> You:", player_score, "| AI:", ai_score)

    print("\nTournament Over")
    print("Final Score -> You:", player_score, "| AI:", ai_score)

    print("\nPlayer Move Statistics:")
    for move, count in player_stats.items():
        print(move.capitalize(), ":", count)

    if player_score > ai_score:
        print("\nOverall Winner: You")
    elif ai_score > player_score:
        print("\nOverall Winner: AI")
    else:
        print("\nOverall Result: Draw")

rps_tournament()
