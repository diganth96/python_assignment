def find_stone_piles(n):
    piles = []
    while n > 0:
        if n % 2 == 0:
            n -= 1
        piles.append(n)
        n -= 2
    return piles
n = 7
stone_piles = find_stone_piles(n)
print("Stones in a single pile =", stone_piles)
