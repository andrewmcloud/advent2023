from dataclasses import dataclass
from collections import Counter

with open("../input/day7.txt") as f:
    input_ = f.read()


@dataclass
class Hand:
    cards: str
    bid: int
    jacks: bool

    @property
    def hand_type(self) -> str:
        card_counter = Counter(self.cards)
        counts = sorted(card_counter.values(), reverse=True)
        hand_type = (counts[0], counts[1]) if len(counts) > 1 else (5, 0)
        jokers = card_counter.get("J", 0)

        hand_types = {
            (5, 0): "five",
            (4, 1): "four",
            (3, 2): "boat",
            (3, 1): "three",
            (2, 2): "two",
            (2, 1): "pair",
            (1, 1): "high",
        }
        hand = hand_types[hand_type]
        if self.jacks:
            return hand_types[hand_type]
        match jokers:
            case 1:
                match hand:
                    case "four":
                        return "five"
                    case "three":
                        return "four"
                    case "two":
                        return "boat"
                    case "pair":
                        return "three"
                    case "high":
                        return "pair"
            case 2:
                match hand:
                    case "boat":
                        return "five"
                    case "two":
                        return "four"
                    case "pair":
                        return "three"
            case 3:
                match hand:
                    case "boat":
                        return "five"
                    case "three":
                        return "four"
            case 4:
                return "five"

        return hand_types[hand_type]

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            raise Exception(f"{other} must be of type Hand.")
        hand_rank = {"five": 0, "four": 1, "boat": 2, "three": 3, "two": 4, "pair": 5, "high": 6}

        card_rank = {
            "A": 13,
            "K": 12,
            "Q": 11,
            "T": 9,
            "9": 8,
            "8": 7,
            "7": 6,
            "6": 5,
            "5": 4,
            "4": 3,
            "3": 2,
            "2": 1,
            "J": 0,
        }
        if self.jacks:
            card_rank["J"] = 10

        if hand_rank[self.hand_type] == hand_rank[other.hand_type]:
            for i in range(len(self.cards)):
                if card_rank[self.cards[i]] == card_rank[other.cards[i]]:
                    continue
                if card_rank[self.cards[i]] > card_rank[other.cards[i]]:
                    return True
                return False

        if hand_rank[self.hand_type] < hand_rank[other.hand_type]:
            return True
        return False


hands = []
joker_hands = []
for line in input_.split("\n"):
    cards, bid = line.split(" ")
    hands.append(Hand(cards, int(bid), True))
    joker_hands.append(Hand(cards, int(bid), False))

part1 = sum(i * hand.bid for i, hand in enumerate(sorted(hands), 1))
part2 = sum(i * joker_hand.bid for i, joker_hand in enumerate(sorted(joker_hands), 1))

print(f"day7:\npart 1: {part1}\npart 2: {part2}")
