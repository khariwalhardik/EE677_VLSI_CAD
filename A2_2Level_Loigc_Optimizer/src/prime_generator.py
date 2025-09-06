from .cube import Cube

def generate_prime_implicants(F, D):
    """
    Generate prime implicants from ON-set F and don't-care set D.
    """
    all_cubes = F.union(D)
    current_level = set(F)  # start with ON-set
    prime_implicants = set()

    while current_level:
        next_level = set()
        used = set()

        current_list = list(current_level)
        for i in range(len(current_list)):
            for j in range(i + 1, len(current_list)):
                merged = current_list[i].merge(current_list[j])
                if merged:
                    next_level.add(merged)
                    used.add(current_list[i])
                    used.add(current_list[j])

        # Add cubes that could not be merged to prime implicants
        prime_implicants.update(c for c in current_level if c not in used)

        current_level = next_level

    return prime_implicants


# --------------------------
# Quick Test
# --------------------------
if __name__ == "__main__":
    from cube import Cube

    F = {Cube("110"), Cube("111"), Cube("101")}
    D = {Cube("011")}

    primes = generate_prime_implicants(F, D)
    print("Prime Implicants:")
    for c in primes:
        print("  ", c)
