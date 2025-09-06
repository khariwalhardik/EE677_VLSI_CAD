from .cube import Cube

def write_pla(filename: str, input_labels, output_labels, selected_cubes_per_output):
    """
    Write optimized cubes to a PLA file, merging cubes across multiple outputs.

    Args:
        filename: path to output PLA file
        input_labels: list of input variable names
        output_labels: list of output variable names
        selected_cubes_per_output: list of sets of Cube objects for each output
    """
    num_inputs = len(input_labels)
    num_outputs = len(output_labels)

    # Merge cubes across outputs
    cube_dict = {}  # key = input pattern, value = list of output bits
    for out_idx, cubes in enumerate(selected_cubes_per_output):
        for cube in cubes:
            if cube.pattern not in cube_dict:
                cube_dict[cube.pattern] = ['0'] * num_outputs
            cube_dict[cube.pattern][out_idx] = '1'

    with open(filename, "w") as f:
        # PLA headers
        f.write(f".i {num_inputs}\n")
        f.write(f".o {num_outputs}\n")
        f.write(".ilb " + " ".join(input_labels) + "\n")
        f.write(".ob " + " ".join(output_labels) + "\n")

        # Write cubes
        for in_pattern, out_bits in cube_dict.items():
            f.write(f"{in_pattern} {''.join(out_bits)}\n")

        f.write(".e\n")


# --------------------------
# Quick Test
# --------------------------
if __name__ == "__main__":
    inputs = ['a', 'b', 'c']
    outputs = ['f0', 'f1']

    # Example selected cubes per output
    selected_cubes = [
        {Cube("11-"), Cube("1-1")},  # Output f0
        {Cube("11-"), Cube("01-")}   # Output f1
    ]

    write_pla("outputs/example_merged.pla", inputs, outputs, selected_cubes)
    print("Optimized PLA written to outputs/example_merged.pla")
