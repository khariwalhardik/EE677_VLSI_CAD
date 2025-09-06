from cube import Cube

def select_prime_cover(F, prime_implicants):
    """
    Select a subset of prime implicants to cover all ON-set cubes (F)
    using a simple greedy heuristic:
        1. Prefer cubes that cover more minterms.
        2. Prefer cubes with fewer literals (smaller terms).

    Args:
        F: set of Cube objects representing ON-set
        prime_implicants: set of Cube objects representing prime implicants

    Returns:
        selected_primes: set of Cube objects forming a heuristic minimal cover
    """
    # Convert F to list of minterms (strings)
    minterms = list(F)
    uncovered = set(minterms)
    selected_primes = set()

    # Greedy selection loop
    while uncovered:
        # Score each prime: (# of uncovered minterms it covers, -literal count)
        scores = []
        for p in prime_implicants:
            cover_count = sum(1 for m in uncovered if p.covers(m.pattern))
            if cover_count > 0:
                # Tuple: (how many uncovered minterms it covers, -literals, cube object)
                scores.append((cover_count, -p.literal_count(), p))

        if not scores:
            raise ValueError("No prime implicant can cover remaining minterms!")

        # Pick the best prime using max by first two numeric fields
        best_prime = max(scores, key=lambda x: (x[0], x[1]))[2]

        # Add to selected primes
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

    # Example ON-set
    F = {Cube("110"), Cube("111"), Cube("101")}
    D = {Cube("011")}  # optional don't-cares

    # Generate prime implicants
    primes = generate_prime_implicants(F, D)

    # Select heuristic minimal cover
    selected = select_prime_cover(F, primes)

    print("Selected Prime Cover:")
    for c in selected:
        print("  ", c)
