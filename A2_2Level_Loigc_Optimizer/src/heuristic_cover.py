from .cube import Cube

def select_prime_cover(F, prime_implicants):
    """
    Select a subset of prime implicants to cover all ON-set cubes (F)
    using a greedy heuristic.
    """
    uncovered = set(F)
    selected_primes = set()

    while uncovered:
        scores = []
        for p in prime_implicants:
            cover_count = sum(1 for m in uncovered if p.covers(m.pattern))
            if cover_count > 0:
                # Score: (number of uncovered minterms covered, -number of literals)
                scores.append((cover_count, -p.literal_count(), p))

        if not scores:
            raise ValueError("No prime implicant can cover remaining minterms!")

        # Select the best prime
        best_prime = max(scores, key=lambda x: (x[0], x[1]))[2]

        selected_primes.add(best_prime)
        # Remove covered minterms
        uncovered = {m for m in uncovered if not best_prime.covers(m.pattern)}

    return selected_primes


# --------------------------
# Quick Test
# --------------------------
if __name__ == "__main__":
    from cube import Cube
    from prime_generator import generate_prime_implicants

    F = {Cube("110"), Cube("111"), Cube("101")}
    D = {Cube("011")}

    primes = generate_prime_implicants(F, D)
    selected = select_prime_cover(F, primes)

    print("Selected Prime Cover:")
    for c in selected:
        print("  ", c)
