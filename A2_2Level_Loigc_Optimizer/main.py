# main.py
"""
2-Level Logic Optimizer
Organized I/O structure:
    inputs/txt/   -> Boolean expression input files (.txt)
    inputs/pla/   -> PLA input files (.pla)
    outputs/txt/  -> Optimized SOP expression outputs (.txt)
    outputs/pla/  -> Optimized PLA outputs (.pla)
"""

import os
from src.pla_to_cubes import pla_to_cubes
from src.prime_generator import generate_prime_implicants
from src.heuristic_cover import select_prime_cover
from src.pla_writer import write_pla
from src.sop_to_pla import sop_to_pla, write_pla_file
from src.pla_to_sop import pla_to_sop_text_multi


def main():
    print("\n=== 2-Level Logic Optimizer ===")
    print("Select input type:")
    print("  1. Boolean Expression Text File (.txt)")
    print("  2. PLA File (.pla)")
    choice = input("Enter 1 or 2: ").strip()

    if choice not in {"1", "2"}:
        print("❌ Invalid choice! Exiting.")
        return

    file_name = input("Enter the base file name (without extension): ").strip()

    # Prepare folders
    os.makedirs("inputs/txt", exist_ok=True)
    os.makedirs("inputs/pla", exist_ok=True)
    os.makedirs("outputs/txt", exist_ok=True)
    os.makedirs("outputs/pla", exist_ok=True)

    if choice == "1":
        # Input: Boolean expression text
        input_txt_file = f"inputs/txt/{file_name}.txt"
        pla_data = sop_to_pla(input_txt_file)

        # Convert to PLA and save in inputs/pla
        input_pla_file = f"inputs/pla/{file_name}.pla"
        write_pla_file(pla_data, input_pla_file)
        print(f"📄 Converted '{input_txt_file}' → '{input_pla_file}'")

    else:
        # Input: PLA file directly
        input_pla_file = f"inputs/pla/{file_name}.pla"

    # Output file paths
    pla_output_file = f"outputs/pla/{file_name}_opt.pla"
    txt_output_file = f"outputs/txt/{file_name}_opt.txt"

    # Step 1: Read PLA and convert to cubes
    n, m, F, D = pla_to_cubes(input_pla_file)
    print(f"\n📥 PLA loaded: {n} inputs, {m} outputs")

    # Default labels (if not parsed)
    input_labels = [f"x{i}" for i in range(n)]
    output_labels = [f"f{i}" for i in range(m)]

    # Step 2: Prime implicant generation + heuristic cover selection
    selected_cubes_per_output = []
    for j in range(m):
        primes = generate_prime_implicants(F[j], D[j])
        selected = select_prime_cover(F[j], primes)
        selected_cubes_per_output.append(selected)
        print(f"   ➤ Output {j}: selected {len(selected)} prime implicants")

    # Step 3: Write optimized PLA
    write_pla(pla_output_file, input_labels, output_labels, selected_cubes_per_output)
    print(f"\n✅ Optimized PLA written to '{pla_output_file}'")

    # Step 4: Convert optimized PLA → SOP text
    sop_text = pla_to_sop_text_multi(pla_output_file)
    with open(txt_output_file, "w") as f:
        f.write(sop_text)
    print(f"✅ SOP expression written to '{txt_output_file}'")


if __name__ == "__main__":
    main()
