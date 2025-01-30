import random

# Card constants
SUIT_TUPLE = ("Spades", "Hearts", "Clubs", "Diamonds")
RANK_TUPLES = (
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
)
NCARDS = 8


def get_card(deck_list_in):
    """Return a random card from the deck."""
    return deck_list_in.pop()


def shuffle(deck_list_in):
    """Return a shuffled copy of the deck."""
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out


def main():
    print("Welcome to Higher or Lower.")
    print(
        "You have to choose whether the next card to be shown will be higher or lower than the current card."
    )
    print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
    print("You have 50 points to start.")
    print()

    starting_deck_list = []
    for suit in SUIT_TUPLE:
        for value, rank in enumerate(RANK_TUPLES):
            card_dict = {"rank": rank, "suit": suit, "value": value + 1}
            starting_deck_list.append(card_dict)

    score = 50

    while True:  # play multiple games
        print()
        game_deck_list = shuffle(starting_deck_list)
        current_card_dict = get_card(game_deck_list)
        current_card_rank = current_card_dict["rank"]
        current_card_value = current_card_dict["value"]
        current_card_suit = current_card_dict["suit"]
        print(f"Starting card is: {current_card_rank} of {current_card_suit}")
        print()

        for _ in range(NCARDS):
            answer = input(
                f"Will the next card be higher or lower than {current_card_rank} of {current_card_suit}? (enter h or l): "
            ).casefold()
            next_card_dict = get_card(game_deck_list)
            next_card_rank = next_card_dict["rank"]
            next_card_value = next_card_dict["value"]
            next_card_suit = next_card_dict["suit"]
            print(f"Next card is: {next_card_rank} of {next_card_suit}")

            if answer == "h":
                if next_card_value > current_card_value:
                    print("You got it right, it was higher")
                    score += 20
                else:
                    print("Sorry, it was not higher")
                    score -= 15
            elif answer == "l":
                if next_card_value < current_card_value:
                    print("You got it right, it was lower")
                    score += 20
                else:
                    print("Sorry, it was not lower")
                    score -= 15
            else:
                print("Invalid input. Please enter 'h' or 'l'.")

            current_card_rank = next_card_rank
            current_card_value = next_card_value
            current_card_suit = next_card_suit

            print(f"Your score is: {score}")
            print()


if __name__ == "__main__":
    main()
