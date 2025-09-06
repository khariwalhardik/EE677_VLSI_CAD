from pla_parser import parse_pla
from cube import Cube

def pla_to_cubes(filename: str):
    """
    Convert PLA file to Cube objects per output.
    Returns:
        n: number of inputs
        m: number of outputs
        F: list of sets of Cube objects for ON-set
        D: list of sets of Cube objects for don't-care set
    """
    pla = parse_pla(filename)
    n, m = pla.num_inputs, pla.num_outputs

    # Initialize sets per output
    F = [set() for _ in range(m)]
    D = [set() for _ in range(m)]

    for in_pat, out_pat in pla.cubes:
        for j, ch in enumerate(out_pat):
            if ch == '1':
                F[j].add(Cube(in_pat))
            elif ch == '-':
                D[j].add(Cube(in_pat))
            # '0' is ignored

    return n, m, F, D

if __name__ == "__main__":
    n, m, F, D = pla_to_cubes("inputs/example1.pla")
    print(f"Inputs: {n}, Outputs: {m}")
    for j in range(m):
        print(f"Output {j} ON-set:")
        for c in F[j]:
            print("  ", c)

        print(f"Output {j} DC-set:")
        for c in D[j]:
            print("  ", c)
