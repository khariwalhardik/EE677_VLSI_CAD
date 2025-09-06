# main.py
"""
2-Level Logic Optimizer
Reads a PLA file from 'inputs/', optimizes it using prime implicant generation
and heuristic cover selection, and writes the optimized PLA to 'outputs/'.
"""

from src.pla_to_cubes import pla_to_cubes
from src.prime_generator import generate_prime_implicants
from src.heuristic_cover import select_prime_cover
from src.pla_writer import write_pla

def main():
    # Input PLA file
    input_file_name=input("Enter the input file Name from input folder:\n")
    input_file = f"inputs/{input_file_name}.pla"
    output_file = f"outputs/{input_file_name}_optimized.pla"

    # Step 1: Read PLA and convert to Cube objects
    n, m, F, D = pla_to_cubes(input_file)
    print(f"PLA loaded: {n} inputs, {m} outputs")

    # Input and output labels (can be extracted from parser if needed)
    input_labels = [f"x{i}" for i in range(n)]
    output_labels = [f"f{i}" for i in range(m)]

    # Step 2: Generate prime implicants and select heuristic minimal cover
    selected_cubes_per_output = []
    for j in range(m):
        primes = generate_prime_implicants(F[j], D[j])
        selected = select_prime_cover(F[j], primes)
        selected_cubes_per_output.append(selected)
        print(f"Output {j}: selected {len(selected)} prime implicants")

    # Step 3: Write optimized PLA
    write_pla(output_file, input_labels, output_labels, selected_cubes_per_output)
    print(f"Optimized PLA written to '{output_file}'")

if __name__ == "__main__":
    main()
