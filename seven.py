from dataclasses import dataclass, field

CARD_ORDER = [
    "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"
    ]
NEW_CARD_ORDER = [
    "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"
    ]


@dataclass
class Card():
    value: chr

    def __eq__(self, other) -> bool:
        return other.value == self.value

    def __lt__(self, other) -> bool:
        return CARD_ORDER.index(self.value) > CARD_ORDER.index(other.value)


class NewCard(Card):
    def __lt__(self, other) -> bool:
        return (
            NEW_CARD_ORDER.index(
                self.value) > NEW_CARD_ORDER.index(other.value)
        )


@dataclass
class Hand():
    cards: list[Card]
    bid: int
    rank: int = field(init=False)

    def __post_init__(self):
        self.rank = self._calculate_rank()

    def __repr__(self):
        cards = "".join([c.value for c in self.cards])
        return f"Rank: {self.rank}, Cards: {cards}, Bid: {self.bid}"

    def __eq__(self, other) -> bool:
        return self.rank == other.rank and self.cards == other.cards

    def __lt__(self, other) -> bool:
        if self.rank != other.rank:
            return self.rank < other.rank
        else:
            for sc, oc in zip(self.cards, other.cards):
                if sc != oc:
                    return sc < oc

    def _calculate_rank(self) -> int:
        return self._counts_to_rank(
            [self.cards.count(Card(x)) for x in CARD_ORDER])

    def _counts_to_rank(self, number_cards: int) -> int:
        if max(number_cards) > 3:
            return max(number_cards) + 1
        elif 3 in number_cards and 2 in number_cards:
            return 4
        elif 3 in number_cards:
            return 3
        elif number_cards.count(2) == 2:
            return 2
        elif 2 in number_cards:
            return 1
        else:
            return 0


class NewHand(Hand):
    def _calculate_rank(self) -> int:
        number_j = self.cards.count(NewCard("J"))
        counts = [
            self.cards.count(NewCard(x))
            for x in NEW_CARD_ORDER if x != "J"]
        res = []
        found_max = False
        for c in counts:
            if c == max(counts) and not found_max:
                res.append(c + number_j)
                found_max = True
            else:
                res.append(c)
        return self._counts_to_rank(res)


def solve1(input: list[str]) -> int:
    hands = []
    for line in input:
        hand = Hand([Card(c) for c in line.split()[0]], int(line.split()[1]))
        hands.append(hand)

    hands.sort()
    res = 0
    for i, h in enumerate(hands):
        res += h.bid * (i + 1)
    return res


def solve2(input: list[str]) -> int:
    hands = []
    for line in input:
        hand = NewHand(
            [NewCard(c) for c in line.split()[0]], int(line.split()[1]))
        hands.append(hand)

    hands.sort()
    res = 0
    for i, h in enumerate(hands):
        res += h.bid * (i + 1)
    return res
