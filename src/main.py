from game_engine import GameEngine

def main():

    engine = GameEngine()

    print("Setting up game...")
    engine.setup()

    print("Starting game")
    round_count = 0

    while not engine.is_game_over():
        round_count += 1
        print()
        print(f"Round: {round_count}")

        engine.play_round()

        # Limit nr of rounds to 250
        if round_count > 250:
            print("The game took too long. Canceling game")
            break

    print("The game is over")
    player1_cards = len(engine.player1)
    player2_cards = len(engine.player2)

    if player1_cards > player2_cards:
        print("Player 1 won the game!")

    elif player2_cards > player1_cards:
        print("Player 2 won the game!")

    else:
        print("The game ended in a draw!")



if __name__ == "__main__":
    main()
