from sys import stdin
input = stdin.readline


def sieve_of_eratosthenes(cards: list) -> list:
    card_2_score = {card:0 for card in cards}
    top_card = max(cards)
    
    for card in sorted(cards):
        for comp in range(card+card, top_card+1, card):
            if comp in card_2_score:
                card_2_score[card] += 1
                card_2_score[comp] -= 1
                
    return [card_2_score[card] for card in cards]


players = int(input())
player_cards = list(map(int, input().split()))
answer = sieve_of_eratosthenes(player_cards)
print(*answer)