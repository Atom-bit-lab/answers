from typing import List, Tuple

class Npaper:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

def find_subscription_combinations(budget: float, newspapers: List[Npaper]) -> List[Tuple[str, str]]:
    combinations = []
    for i in range(len(newspapers)):
        for j in range(i+1, len(newspapers)):
            total_p = sum(newspapers[i].prices) + sum(newspapers[j].prices)
            if total_p <= budget:
                combinations.append((newspapers[i].name, newspapers[j].name))
    return combinations

newspapers = [
    Npaper("Hindu", [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4]),
    Npaper("ET", [4, 4, 4, 4, 4, 4, 10]),
    Npaper("BM", [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]),
    Npaper("HT", [2, 2, 2, 2, 2, 4, 4])
]

budget = int(input("Input budget"))
combinations = find_subscription_combinations(budget, newspapers)
print(combinations)
