# main.py
"""
2-Level Logic Optimizer
----------------------
Reads a PLA file from 'inputs/', parses it, generates prime implicants,
selects a heuristic minimal cover, and writes an optimized PLA to 'outputs/'.
"""

from src.pla_to_cubes import pla_to_cubes
from src.prime_generator import generate_prime_implicants
from src.heuristic_cover import select_prime_cover
from src.pla_writer import write_pla

def optimize_pla(input_file: str, output_file: str, input_labels, output_labels):
    # Step 1: Parse PLA and convert to Cube objects
    n, m, F, D = pla_to_cubes(input_file)

    # Step 2: Generate prime implicants and select minimal cover for each output
    selected_cubes_per_output = []
    for j in range(m):
        primes = generate_prime_implicants(F[j], D[j])
        selected = select_prime_cover(F[j], primes)
        selected_cubes_per_output.append(selected)

    # Step 3: Write optimized cubes to PLA file
    write_pla(output_file, input_labels, output_labels, selected_cubes_per_output)
    print(f"Optimized PLA written to {output_file}")


if __name__ == "__main__":
    # Example usage
    input_file = "inputs/example1.pla"
    output_file = "outputs/example1_optimized.pla"
    
    # Input and output labels must match your PLA headers
    input_labels = ['a', 'b', 'c']
    output_labels = ['f']

    optimize_pla(input_file, output_file, input_labels, output_labels)
