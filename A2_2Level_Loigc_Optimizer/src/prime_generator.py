from cube import Cube

def generate_prime_implicants(F, D):
    """
    Generate prime implicants from ON-set F and don't-care set D.

    Args:
        F: set of Cube objects representing ON-set
        D: set of Cube objects representing don't-care set

    Returns:
        prime_implicants: set of Cube objects representing prime implicants
    """
    # Combine F and D for merging
    all_cubes = F.union(D)
    current_level = set(F)  # start with ON-set cubes
    prime_implicants = set()  # final primes

    while current_level:
        next_level = set()
        merged_cubes = set()  # track cubes that were merged

        current_list = list(current_level)
        used = set()  # mark which cubes got merged

        # Try merging each pair of cubes
        for i in range(len(current_list)):
            for j in range(i + 1, len(current_list)):
                c1 = current_list[i]
                c2 = current_list[j]
                merged = c1.merge(c2)
                if merged:
                    next_level.add(merged)
                    used.add(c1)
                    used.add(c2)

        # Cubes that could not be merged are prime implicants
        for c in current_level:
            if c not in used:
                prime_implicants.add(c)

        # Move to next level
        current_level = next_level

    return prime_implicants


# --------------------------
# Quick Test
# --------------------------
if __name__ == "__main__":
    from cube import Cube

    # Example ON-set
    F = {Cube("110"), Cube("111"), Cube("101")}
    D = {Cube("011")}  # optional don't-cares

    primes = generate_prime_implicants(F, D)
    print("Prime Implicants:")
    for c in primes:
        print("  ", c)
