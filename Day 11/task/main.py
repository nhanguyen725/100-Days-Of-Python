import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(count, list_of_cards):
    for card in range(count):
        dealer = random.choice(cards)
        list_of_cards.append(dealer)

def calculate_score(list_of_cards):
    current_score = 0
    total = sum(list_of_cards)
    current_score += total
    if total == 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and total > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return current_score

def compare(user_card_list, computer_card_list,
            final_user_score, final_computer_score):
    if final_user_score == 0 or final_computer_score == 0:
        print(f"Your final hand: {user_card_list}, final score: {final_user_score}\n"
              f"Computer's final hand: {computer_card_list}, final score: {final_computer_score}")
        if final_user_score == 0:
            print("Win with a Blackjack 😎")
        elif final_computer_score == 0:
            print("Computer wins with a Blackjack. You lose 😭")
        blackjack()
    elif final_user_score > 21 or final_computer_score > 21:
        print(f"Your final hand: {user_card_list}, final score: {final_user_score}\n"
              f"Opponent's final hand: {computer_card_list}, final score: {final_computer_score}")
        if final_user_score > 21:
            print("You went over. You lose 😭")
        elif final_computer_score > 21:
            print("Opponent went over. You win 😎")
        blackjack()

def blackjack():
    user_cards = []
    computer_cards = []
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        print("\n"* 20)
        print(art.logo)
        deal_card(2, user_cards)
        deal_card(2, computer_cards)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        compare(user_card_list = user_cards, computer_card_list = computer_cards,
            final_user_score = user_score, final_computer_score = computer_score)
        continue_draw = True
        while continue_draw:
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_another_card == "y":
                deal_card(1, user_cards)
                deal_card(1, computer_cards)
                user_score = calculate_score(user_cards)
                computer_score = calculate_score(computer_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}\n"
                        f"Computer's first card: {computer_cards[0]}")
                compare(user_card_list = user_cards, computer_card_list = computer_cards,
                        final_user_score = user_score, final_computer_score = computer_score)
            elif draw_another_card == "n":
                while computer_score != 0 and computer_score < 17:
                    deal_card(1, computer_cards)
                    computer_score = calculate_score(computer_cards)
                continue_draw = False
                user_score = calculate_score(user_cards)
                computer_score = calculate_score(computer_cards)
                compare(user_card_list = user_cards, computer_card_list = computer_cards,
                        final_user_score = user_score, final_computer_score = computer_score)
                if user_score > computer_score:
                    print(f"Your final hand: {user_cards}, final score: {user_score}\n"
                          f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You win 😎")
                    blackjack()
                elif computer_score > user_score:
                    print(f"Your final hand: {user_cards}, final score: {user_score}\n"
                          f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You lose 😭")
                    blackjack()
                elif user_score == computer_score:
                    print(f"Your final hand: {user_cards}, final score: {user_score}\n"
                          f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("It's a draw 🙃")
                    blackjack()
    elif play == "n":
        print("Good game!")

blackjack()